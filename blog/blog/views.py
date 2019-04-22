from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from .forms import AddPostForm
from .models import Post
from django.urls import reverse


def hello_world(request):
    return HttpResponse('Hello, world!')


class MainPageView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class PostAdd(generic.CreateView):
    template_name = 'post_add.html'
    form_class = AddPostForm

    def get_success_url(self):
        return reverse('index')


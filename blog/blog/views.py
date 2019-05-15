from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from .forms import AddPostForm, AddCommentForm
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
    # s = Post.objects.order_by('-comment__author')
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     s = qs.filter(id=self.kwargs['pk']).order_by('-comment__creation_date')
    #     for i in s:
    #         print(i)
    #     return qs.filter(id=self.kwargs['pk']).order_by('comment__creation_date')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_add_url'] = '/topic/{}/add_comment'.format(context['post'].id)
        return context


class CommentAdd(generic.CreateView):
    template_name = 'comment_add.html'
    form_class = AddCommentForm

    def get_initial(self):
        return {
            "topic": self.kwargs['topic_pk']
        }

    def get_success_url(self):
        return '/topic/{}'.format(self.kwargs['topic_pk'])


class PostAdd(generic.CreateView):
    template_name = 'post_add.html'
    form_class = AddPostForm

    def get_success_url(self):
        return reverse('index')


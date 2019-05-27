from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import AddPostForm, AddCommentForm
from .models import Post, User, Comment
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPageView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get('num_visits',0)
        self.request.session['num_visits'] = num_visits + 1
        context['num_visits'] = num_visits

        return context


class PopularView(generic.ListView):
    model = Post
    template_name = 'popular.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-visit_count')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def increment_visit_counter(self):
        obj = self.get_object()
        obj.visit_count += 1
        obj.save()

    def get(self, request, pk):
        post = self.get_object()
        url = '/topic/{}/add_comment'.format(post.id)
        hide_url = '/topic/{}/hide'.format(post.id)
        show_url = '/topic/{}/show'.format(post.id)
        context = {'post': post, 'comment_add_url': url, 'hide_url': hide_url, 'show_url': show_url}
        self.increment_visit_counter()
        return render(request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment_add_url'] = '/topic/{}/add_comment'.format(context['post'].id)
    #     return context


class CommentAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'comment_add.html'
    form_class = AddCommentForm

    def get_initial(self):
        return {
            "topic": self.kwargs['topic_pk'],
            "author": self.request.user
        }

    def get_success_url(self):
        return '/topic/{}'.format(self.kwargs['topic_pk'])


class PostAdd(LoginRequiredMixin, generic.CreateView):
    template_name = 'post_add.html'
    form_class = AddPostForm

    def get_initial(self):
        return {
            "post_author": self.request.user
        }

    def get_success_url(self):
        return reverse('index')


class SearchView(generic.ListView):
    template_name = 'search_results.html'
    model = Post
    context_object_name = 'search_results'

    def get_queryset(self):
        return (Post.objects.filter(
            post_title__icontains=self.request.GET['title']
        ))


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'profile.html'


class MyPostView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'my_posts.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return (Post.objects.filter(
            post_author=self.request.user
        ))


class MyCommentView(LoginRequiredMixin, generic.ListView):
    model = Comment
    template_name = 'my_comments.html'
    context_object_name = 'comments_list'

    def get_queryset(self):
        return (Comment.objects.filter(
            author=self.request.user
        ).order_by('-creation_date'))


class HidePostView(LoginRequiredMixin, generic.DetailView):
    model = Post

    def get(self, request, pk):
        post = self.get_object()
        if self.request.user == post.post_author:
            post.is_hidden = True
            post.save()
        return redirect('index')


class ShowPostView(LoginRequiredMixin, generic.DetailView):
    model = Post

    def get(self, request, pk):
        post = self.get_object()
        if self.request.user == post.post_author:
            post.is_hidden = False
            post.save()
        return redirect('index')


from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text']
        widgets = {
            'post_title': forms.TextInput(attrs={'class':'form-control'}),
            'post_text': forms.Textarea(attrs={'rows':'5','class':'form-control'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['topic', 'author', 'body']
        labels = {
            'author': 'Comment author',
            'body': 'Comment body'
        }
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'rows': '5', 'class': 'form-control'}),
            'topic': forms.HiddenInput()
        }

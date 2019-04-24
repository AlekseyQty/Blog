from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text']
        widgets = {
            'post_title': forms.TextInput(attrs = {'class':'form-control'}),
            'post_text': forms.Textarea(attrs = {'rows':'5','class':'form-control'})
        }
from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('title','content','image_1','image_2')

class CommentForm(forms.ModelForm):

     class Meta:
        model = Comment
        fields = ['post']

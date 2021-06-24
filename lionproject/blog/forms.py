from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('title','content','image_1','image_2')

# def check_title_less_than_three(title):
#     if len(title) < 3:
#         raise forms.ValidationError('제목이 세 글자 미만입니다.')

# class PostForm(forms.Form):
#     title = forms.CharField(required=False, validators=[check_title_less_than_three])
#     content = forms.CharField(widget=forms.Textarea)
#     image_1 = forms.ImageField(required=False)
#     image_2 = forms.ImageField(required=False)


from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .forms import CommentForm
from .models import Post
from .models import Comment
from datetime import datetime

def home(request):
    return render(request, 'main/home.html')

def like(request):
    return render(request, 'main/like.html')

def dislike(request):
    return render(request, 'main/dislike.html')

def sns(request):
    return render(request, 'main/sns.html')

def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request,'main/post_list.html', context)

def post_detail(request,post_id):
    post_detail = get_object_or_404(Post,pk=post_id)
    comments = Comment.objects.filter(post = post_id)
    if request.method == "POST":
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = datetime.now()
        comment.save()
    return render(request,'main/post_detail.html',{'post':post_detail, 'comments':comments})


def post_new(request):
    if request.method == 'GET':
        form = PostForm()

    elif request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('post_detail', post_id=post.id)

    return render(request, 'main/post_new.html', {
        'form': form,
    }) 

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post_list')


def post_edit(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)

    elif request.method =='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post = form.save()
            return redirect('post_detail', post_id=post.id)
            
    return render(request, 'main/post_edit.html', {
        'form': form,
        'post': post,
    })

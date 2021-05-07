from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts' : posts,
    })

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "GET":
        post.click()

    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

def post_init(request, post_id):
    post = Post.objects.get(id=post_id)

    post.init()

    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('post_list')
    
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('post_detail', post.id)
    else:
        form = PostForm(instance=post)
            
        return render(request, 'blog/post_edit.html', {
            'form': form,
            'post': post,
            })    

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()

            return redirect('post_detail', post.id)
    else:
        form = PostForm()
            
        return render(request, 'blog/post_new.html', {
            'form': form,
            })




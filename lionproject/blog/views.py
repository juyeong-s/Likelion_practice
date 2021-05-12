from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Post

def post_list(request):
    post_list = Post.objects.all()  #Post클래스에서 데이터베이스에서 데이터를 가져옴
    context = {
        'post_list': post_list,  #'post_list'가 html에서 for문에서 쓰임, 'post_list'이름을 html이 알아야됨
    }
    return render(request,'blog/post_list.html', context)
#key를 통해 value를 가져오니까
#context['key']랑 같은거임

  #첫번재 인자는 무조건 repuest  post_id 는 urls.py에서 <int: post_id> 이 이름임
def post_detail(request, post_id):  

    post = Post.objects.get(id=post_id)
    context = {
        'post_id':post_id,
        'post':post
    }
    return render(request,'blog/post_detail.html', context)

def post_new(request):
    if request.method == 'GET':
        form = PostForm()

    elif request.method =='POST':
        #사용자가 입력한 데이터를 저장하는 부분
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  #사용자가 입력한 데이터에 문제가 없으면 if문 실행
            post = form.save()
            return redirect('post_detail', post_id=post.id)

    return render(request, 'blog/post_new.html', {
        'form': form,
    }) 


def post_edit(request, post_id):

    post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, id=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)

    elif request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id=post.id)
            
    return render(request, 'blog/post_edit.html', {
        'form': form,
        'post': post,
    })

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    #post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')


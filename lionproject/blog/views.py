from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Post

def post_list(request):
    post_list = Post.objects.all()  #PostŬ�������� �����ͺ��̽����� �����͸� ������
    context = {
        'post_list': post_list,  #'post_list'�� html���� for������ ����, 'post_list'�̸��� html�� �˾ƾߵ�
    }
    return render(request,'blog/post_list.html', context)
#key�� ���� value�� �������ϱ�
#context['key']�� ��������

  #ù���� ���ڴ� ������ repuest  post_id �� urls.py���� <int: post_id> �� �̸���
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
        #����ڰ� �Է��� �����͸� �����ϴ� �κ�
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  #����ڰ� �Է��� �����Ϳ� ������ ������ if�� ����
            post = form.save(commit=False)
            post.user = request.user
            post.save(commit=True)

            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # image_1 = form.cleaned_data['image_1']
            # image_2 = form.cleaned_data['image_2']
            # post = Post.objects.create(title=title,
            #                             content=content, 
            #                             image_1=image_1,
            #                             image_2=image_2)

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


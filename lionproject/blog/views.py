from django.shortcuts import render, redirect, get_object_or_404 #페이지를 찾을 수 없을 때 404 띄움
from django.utils import timezone
from .models import Blog

def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {
        'blogs':blog })

def detail(request, id): #html에 blog.id넣어주면 글 순서대로 1,2,3,4 번호가 뜸
    blog = get_object_or_404(Blog, pk = id) #pk = Primaey Key  글의 id를 찾아서 blog에 넣어줌
    return render(request, 'detail.html', {
        'blog' : blog
    })

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()  #Blog의 object가 됨
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST.get('body', '')
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {
        'blog': edit_blog,
    })

def update(request, id):
    update_blog = Blog.objects.get(id =id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST.get('body', '')
    update_blog.pub_date = timezone.now()
    update_blog.save() #꼭 저장 필요.
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
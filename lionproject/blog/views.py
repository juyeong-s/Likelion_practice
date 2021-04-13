from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()  #Post클래스에서 데이터베이스에서 데이터를 가져옴
    context = {
        'post_list': post_list,  #'post_list'가 html에서 for문에서 쓰임, 'post_list'이름을 html이 알아야됨
    }
    return render(request,'blog/post_list.html', context)
#key를 통해 value를 가져오니까
#context['key']랑 같은거임
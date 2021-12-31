from django.shortcuts import render, redirect
from django.utils import timezone
from blog.form import PostForm
from blog.models import Post


def index(request):
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    #글쓰기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)   #form에 입력된 자료 가져오기
        if form.is_valid():
            post = form.save(commit=False)  #가저장
            post.pub_date = timezone.now()
            post.save()     #실제저장
            return redirect('blog:index')   #등록후 블로그홈으로 경로이동
    form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)


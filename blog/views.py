from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
# Change

def all_blogs(request):
    # the next line takes the latest 3 entries of the blog ordered desc by date
    blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
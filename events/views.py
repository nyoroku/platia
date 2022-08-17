from django.shortcuts import render, get_object_or_404
from .forms import ApplicationForm
from .models import Blog
from home.models import Latest

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def apply_course(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return render(request, 'application/applied.html', {'application': application})

    else:
        form = ApplicationForm
    return render(request, 'application/applycourse.html', {'form': form})


def blog_list(request):
    blogs = Blog.published.all()
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog/bloglist.html', {'blogs': blogs, 'page': page})


def blog_detail(request, year, month, day, blog):
    blog = get_object_or_404(Blog, slug=blog)
    return render(request, 'blog/blogdetail.html', {'blog': blog})






from django.shortcuts import render, get_object_or_404
from models import Latest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def allevents(request):
    happens = Latest.objects.order_by('-created')
    paginator = Paginator(happens, 5)
    page = request.GET.get('page')
    try:
        happens = paginator.page(page)
    except PageNotAnInteger:
        happens = paginator.page(1)
    except EmptyPage:
        happens = paginator.page(paginator.num_pages)
    return render(request, 'event/event.html', {'happens': happens, 'page': page})



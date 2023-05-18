from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

from .models import ( Blog
)

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-created')
    template_name = 'home.html'
    context = { 
        "blogs": blogs
    }
    return render(request, template_name, context)


def blogs(request):
    queryset = Blog.objects.order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
     

    template_name = 'blog.html'
    
    context = { 
        "blogs": blogs,
        "paginator": paginator
        }
    return render(request, template_name, context)
    

def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = { 
        "blog": blog,
         } 
    return render(request, 'blog_details.html', context)



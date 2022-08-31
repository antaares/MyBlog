from django.shortcuts import render

from django.views.generic import ListView

from .models import Article

# Create your views here.


def index(request):
    return render(request, 'index.html')




class ArticleListView(ListView):
    model = Article
    template_name = 'blog_temp/articles.html'
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView

from .models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'blog_temp/articles.html', context=context)

def hello(request):
    return HttpResponse("Hello guys. this blank page.")


class ArticleListView(ListView):
    model = Article
    template_name = 'blog_temp/articles.html'
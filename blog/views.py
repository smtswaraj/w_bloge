from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Article

def homepage(request):
    articles = Article.objects.all()
    return render(request, 'blog/homepage.html', {'articles': articles})

def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def load_more_articles(request):
    page = int(request.GET.get('page', 1))
    articles = Article.objects.all()[page * 10:(page + 1) * 10]

    if not articles:
        return HttpResponse("")

    context = {'articles': articles}
    return HttpResponse(render_to_string('blog/load_more_articles.html', context))


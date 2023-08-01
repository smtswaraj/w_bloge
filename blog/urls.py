from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('article/<int:article_id>/', views.article_page, name='article_page'),
    # path('load_more_articles/', views.load_more_articles, name='load_more_articles'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

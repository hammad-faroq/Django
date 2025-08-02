# from django.urls import path, reverse_lazy
# from . import views

# app_name='myarts'
# urlpatterns = [
#     path('', views.ArticleListView.as_view(), name='all'),
#     path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
#     path('article/create', 
#         views.ArticleCreateView.as_view(success_url=reverse_lazy('myarts:all')), name='article_create'),
#     path('article/<int:pk>/update', 
#         views.ArticleUpdateView.as_view(success_url=reverse_lazy('myarts:all')), name='article_update'),
#     path('article/<int:pk>/delete', 
#         views.ArticleDeleteView.as_view(success_url=reverse_lazy('myarts:all')), name='article_delete'),
# ]
from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
]
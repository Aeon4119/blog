from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='blog'),
    path('about/', views.about, name='about'),
    path('pages/', views.BlogListView.as_view(), name='blog-list'),
    path('pages/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('pages/new/', views.BlogCreateView.as_view(), name='blog-create'),
    path('pages/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('pages/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),

]

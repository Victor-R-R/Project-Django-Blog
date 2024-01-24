from django.urls import path
from .views import BlogHomeView, BlogPostCreateView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView


app_name = 'posts'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetailView.as_view(), name='detail'),
    path('update/<str:slug>/', BlogPostUpdateView.as_view(), name='update'),
    path('delete/<str:slug>/', BlogPostDeleteView.as_view(), name='delete'),
]

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('shops/', views.ShopsView.as_view(), name='shops'),
]

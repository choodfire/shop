from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/', views.CategoryCatalogView.as_view(), name='category_catalog'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('stores/', views.StoresView.as_view(), name='stores'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
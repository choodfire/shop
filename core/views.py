from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from .models import Product, CATEGORIES, Store
from mixins.mixins import TitleMixin


class IndexView(TitleMixin, ListView):
    model = Product
    title = 'Main page'
    template_name = 'core/index.html'

class CatalogView(TitleMixin, TemplateView):
    template_name = 'core/catalog.html'
    title = 'Catalog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORIES
        return context

class ProductView(TitleMixin, DetailView):
    model = Product
    template_name = 'core/product.html'

    def get_title(self):
        return self.object.name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.all().exclude(id=self.object.id)[:4]
        return context

class AboutView(TitleMixin, TemplateView):
    template_name = 'core/about.html'
    title = 'About'

class FAQView(TitleMixin, TemplateView):
    template_name = 'core/faq.html'
    title = 'Frequently asked questions'

class StoresView(TitleMixin, ListView):
    model = Store
    title = 'Stores'
    template_name = 'core/stores.html'

class LoginView(TitleMixin, LoginView):
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse('core:index')

class SignupView(TitleMixin, TemplateView):
    template_name = 'core/signup.html'

    def get_success_url(self):
        return reverse('core:index')

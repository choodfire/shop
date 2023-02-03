from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Product, CATEGORIES


class IndexView(ListView):
    model = Product
    template_name = 'core/index.html'

class CatalogView(TemplateView):
    template_name = 'core/catalog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORIES
        return context

class ProductView(DetailView):
    model = Product
    template_name = 'core/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.all().exclude(id=self.object.id)[:4]
        return context
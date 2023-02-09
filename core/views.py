from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .forms import RegistrationForm, UserChangePFPForm, UserChangeNameForm
from .models import Product, Store, CustomUser, Category
from mixins.mixins import TitleMixin

class IndexView(TitleMixin, ListView):
    model = Product
    title = 'Main page'
    template_name = 'core/index.html'

class CatalogView(TitleMixin, ListView):
    template_name = 'core/catalog.html'
    title = 'Catalog'
    model = Category

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

class MyLoginView(TitleMixin, LoginView):
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse('core:index')

class SignupView(TitleMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'core/signup.html'
    title = "Sign up"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_successful_url())

    def get_successful_url(self):
        return reverse('core:index')

class MyLogoutView(LogoutView):
    def get_success_url(self):
        return reverse('core:index')

class ProfileView(TitleMixin, UpdateView):
    template_name = 'core/profile.html'
    model = CustomUser
    fields = ['username', 'profile_picture']
    title = 'Profile'
    success_url = ''

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('core:profile')


from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import ContactForm
from .models import Blog,Portfolio,Certificate,Testimonial

class IndexView(generic.TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        testimonial = Testimonial.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        blog = Blog.objects.filter(is_active=True)
        certificate = Certificate.objects.filter(is_active=True)

        context['testimonial'] = testimonial
        context['portfolio'] = portfolio
        context['blog'] = blog
        context['certficate'] = certificate
        return context

class ContactView(generic.FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self,form):
        form.save()
        messages.success('Thank you for contacting Wycliff,will reach out to you soon')
        return super().form_valid(form)

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'core/portfolio.html'
    Paginate_by = 10

    def get_queryset(self):
        super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    tempate_name = 'core/portfolio-detail.html'

class BlogView(generic.ListView):
    model = Blog
    template_name = 'core/blog.html'
    Paginate_by = 10

    def get_queryset(self):
        super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'core/blog-detail.html'

from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.contrib import messages
from .forms import ContactForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.paginator import Paginator
from django.db.models import Q

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

    # Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = Type.objects.all()
        service = Services.objects.all().order_by('-id')
        skill = Skill.objects.all().order_by('-id')
        portfolio = Portfolio.objects.all().order_by('-id')
        portfolio_type = Portfolio.objects.values('type').distinct()
        education = Education.objects.all().order_by('-id')
        experiecne = Experience.objects.all().order_by('-id')
        blog = Blog.objects.all().order_by('-id')
        context.update({'services': service,
                        'skills': skill,
                        'portfolios': portfolio,
                        'portfolio_type': portfolio_type,
                        'educations': education,
                        'experiences': experiecne,
                        'blogs': blog,
                        'types': type
                        })
        return context
    # error comming in message
    def post(self, request, *args, **kwargs):
        messageForm = ContactForm(request.POST)
        if messageForm.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            try:
                validate_email(email)
                if username and not email and not subject and not message:
                    messages.add_message(request, messages.WARNING, 'Please enter the required field!')
                    return render(request, self.template_name)
                else:
                    print(username, email, subject, message)
                    messageObject = Message.objects.create(
                        username = username,
                        email = email,
                        subject = subject,
                        message = message
                    )
                    messageObject.save()
                    messages.add_message(request, messages.INFO, 'Thank you for your feedback!')
                    return render(request, self.template_name)
            except ValidationError as e:
                print(e)
        else:
            print(messageForm.errors.as_data())

        


class PortfolioView(TemplateView):
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = Type.objects.all()
        portfolio = Portfolio.objects.all().order_by("-id")
        context['types'] = type
        context["portfolios"] = portfolio
        return context

class PortfolioDetailView(TemplateView):
    template_name = "portfolio-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        url_slug = self.kwargs['slug']
        portfolio_detail = Portfolio.objects.get(slug=url_slug)
        
        context['portfolio'] = portfolio_detail
        return context

class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bloglist = Blog.objects.all().order_by("-id")
        paginator = Paginator(bloglist, 3)
        page_number = self.request.GET.get('page')
        blog_list = paginator.get_page(page_number)
        context['bloglist'] = blog_list

        search_keyword = self.request.GET.get('search')
        if search_keyword:
            print("search keyword: ",search_keyword)
            results = Blog.objects.filter(
                Q(title__icontains=search_keyword) | Q(type__type__icontains=search_keyword) | Q(name__icontains=search_keyword)
            )
            print("this is final: ", results)
            context['searchlist'] = results
        else:
            pass

        type = Type.objects.all()
        context['typelist'] = type

        return context 

class BlogDetailView(TemplateView):
    template_name = "blog-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        blog_detail = Blog.objects.get(slug=url_slug)
        print(blog_detail.listing_overivew)
        context['blog'] = blog_detail
        return context

class TypeView(TemplateView):
    template_name = "type.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        type = Type.objects.get(slug=url_slug)
        if type is not None:
            type_blog = Blog.objects.filter(type=type)
            context['typeblog'] = type_blog
        context['type'] = type
        typelist = Type.objects.all().order_by("-id")
        context['typelist'] = typelist
        return context
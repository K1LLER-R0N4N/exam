from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost
from .models import mycar

def home_page(request):
  mymembers = BlogPost.objects.all().values()
  template = loader.get_template('home_page.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = BlogPost.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def my_list(request):
  mycars = mycar.objects.all()
  template = loader.get_template('my_list.html')
  data = {
    'mycar': mycars,
  }
  return HttpResponse(template.render(data, request))




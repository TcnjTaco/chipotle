from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .models import *
# Create your views here.

class Homepage(TemplateView):
    template_name = 'landing.html'

class Search(ListView):
    model = courseInfo
    template_name = 'search.html'
    print("before method")
    def get_queryset(self):
        query =  self.request.GET.get('q')
        object_list = courseInfo.objects.filter(
            Q(class_id__icontains=query) | Q(course_code__icontains=query) |
            Q(professor__icontains=query) | Q(day__icontains=query) |
            Q(time__icontains=query)
        )
        print("in method")
        return object_list
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import *

# Error views.

# def page404 (request, exception):
#     return render(request, 'core/404.html')

# def page500 (request):
#     return render(request, 'core/serverError.html')

# class HomepageView(TemplateView):
#     template_name = 'core/homepage.html'

# class LegalView(ListView):
#     context_object_name = 'privacy'
#     queryset = Privacy.objects.order_by('-date')
#     template_name = 'core/legal.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['terms'] = Terms.objects.order_by('-date')
#         return context
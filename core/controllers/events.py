from django.views.generic import TemplateView, ListView
from ..models import Event

class EventView(TemplateView):
    template_name = 'core/events.html'

# class EventList(ListView):
#     context_object_name = 'events'
#     queryset = Event.objects.filter(date__lte = datetime.date.today()).order_by('-date')
#     template_name = 'core/events.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['gigs'] = Event.objects.filter(date__gte = datetime.date.today()).order_by('-date')
#         return context

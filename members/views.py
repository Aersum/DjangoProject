from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Event


class IndexView(ListView):
    model = Event
    template_name = 'members/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = "All events"
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'members/event.html'


def hello_there(request, name):
    return render(
        request,
        'members/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Max

from .models import Gate, Cafe, Category, Menu

# Create your views here.


class IndexView(generic.ListView):
    model = Gate
    template_name = 'cafeyo/index.html'
    context_object_name = 'gate_list'

    def get_queryset(self):
        return Gate.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Gate
    template_name = 'cafeyo/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        max_id = Cafe.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)
            context['random_cafe'] = Cafe.objects.filter(pk=pk).first()
            if context['random_cafe']:
                return context


class ResultsView(generic.DetailView):
    model = Cafe
    template_name = 'cafeyo/results.html'

    # random menu pick v.2
    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        max_id = Menu.objects.all().aggregate(max_id=Max('id'))['max_id']
        while True:
            pk = random.randint(1, max_id)
            context['random_menu'] = Menu.objects.filter(pk=pk).first()
            if context['random_menu']:
                return context

    # random menu pick v.1
    # def get_context_data(self, **kwargs):
    #     context['random_menu'] = Menu.objects.order_by('?').first()
    #     return context

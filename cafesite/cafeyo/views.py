from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

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


class ResultsView(generic.DetailView):
    model = Cafe
    template_name = 'cafeyo/results.html'

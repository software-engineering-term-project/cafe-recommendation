import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Max

from .models import Gate, Cafe, Category, Menu

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'cafeyo/index.html'


class CafelistView(generic.ListView):
    model = Cafe
    template_name = 'cafeyo/cafe_list.html'
    context_object_name = 'cafe_list'

    def get_queryset(self):
        if 'category_id' in self.kwargs:
            return Cafe.objects.filter(문=self.kwargs['gate_id'], 카테고리=self.kwargs['category_id'])
        else:
            return Cafe.objects.filter(문=self.kwargs['gate_id'])

    def get_context_data(self, **kwargs):
        context = super(CafelistView, self).get_context_data(**kwargs)
        max_id = Cafe.objects.all().aggregate(max_id=Max('id'))['max_id']
        if 'category_id' in self.kwargs:
            if Cafe.objects.filter(문=self.kwargs['gate_id'], 카테고리=self.kwargs['category_id']).exists():
                while True:
                    rand = random.randint(1, max_id)
                    context['random_cafe'] = Cafe.objects.filter(
                        문=self.kwargs['gate_id'], 카테고리=self.kwargs['category_id'], pk=rand).first()
                    if context['random_cafe']:
                        break
        else:
            if Cafe.objects.filter(문=self.kwargs['gate_id']).exists():
                while True:
                    rand = random.randint(1, max_id)
                    context['random_cafe'] = Cafe.objects.filter(
                        문=self.kwargs['gate_id'], pk=rand).first()
                    if context['random_cafe']:
                        break
        context['id_param'] = self.kwargs['gate_id']
        return context


class ResultsView(generic.DetailView):
    model = Cafe
    template_name = 'cafeyo/results.html'

    def get_context_data(self, **kwargs):
        if Menu.objects.filter(카페=self.kwargs['pk'], 카페인=True).exists():
            context = super(ResultsView, self).get_context_data(**kwargs)
            max_id = Menu.objects.all().aggregate(max_id=Max('id'))['max_id']
            while True:
                rand = random.randint(1, max_id)
                context['cafein_menu'] = Menu.objects.filter(
                    카페=self.kwargs['pk'], 카페인=True, pk=rand).first()
                if context['cafein_menu']:
                    break

        if Menu.objects.filter(카페=self.kwargs['pk'], 카페인=False).exists():
            while True:
                rand = random.randint(1, max_id)
                context['decafein_menu'] = Menu.objects.filter(
                    카페=self.kwargs['pk'], 카페인=False, pk=rand).first()
                if context['decafein_menu']:
                    break

        return context

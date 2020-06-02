from django.urls import include, path

from . import views

app_name = 'cafeyo'
urlpatterns = [
    # ex: /cafeyo/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /cafeyo/list/1/
    path('list/<int:gate_id>/', views.CafelistView.as_view(), name='cafelist'),
    # ex: /cafeyo//list/1/category/3/
    path('list/<int:gate_id>/category/<category_id>/',
         views.CafelistView.as_view(), name='cafelist_category'),
    # ex: /cafeyo/results/1/
    path('results/<int:pk>/', views.ResultsView.as_view(), name='results')
]

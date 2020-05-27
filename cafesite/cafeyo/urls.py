from django.urls import include, path

from . import views

app_name = 'cafeyo'
urlpatterns = [
    # ex: /cafeyo/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /cafeyo/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /cafeyo/1/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results')
]

from django.urls import include, path

from . import views

app_name = 'cafeyo'
urlpatterns = [
    # ex: /cafeyo/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /cafeyo/북문/
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]

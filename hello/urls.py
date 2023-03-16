from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),  # localhost:8000 => вызывает функцию индекс из вьюшки приложения
    path("about", views.about, name="about")  # localhost:8000/about => вызывает функцию about из вьюшки приложения
]

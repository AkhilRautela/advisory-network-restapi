

from django.urls import path
from admin import views

urlpatterns = [
    path('/advisor', views.add_advisor),
    path('/truncate', views.truncate_tables)
]

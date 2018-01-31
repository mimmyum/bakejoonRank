from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.monthly_table, name='monthly_table'),
]
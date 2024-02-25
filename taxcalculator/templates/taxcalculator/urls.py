from django.urls import path
from . import views

urlspatterns = [
    path('taxcalculator', views.default_view,name='default'),
    path('<int:any_number>/', views.any_number_view, name='any_number'),
    path('taxrate/',views.tax_rate_view, name='tax_rate'),
]
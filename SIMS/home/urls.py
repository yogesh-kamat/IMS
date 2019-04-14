from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('inventory/',views.inventory,name='inventory'),
    path('checkout/',views.checkout,name='checkout'),
    path('transaction/',views.transaction,name='transaction'),
    path('report/',views.report,name='report'),
    path('chart/',views.chart,name='chart'),
]
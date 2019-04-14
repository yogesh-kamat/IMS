from django.urls import path
from users import views

urlpatterns = [
    path('login/',views.index,name='login'),
    path('logout/', views.logout_user, name = "logout"),
]
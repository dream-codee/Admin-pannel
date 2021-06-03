from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('pic/', views.profile_pic, name="pic"),
    path('profile/', views.profile, name="profile"),
]

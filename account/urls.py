from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   path('signin',views.customer_signup_view,name='customer_signup_view'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),
]
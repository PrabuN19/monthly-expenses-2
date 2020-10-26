from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('signup',views.customer_signup_view,name='customer_signup_view'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),
   path('password_reset',auth_views.PasswordResetView.as_view(template_name='forget.html'), name='password_reset'),
   path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='resetdone.html'),name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
   path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
   path('edit_profile',views.edit_profile,name='edit_profile'),
   path('change_password',views.changepassword,name='change_password'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mylist',views.my,name='mylist'),
    path('add',views.projectcreateview.as_view(),name='add'),
    path('<slug:months_slug>',views.detail, name='detail'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('month_del/<int:id>',views.month_del,name='month_del'),

]
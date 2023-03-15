from. import views
from django.urls import path

urlpatterns = [

    path('',views.fun1,name='fun1'),
    path('about/',views.fun2,name='fun2'),
    path('contact/',views.fun3,name='fun3'),
    path('details/',views.fun4,name='fun4'),
    path('thanx/',views.fun5,name='fun5')
]
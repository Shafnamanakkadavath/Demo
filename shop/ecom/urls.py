
from django.urls import path,include
from .import views
app_name='ecom'

urlpatterns = [

    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='all_product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='pro_cat_detail')

]
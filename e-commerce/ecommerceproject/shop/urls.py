from . import views
from django.urls import path


app_name='shop'
urlpatterns = [
   # path('',views.index,name='index')
   path('',views.allprodCat,name='allprodCat'),
   path('<slug:c_slug>/',views.allprodCat,name='products_by_category'),
   path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]


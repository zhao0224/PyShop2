from django.urls import path
from . import views, admin

# /products
# /products/1/detail
# /products/new

urlpatterns = [
    path('', views.index),
    path('new', views.new),

]

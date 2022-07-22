from django.urls import path

from .views.home import home_view
from .views.new_product import new_product_view

app_name = 'store'
urlpatterns = [
    path('', home_view, name="home"),
    path('new_product', new_product_view, name="new_product"),
]
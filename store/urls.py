from django.urls import path

from .views import sign_in_options, custom_product
from .views.home import home_view
from .views.new_product import new_product_view

app_name = 'store'
urlpatterns = [
    path('', home_view, name="home"),
    path('new_product', new_product_view, name="new_product"),
    path('sign_in_options', sign_in_options.SignInOptionsView.as_view(), name="sign_in_options"),
    path('Request/', custom_product.RequestProductView, name="custom product"),
]

from django.urls import path

from .views import custom_product, UpdatesView, CheckoutView
from .views.home import home_view, third_party
from .views.new_product import new_product_view, AddCategory


app_name = 'store'
urlpatterns = [
    path('', home_view, name="home"),
    path('New/', new_product_view, name="upload_product"),
    path('Request/', custom_product.RequestProductView, name="custom product"),
    path('Updates/', UpdatesView.updates_view, name='Updates'),
    path('Checkout/', CheckoutView.CheckoutView.as_view(), name='Checkout'),
    path('New-Category', AddCategory.as_view(), name="new category"),
    #path('accounts/google/login/', third_party, name="third party"),

]

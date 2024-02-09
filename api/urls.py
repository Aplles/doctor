from django.urls import path

from api.views.order import OrderCreateView
from api.views.product import ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),

    path("orders/", OrderCreateView.as_view(), name="orders"),
]


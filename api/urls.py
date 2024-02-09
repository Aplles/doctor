from django.urls import path

from api.views.product import ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products")
]


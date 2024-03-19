from django.urls import path

from api.views.category import CategoryListView
from api.views.country import CountryListView
from api.views.nurse import NurseCreateView, NursePromoCodePresenceView
from api.views.order import OrderCreateView
from api.views.product import ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),

    path("orders/", OrderCreateView.as_view(), name="orders"),

    path("nurses/", NurseCreateView.as_view(), name="nurses"),
    path(
        "nurses/promo_code/<str:promo_code>/presence/",
        NursePromoCodePresenceView.as_view(),
        name="promo_code_presence"
    ),
    path("categories/", CategoryListView.as_view(), name="categories"),

    path('countries/', CountryListView.as_view(), name="countries")
]


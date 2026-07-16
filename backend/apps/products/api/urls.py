from django.urls import path

from apps.products.api.views.product_list import ProductListView
from apps.products.api.views.product_detail import ProductDetailView

urlpatterns = [
    path(
        "",
        ProductListView.as_view(),
        name="product-list",
    ),
    path(
        "<slug:slug>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
]
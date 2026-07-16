from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from rest_framework.generics import ListAPIView

from apps.products.filters import ProductFilter
from apps.products.pagination import (
    ProductPagination,
)

from apps.products.services.product_service import (
    ProductService,
)

from apps.products.api.serializers.product_list import (
    ProductListSerializer,
)


class ProductListView(ListAPIView):

    serializer_class = ProductListSerializer

    pagination_class = ProductPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = ProductFilter

    search_fields = [
        "name",
        "description",
        "brand",
        "sku",
    ]

    ordering_fields = [
        "price",
        "rating",
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]

    def get_queryset(self):

        return ProductService.list_products()
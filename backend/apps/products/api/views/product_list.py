from rest_framework.generics import ListAPIView

from apps.products.api.serializers.product_list import (
    ProductListSerializer,
)

from apps.products.services.product_service import (
    ProductService,
)


class ProductListView(ListAPIView):

    serializer_class = ProductListSerializer

    permission_classes = []

    def get_queryset(self):

        return ProductService.list()
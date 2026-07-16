from rest_framework.generics import RetrieveAPIView

from apps.products.api.serializers.product_detail import (
    ProductDetailSerializer,
)

from apps.products.services.product_service import (
    ProductService,
)


class ProductDetailView(RetrieveAPIView):

    serializer_class = ProductDetailSerializer

    permission_classes = []

    lookup_field = "slug"

    def get_object(self):

        return ProductService.detail(
            self.kwargs["slug"]
        )
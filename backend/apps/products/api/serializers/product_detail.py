from rest_framework import serializers

from apps.products.models import Product, ProductImage

from .category import CategorySerializer


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductImage

        fields = (
            "id",
            "image",
            "alt_text",
            "is_primary",
        )


class ProductDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    images = ProductImageSerializer(
        many=True,
        read_only=True,
    )

    final_price = serializers.ReadOnlyField()

    discount_percentage = serializers.ReadOnlyField()

    is_in_stock = serializers.ReadOnlyField()

    class Meta:

        model = Product

        fields = (
            "__all__"
        )
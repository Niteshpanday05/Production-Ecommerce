from rest_framework import serializers

from apps.products.models import Product

from .category import CategorySerializer


class ProductListSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    final_price = serializers.ReadOnlyField()

    discount_percentage = serializers.ReadOnlyField()

    is_in_stock = serializers.ReadOnlyField()

    class Meta:

        model = Product

        fields = (
            "id",
            "name",
            "slug",
            "thumbnail",
            "price",
            "discount_price",
            "final_price",
            "discount_percentage",
            "rating",
            "total_reviews",
            "stock",
            "is_in_stock",
            "brand",
            "category",
        )
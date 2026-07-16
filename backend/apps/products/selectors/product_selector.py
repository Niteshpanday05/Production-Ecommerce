from apps.products.models import Product
from django.db.models import Prefetch


from apps.products.models import (
    Product,
    ProductImage,
)


class ProductSelector:

    @staticmethod
    def product_list():

        return (
            Product.objects
            .select_related("category")
            .prefetch_related("images")
            .filter(is_active=True)
        )

    @staticmethod
    def product_detail(slug):

        return (
            Product.objects
            .select_related("category")
            .prefetch_related("images")
            .get(
                slug=slug,
                is_active=True,
            )
        )
        
        

    @staticmethod
    def get_products():

        return (
            Product.objects
            .select_related("category")
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ProductImage.objects.order_by(
                        "-is_primary"
                    ),
                )
            )
            .filter(
                is_active=True,
            )
        )

    @staticmethod
    def get_product(slug):

        return (
            ProductSelector
            .get_products()
            .get(slug=slug)
        )
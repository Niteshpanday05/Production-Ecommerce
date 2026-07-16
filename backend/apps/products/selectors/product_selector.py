from apps.products.models import Product


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
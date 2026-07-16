from apps.products.selectors.product_selector import (
    ProductSelector,
)


class ProductService:

    @staticmethod
    def list():

        return ProductSelector.product_list()

    @staticmethod
    def detail(slug):

        return ProductSelector.product_detail(slug)
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
    
    
    @staticmethod
    def list_products():

        return ProductSelector.get_products()

    @staticmethod
    def get_product(slug):

        return ProductSelector.get_product(slug)

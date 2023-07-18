from rest_framework import serializers
from APIApp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    #
    # def create(self, validated_data):
    #     product = validated_data.pop('product')
    #     product_id = product.id if isinstance(product, Product) else product
    #     product = Product.objects.get(id=product_id)
    #     new_product = Product.objects.create(product=product, **validated_data)
    #
    #     return new_product


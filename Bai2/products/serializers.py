from rest_framework import serializers 
from products.models import product
 
 
class productSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = product
        fields = ('id',
                  'title',
                  'description',
                  'category',
                  'price')

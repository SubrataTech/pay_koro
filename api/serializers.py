from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from api.models import *


class UserSerializer(ModelSerializer):
    """ Django default user level model serializer """
    business_type = serializers.CharField(max_length=100)
    customer_name = serializers.CharField(max_length=100)
    customer_mobile = serializers.CharField(max_length=13)
    customer_email = serializers.EmailField(max_length=250)
    own_business = serializers.CharField(max_length=3)
    customer_password = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('id', 'business_type', 'customer_name', 'customer_mobile',
                  'customer_email', 'own_business', 'customer_password', 'username')

        depth = 10

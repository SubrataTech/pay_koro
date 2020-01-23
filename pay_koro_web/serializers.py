from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['business_type', 'customer_name', 'customer_mobile', 'customer_email',
                  'own_business', 'customer_password', 'is_registration_active']
        # fields = '__all__'

        def create(self, validate_data):
            registration = Registration(
                business_type=validate_data['business_type'],
                customer_name=validate_data['customer_name'],
                customer_mobile=validate_data['customer_mobile'],
                customer_email=validate_data['customer_email'],
                own_business=validate_data['own_business'],
                customer_password=validate_data['customer_password'],
                is_registration_active=validate_data['is_registration_active'],
            )
            registration.save()
            return registration

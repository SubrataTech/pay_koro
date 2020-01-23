from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from api.serializers import UserSerializer
from rest_framework.response import Response
from api.utils import response_messages
from django.contrib.auth.models import User


@permission_classes((AllowAny,))
class Register(viewsets.ModelViewSet):
    """ Registration of new user """

    lookup_field = 'id'
    serializer_class = UserSerializer
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        customer_name = request.data.get("customer_name")
        customer_mobile = request.data.get('customer_mobile')
        business_type = request.data.get('business_type')
        customer_email = request.data.get('customer_email')
        own_business = request.data.get('own_business')
        customer_password = request.data.get('customer_password')
        print(business_type)
        if not all((customer_name, customer_mobile, business_type, customer_email, own_business, customer_password)):
            return Response({'message': response_messages['EN0007'], 'success': False, 'status_code': 'EN0007'},
                            status=status.HTTP_400_BAD_REQUEST)

        if own_business.upper() == 'YES' or own_business.upper() == 'NO':
            print('OK')
            pass

        else:
            return Response({'message': response_messages['EN0011'], 'success': False, 'status_code': 'EN0011'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(customer_name=customer_name, customer_mobile=customer_mobile,
                                   business_type=business_type, customer_email=customer_email,
                                   own_business=own_business)
        user.username = customer_name.lower() + str(user.id)
        user.set_password(customer_password)
        user.is_active = False
        user.save()

        return Response({'message': response_messages['EN0001'], 'success': False, 'status_code': 'EN0001'},
                        status=status.HTTP_201_CREATED)


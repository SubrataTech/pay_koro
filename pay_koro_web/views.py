from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .serializers import RegistrationSerializer

# Status Code
'''
Success : 200 OK

Bad Request : 400
Unauthorized : 401
Forbidden : 403
Not Found : 404
Method Not Allowed : 405

Internal Server Error : 500
Bad Gateway : 502
Gateway Timeout : 504

'''


class Registration_api(APIView):

    def post(self, request):
        business_type = ''
        customer_name = ''
        mobile_number = ''
        email_id = ''
        is_your_business = ''
        password = ''
        confirm_password = ''

        return Response('serializer.data', status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
def index(request):
    return HttpResponse("Hello Subrata")

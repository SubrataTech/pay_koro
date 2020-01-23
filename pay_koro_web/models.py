from django.db import models


# Create your models here.
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    business_type = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_mobile = models.BigIntegerField(10)
    customer_email = models.EmailField(max_length=250)
    own_business = models.CharField(max_length=10)
    customer_password = models.CharField(max_length=150)
    is_registration_active = models.CharField(max_length=5)
    customer_created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_email


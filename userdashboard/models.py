from django.db import models
from django.contrib.auth import get_user_model
import uuid
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    profile_image = models.ImageField(upload_to='profile_images', default='r.jpg')
    first_name  = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    referral_price  = models.IntegerField(default=0)
    referral_people  = models.IntegerField(default=0)
    referred_by  = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.user.username 
    
class Verification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    day_of_birth  = models.IntegerField(default=0)
    month_of_birth = models.CharField(max_length=50,null=True,blank=True)
    year_of_birth = models.CharField(max_length=50,null=True,blank=True)
    document_uploaded = models.CharField(max_length=50,null=True,blank=True)
    serial_number  = models.IntegerField(default=0)
    year_issued = models.IntegerField(default=0)
    verify_document = models.FileField(upload_to='verify_document',default='r.jpg')
    
    def __str__(self):
        return self.user.username 
    
class Referral(models.Model):
    profile = models.ForeignKey(Profile,related_name="referrals", on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    
    def __str__(self):
        return self.profile.user.username 
    
    
    
from djongo import models

# Create your models here.
class user_profile(models.Model):
    username = models.CharField(max_length=50, null=False)

  

class user_detail(models.Model):
    phone_no = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=200, blank=True)
    u_id = models.IntegerField()
    # user= models.ForeignKey('user', on_delete=models.CASCADE,blank=True)
    
    
    
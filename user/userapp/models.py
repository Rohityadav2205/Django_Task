from django.db import models

# Create your models here.
class userModel(models.Model):
    user_name =models.CharField(max_length=100)
    user_email=models.EmailField()
    mobile_number=models.CharField(max_length=10)

    def __str__(self):
        return "user_name={0},user_email={1},mobile_number={2}".format(self.user_name,self.user_email,
                                                                       self.mobile_number)

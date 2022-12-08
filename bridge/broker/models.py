from django.db import models
from django.contrib.auth.models import User

class Balance(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=30, default='$0.00')
    plan = models.CharField(
        max_length=50,
        choices=[('None', 'None'), ('Basic', 'Basic'), ('+Advanced', '+Advanced'), ('+Premuim', '+Premuim'), ('+Ultimate', '+Ultimate'), 
        ('+Spartan', '+Spartan'),], default = 'Make a deposit to get started')

    def __str__(self):
        return str(self.user)
    


from django.db import models

# Create your models here.
class Countries(models.Model):
    CId=models.CharField(max_length=100,primary_key=True)
    CName=models.CharField(max_length=10,unique=True)
    RegionId=models.IntegerField(null=True)

    def __str__(self):
        return self.CId

class City(models.Model):
    CityNname=models.CharField(max_length=100)
    PINCode=models.IntegerField(null=True)
    CId=models.ForeignKey(Countries,on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.CityNname
from django.db import models
from asosiy.models import Mahsulot
from userapp.models import Account


class Tanlanganlar(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Savat(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    umumiy_summa = models.PositiveSmallIntegerField()
    holat = models.CharField(max_length=30)

class SavatItem(models.Model):
    savat = models.ForeignKey(Savat,on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)

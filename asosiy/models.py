from django.db import models
from userapp.models import Account

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.IntegerField()
    min_miqdor = models.PositiveSmallIntegerField(default=1)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    davlat = models.CharField(max_length=100)
    brend = models.CharField(max_length=30)
    kafolat= models.CharField(max_length=30)
    matn= models.TextField()
    yetkazish = models.CharField(max_length=30)
    mavjud= models.BooleanField(default=True)
    chegirma= models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulotlar')
    mahsulot= models.ForeignKey(Mahsulot,on_delete=models.CASCADE)

class Izoh(models.Model):
    matn = models.TextField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    sana = models.DateField()
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField()

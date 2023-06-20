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

    def save(self, *args ,**kwargs):
        savat_items = SavatItem.objects.filter(savat__id=self.id)
        summa = 0
        for item in savat_items:
            ch = (item.mahsulot.narx/100)*item.mahsulot.chegirma
            narxi = item.mahsulot.narx - int(ch)
            narxi = narxi * item.miqdor
            summa += narxi
        self.umumiy_summa= summa
        super(Savat , self).save(*args, **kwargs)
class SavatItem(models.Model):
    savat = models.ForeignKey(Savat,on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    summa = models.PositiveBigIntegerField()

    # def save(self , *args , **kwargs):
    #     ch = (self.mahsulot.narx / 100) * self.mahsulot.chegirma
    #     narxi = self.mahsulot.narx - int(ch)
    #     self.summa = narxi * self.miqdor
    #     savat = Savat.objects.get(id= self.savat.id)
    #     savat.save()
    #     super(SavatItem, self).save(*args, **kwargs)
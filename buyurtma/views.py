from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from asosiy.models import Mahsulot
from userapp.models import Account


class ShoppingCard(View):
    def get(self , request):
        savati = Savat.objects.get(account__user=request.user)
        itemlar = SavatItem.objects.filter(savat = savati)
        narx_sum = 0
        ch = 0
        for item in itemlar:
            ch +=((item.mahsulot.narx/100)*item.mahsulot.chegirma)*item.miqdor
            narx_sum += item.mahsulot.narx* item.miqdor
        savati.umumiy_summa = narx_sum-ch
        savati.save()
        content = {
            "savat" : savati,
            "itemlar" : SavatItem.objects.filter(savat = savati),
            'total' : narx_sum,
            'discount': ch,
            'price': narx_sum-ch

        }
        return render(request, 'page-shopping-cart.html',content)

class Miqdor_kamaytir(View):
    def get(self , request, pk):
        item =SavatItem.objects.get(id= pk)
        if item.miqdor > 1:
            item.miqdor -= 1
            item.summa -= item.mahsulot.narx
            item.save()
        return redirect("/buyurtma/savat/")

class Miqdor_qosh(View):
    def get(self , request, pk):
        item =SavatItem.objects.get(id=pk)
        item.miqdor += 1
        item.summa += item.mahsulot.narx
        item.save()
        return redirect("/buyurtma/savat/")

class Savat_qosh(View):
    def get(self, request, pk):
        savati = Savat.objects.get(account__user = request.user)
        m = Mahsulot.objects.get(id=pk)
        savat_item = SavatItem.objects.filter(mahsulot= m, savat = savati)
        if len(savat_item) > 1:
            return redirect(f"/asosiy/mahsulot/{pk}/")
        SavatItem.objects.create(
            miqdor = 1,
            mahsulot = m,
            savat = savati ,
             summa = m.narx
        )
        return redirect(f"/asosiy/mahsulot/{pk}/")

class ProfilOrders(View):
    def get(self , request):
        return render(request, 'page-profile-orders.html')

class ProfilWishlist(View):
    def get(self, request):
        content = {
            "tanlanganlar": Tanlanganlar.objects.filter(account__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', content)


class TanlanganQosh(View):
    def get(self , request , son):
        Tanlanganlar.objects.create(
            mahsulot = Mahsulot.objects.get(id=son),
            account = Account.objects.get(user=request.user)
        )
        return redirect("/buyurtma/wishlist/")
class WishOchir(View):
    def get(self, request ,son):
        Tanlanganlar.objects.get(id=son, account__user = request.user).delete()
        return redirect("/buyurtma/wishlist/")

class SavatItemOchir(View):
    def get(self, request,son):
        SavatItem.objects.get(id=son, savat__account__user = request.user).delete()
        return redirect("/buyurtma/savat/")

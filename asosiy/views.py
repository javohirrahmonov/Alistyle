from django.db.models import Sum, Avg
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Account


class Home(View):
    def get(self,request):
        content = {
            'bolimlar': Bolim.objects.all()[0:8]
        }
        return render(request,'page-index.html',content)

class HomeLoginsiz(View):
    def get(self,request):
        return render(request,'page-index-2.html')

class MasulotlarView(View):
    def get(self,request,pk):
        content = {
            "mahsulotlar": Mahsulot.objects.filter(bolim__id=pk)
        }
        return render(request,'page-listing-grid.html',content)

class HammaBolimView(View):
    def get(self,request):
        content = {
            "bolimlar" : Bolim.objects.all()
        }
        return render(request, 'page-category.html', content)

class BittaMahsulotView(View):
    def get(self,request,son):
        izohlar = Izoh.objects.filter(mahsulot__id = son)
        ortachasi= izohlar.aggregate(Avg('baho')).get('baho__avg')
        if ortachasi is None:
            ortachasi = 0
        content = {
            "mahsulot" :Mahsulot.objects.get(id=son),
            "izohlar" : izohlar,
            'izoh_soni' :len(izohlar),
            "ortachasi" : int(ortachasi*20)
        }
        return render(request,'page-detail-product.html',content)

    def post(self,request,son):
        Izoh.objects.create(
            matn = request.POST.get('comment'),
            baho = request.POST.get('rating'),
            mahsulot = Mahsulot.objects.get(id=son),
            account = Account.objects.get(user=request.user)
        )
        return redirect(f"/asosiy/mahsulot/{son}/")
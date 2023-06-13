from django.shortcuts import render
from django.views import View
from .models import *

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
        content = {
            "mahsulot" :Mahsulot.objects.get(id=son)
        }
        return render(request,'page-detail-product.html',content)
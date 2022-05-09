from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import *

class Catalog(View):
    def get(self, request):
        bolim = Bolim.objects.all()
        return render(request, 'Catalog.html', {'bolimlar' : bolim})

class Mahsulotlar(View):
    def get(self, request, pk):
        b = Bolim.objects.get(id = pk)
        m = Product.objects.filter(bolim = b)
        return render(request, 'milkandegg.html', {'bolim' : b, 'mahsulotlar' : m})

class Mahsulot(View):
    def get(self, request, pk):
        m = Product.objects.get(id = pk)
        c = Comment.objects.filter(mahsulot = m)
        b = Bolim.objects.get(id = m.bolim.id)
        mah = Product.objects.filter(bolim = b).exclude(id = m.id)[:5]
        return render(request, 'butter.html', {'mahsulot' : m, 'mahsulotlar' : mah, 'sharhlar' : c})
    def post(self, request, pk):
        m = Product.objects.get(id = pk)
        mijoz = Mijoz.objects.get(id = 1)
        Comment.objects.create(
            mahsulot = m,
            matn = request.POST.get('sharh'),
            baho = int(request.POST.get('demo')),
            mijoz = mijoz
        )
        return redirect('mahsulot', pk = m.id)
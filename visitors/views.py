from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'visitors/index.html')


def buycrypto(request):
    return render(request, 'visitors/buycrypto.html')

def cryptoloan(request):
    return render(request, 'visitors/cryptoloan.html')

def debitcard(request):
    return render(request, 'visitors/debitcard.html')

def earn(request):
    return render(request, 'visitors/earn.html')
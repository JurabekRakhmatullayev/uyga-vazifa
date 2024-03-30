from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home
def main(request):
    return HttpResponse("Assalomu aleykum")
# hello
def main(request):
    return HttpResponse("Salom dunyo")
# help
def main(request):
    return HttpResponse("Bu sayt sifat uquvchilari tomonidan yaratilgan")
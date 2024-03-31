from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home
def main(request,name):
    return HttpResponse(f"Assalomu aleykum {name}")
# # hello
# def main(request):
#     return HttpResponse("Salom dunyo")
# # help
# def main(request):
#     return HttpResponse("Bu sayt sifat uquvchilari tomonidan yaratilgan")
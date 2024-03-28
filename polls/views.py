from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def menu(request):
    return HttpResponse("커피메뉴")

def order_coffee(request):
    return HttpResponse("커피 한 잔 주세요.")
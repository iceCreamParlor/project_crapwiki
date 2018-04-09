from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'mypage/index.html')
def search(request):
    return render(request, 'mypage/index2.html')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'mypage/index.html')
def search(request):
    searchWord = request.POST['search']
    context = {'searchWord': searchWord}
    return render(request, 'mypage/searchWord.html', context)

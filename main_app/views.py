from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
# import requests
# Create your views here.


# # Define the test view
# def test(request):
#     context={
#         'test': 'This is a test!'
#     }
#     return render(request, 'gallery/index.html', context)


# Testing with fake API via URL
# def test(request):
#     response=HttpRequest.GET('https://jsonplaceholder.typicode.com/posts')
#     post=response.json()
#     return render(HttpRequest, 'gallery/index.html', {'post': post})

def test(request):
    return HttpResponse('This is a test')

# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
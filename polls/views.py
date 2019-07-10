from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("こんにちは、World。あなたは投票インデックスにいます。これはindexビューで定義した ものです。")

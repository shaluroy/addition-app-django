from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	
	return render(request,"addition/index.html")


def addlogic(request):
	a = request.GET["txtnum1"]
	b = request.GET["txtnum2"]
	c = int(a)+int(b)
	return render(request,"addition/index.html",{'key':c})
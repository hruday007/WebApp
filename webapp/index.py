from django.http import HttpResponse
from django.shortcuts import render

def webpage(request):
	return render(request,'homepage.html')


def webpage1(request):
	return render(request,'end.html')
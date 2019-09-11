from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def index(req:HttpResponse):
    return HttpResponse(open("./appone/index.html"))

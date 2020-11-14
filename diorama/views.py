from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt


def welcome(request):
    return HttpResponse('Welcome to Gee Diorama')


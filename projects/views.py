from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Here are all of our projects')

def project(request, pk):
    return HttpResponse('Single project page for' + ' ' + str(pk))
from django.shortcuts import render, HttpResponse

def display(request):
    return HttpResponse('placeholder to display all the surveys created')


def new(request):
    return HttpResponse('placehloder for users to add a new survey')
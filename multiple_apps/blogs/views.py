from django.shortcuts import render, HttpResponse, redirect

def display(request):
    return HttpResponse('Placehodler to later display all the list of blogs')


def new(request):
    return HttpResponse('placeholder to diplay a new form to creat a new blog')


def create(request):
    return redirect('/blogs')

def specific(request, blog_number):
    return HttpResponse('placeholder to display blog {}'.format(blog_number))


def edit(request, blog_number):
    return HttpResponse('placeholder to edit blog {}'.format(blog_number))


def delete(request):
    return redirect('/blogs')
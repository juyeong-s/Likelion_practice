from django.shortcuts import render, redirect

def main(request):
    return render(request, 'web/main.html')

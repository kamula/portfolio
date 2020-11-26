from django.shortcuts import render

def list_jobs(request):
    return render(request,'jobs/home.html')

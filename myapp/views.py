from django.shortcuts import render

# Create your views here.
name="SABA"
email="saba@gmail.com"
phno=9449675023
def index(request):
    return render(request,"home.html",{'name':name})

def profile_pic(request):
    return render(request,"profile_pic.html",{'name':name})

def profile(request):
    return render(request,"profile.html",{"name":name,"email":email,"phno":phno})
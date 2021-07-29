from django.shortcuts import render
from .models import details 
from . forms import  add_details

# Create your views here.
def accept(request):
    if request.method=="POST":
        acc = add_details(request.POST)
        if acc.is_valid():
            Fname =acc.cleaned_data['Fname']
            Lname = acc.cleaned_data['Lname']
            Email =acc.cleaned_data['Email']
            Number =acc.cleaned_data['Number']
            Dname =acc.cleaned_data['Dname']
            Branch = acc.cleaned_data['Branch']
            Dscore = acc.cleaned_data['Dscore']
            Styear = acc.cleaned_data['Styear']
            Dyear = acc.cleaned_data['Dyear']
            Hsc = acc.cleaned_data['Hsc']
            Hscore = acc.cleaned_data['Hscore']
            Hyear =acc.cleaned_data['Hyear']
            Ssc =acc.cleaned_data['Ssc']
            Sscore =acc.cleaned_data['Sscore']
            Syear =acc.cleaned_data['Syear']
            Experience = acc.cleaned_data['Experience']
            Skills = acc.cleaned_data['Skills']
            Awards =acc.cleaned_data['Awards']
            more = details(Fname = Fname , Lname = Lname , Email = Email , Number = Number , Dname = Dname , Branch = Branch , Dscore = Dscore , Styear = Styear , Dyear = Dyear , Hsc = Hsc , Hscore = Hscore , Hyear = Hyear , Ssc =Ssc ,Sscore = Sscore , Syear = Syear , Experience = Experience , Skills = Skills , Awards = Awards )
            more.save()
            acc = add_details()
    else:
        acc = add_details()
    acad = details.objects.all()
    return render(request,'index.html',{'form':acc})

def lost(request):
    return render(request,"list.html")
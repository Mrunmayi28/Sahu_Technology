

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import modelaccept
from django.shortcuts import render




# Create your views here.
def accept (request):
    if request.method =="POST":
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname','')
        specification  = request.POST.get('specification','')
        email = request.POST.get('email','')
        number = request.POST.get('number','')
        link = request.POST.get('link','')
        dname = request.POST.get('dname','')
        branch = request.POST.get('branch','')
        dscore = request.POST.get('dscore','')
        styear = request.POST.get('styear','')
        dyear = request.POST.get('dyear','')
        hsc = request.POST.get('hsc','')
        hscore = request.POST.get('hscore','')
        hyear = request.POST.get('hyear','')
        ssc = request.POST.get('ssc','')
        sscore = request.POST.get('sscore','')
        syear = request.POST.get('syear','')
        experience = request.POST.get('experience','')
        skills = request.POST.get('skills','')
        awards = request.POST.get('awards','')
        
        
        print(fname,lname,email,specification ,number,link,dname,branch,dscore,styear,dyear,hsc,hscore,hyear,ssc,sscore,syear,experience,skills,awards)
        accepting = modelaccept(fname=fname,lname=lname,specification =specification ,email=email,number=number,link=link,dname=dname,branch=branch,dscore=dscore,styear=styear,dyear=dyear,
        hsc=hsc,hscore=hscore,hyear=hyear,ssc=ssc,sscore=sscore,syear=syear,experience=experience,skills=skills,awards=awards)
        accepting.save()
        
        return render(request,"pdf.html" )
    return render(request,"index.html" )



def pdf_print(request):
    user = modelaccept.objects.all().last()
    template_path = 'list.html'
    context = {'user': user}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="resume.pdf"'
   
    template = get_template(template_path)
    html = template.render(context)
    

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    




    
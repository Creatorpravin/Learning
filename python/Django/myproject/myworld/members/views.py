from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse


def index(request):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    # mymembers = Members.objects.all().values()
    # output = ""
    # mem = Members(firstname="Rahul", lastname="Raj") # add value on table
    # mem.save()
    # for x in mymembers:
    #   output += "Firstname:"+ x["firstname"] + " Lastname:" + x["lastname"] + "\t"
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')

    context = {
        'mymembers': mymembers
    }

    # send the object to html template
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    members = Members.objects.get(id=id)
    members.delete()
    return HttpResponse(reverse('index'))
from django.http import HttpResponse
from django.template import loader
from .models import Members

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
    'mymembers' : mymembers
  }
  
  return HttpResponse(template.render(context, request)) # send the object to html template
from django.shortcuts import render
from .models import AnonMessage

# Create your views here.
def home(request):
    
    last_messages = AnonMessage.objects.order_by('-id')[:10]
    
    for message in last_messages:
        
        message.time = message.time.strftime("%b. %d, %Y, %H:%M")

    return render(request, 'home/index.html',{'last_messages':last_messages})
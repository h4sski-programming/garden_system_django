from django.shortcuts import render, redirect


from .models import Zone
# Create your views here.

def index(request):
    
    context = {
        'zones': Zone.objects.all(),
        'temp': 'temp',
    }
    return render(request=request, template_name='index.html', context=context)


def zone_settings(request, id):
    
    context = {
        'zone': Zone.objects.get(pk=id),
        'temp': 'temp'
    }
    return render(request=request, template_name='zone_settings.html', context=context)



def change_zone_state(request, id):
    zone = Zone.objects.get(pk=id)
    print(zone.state)
    if zone.state:
        zone.state = False
    else:
        zone.state = True
    print(zone.state)
    zone.save()
        
    return redirect('/')
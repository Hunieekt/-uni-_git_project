from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import Form
from .models import Squirrels


def index(request):
    squirrels = Squirrels.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'sightings/index.html', context)


def squirrels_details(request, Unique_squirrel_id):
    squirrel = Squirrels.objects.get(id=Unique_squirrel_id)
    return HttpResponse(f"This is {squirrel.Unique_squirrel_id}")


def update(request, squirrel_id):
    Object = get_object_or_404(Squirrels, Unique_squirrel_id=squirrel_id)
    form = Form(request.POST or None, instance=Object)

    if form.is_valid():
        Object = form.save(commit=False)
        Object.save()
        return redirect('/sightings/')
    else:
        context = {
            'form': form,
        }
        return render(request, 'sightings/update_form.html', context)



def create_view(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings/')
    else:
        form = Form()
        context = {'form': form, }
        return render(request, 'sightings/new_squirrel.html', context)


def delete(request, squirrel_id):
    Object = get_object_or_404(Squirrels, Unique_squirrel_id=squirrel_id)
    try:
        Object.delete()
        return redirect(f'/sightings/')
    except:
        return render(request, 'sightings/confirm_delete.html')


def showmap(request):
    sightings = Squirrels.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'sightings/map.html', context)


def stats(request):
    num_of_sightings = Squirrels.objects.all().count()
    juvenile_age = Squirrels.objects.filter(Age='Juvenile').count()
    gray_fur = Squirrels.objects.filter(Primary_Fur_Color='Gray').count()
    ground_plane_location = Squirrels.objects.filter(
        Location='Ground Plane').count()
    running = Squirrels.objects.filter(Running='TRUE').count()
    context = {
        'num_of_sightings': num_of_sightings,
        'juvenile_age': juvenile_age,
        'gray_fur': gray_fur,
        'ground_plane_location': ground_plane_location,
        'running': running,
    }
    return render(request, 'sightings/stats.html', context)
# Create your views here.

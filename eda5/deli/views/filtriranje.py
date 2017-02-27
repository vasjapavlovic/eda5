
from django.core.context_processors import csrf
from django.http import JsonResponse

# Deli
from ..models import Skupina, Podskupina, DelStavbe



# view called with ajax to reload the month drop down list
def filter_skupina_podskupina(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    skupina = request.POST['skupina']
    skupina = Skupina.objects.get(id=skupina)

    # podskupine glede na izbrano skupino
    podskupina_list = []
    for podskupina in skupina.podskupina_set.all():
        podskupina_list.append(podskupina.id)

    # OUTPUT FILTER
    # Podskupine
    context['podskupine_to_display'] = podskupina_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def filter_podskupina_delstavbe(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    podskupina = request.POST['podskupina']
    podskupina = Podskupina.objects.get(id=podskupina)

    # deli stavbe glede na izbrano podskupino
    del_stavbe_list = []
    for del_stavbe in podskupina.delstavbe_set.all():
        del_stavbe_list.append(del_stavbe.id)



    # OUTPUT FILTER

    # DelStavbe
    context['del_stavbe_to_display'] = del_stavbe_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def filter_delstavbe_projektnomesto(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    del_stavbe = request.POST['del_stavbe']
    del_stavbe = DelStavbe.objects.get(id=del_stavbe)


    projektno_mesto_list = []
    for projektnomesto in del_stavbe.projektnomesto_set.all():
        projektno_mesto_list.append(projektnomesto.id)

    # OUTPUT FILTER

    # DelStavbe
    context['element_to_display'] = projektno_mesto_list

    return JsonResponse(context)
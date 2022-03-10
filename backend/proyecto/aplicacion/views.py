
import json
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Geometria

# Create your views here.

class Vista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        listGet=list(Geometria.objects.values())
        #print(listGet)
        thisdict = {
            "type": "FeatureCollection",
        }
        miLista=[]
        for a in listGet:
            miLista.append({
                "type": "Feature",
                "properties":{
                    "color":a["class_color"],
                    "info":a["class_info"]},
                "geometry":{
                    "type":a["class_type"],
                    "coordinates":json.loads(a["class_coordinates"])
                    }
                }
            ),
        thisdict["features"]=miLista
        return JsonResponse(thisdict)

    def post(self,request):
        dictEntrada = json.loads(request.body)
        
        Geometria.objects.create(
            class_info = dictEntrada['properties']['info'], 
            class_color = dictEntrada['properties']['color'], 
            class_coordinates = dictEntrada['geometry']['coordinates'],
            class_type = dictEntrada['geometry']['type'])
        
        respuesta = {
            "mensaje": "Todo bien!"
        }
        return JsonResponse(dictEntrada)


    def delete(self,request):
        Geometria.objects.filter(id=7).delete()
        respuesta = {
            "mensaje": "Se borro :o"
        }
        return JsonResponse(respuesta)

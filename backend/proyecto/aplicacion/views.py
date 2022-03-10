
import json
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .calculation import *

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

        print("ahora haremos que le point del cliente se convierta en un circulo")

        ##############################
        # agregar radio de destrcucion
        ##############################
        circulo = genera_circulo_2(
            dictEntrada['geometry']['coordinates'][0],
            dictEntrada['geometry']['coordinates'][1],
            int(dictEntrada['properties']['radio']))

        Geometria.objects.create(
            class_info = 'generado por punto del cliente', 
            class_color = 'green', 
            class_coordinates = circulo,
            class_type = 'Polygon'
            )
        ##############################
        # agregar radio de radiacion
        ##############################
        circulo = genera_circulo_2(
            dictEntrada['geometry']['coordinates'][0],
            dictEntrada['geometry']['coordinates'][1],
            2)

        Geometria.objects.create(
            class_info = 'generado por punto del cliente', 
            class_color = 'red', 
            class_coordinates = circulo,
            class_type = 'Polygon'
            )

        ##############################
        # agregar punto ingresado por usuario
        ##############################
        Geometria.objects.create(
            class_info = dictEntrada['properties']['info'], 
            class_color = dictEntrada['properties']['color'], 
            class_coordinates = dictEntrada['geometry']['coordinates'],
            class_type = dictEntrada['geometry']['type']
            )
        
        respuesta = {
	        "type": "Feature",
	            "properties": {
		        "mensaje": "Tudu ven! "
	        }
        }   

        return JsonResponse(respuesta)


    def delete(self,request):
        Geometria.objects.filter(id=7).delete()
        respuesta = {
            "mensaje": "Se borro :o"
        }
        return JsonResponse(respuesta)

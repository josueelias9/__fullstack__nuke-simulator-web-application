
from ctypes.wintypes import HPALETTE
import json
from urllib import request, response
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
                    "info":a["class_info"],
                    "strokeWeight":a["class_strokeWeight"]},
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
        
        ##############################
        # tipo de bomba
        ##############################
        r_destruccion = 0
        r_radiacion = 0
        a = "big bomb" # dictEntrada['properties']['bomba']
        if(a == "big bomb"):
            r_destruccion = 2
            r_radiacion = 8
        elif (a =="medium bomb"):
            r_destruccion = 10
            r_radiacion = 20
        
        ##############################
        # agregar radio de destrcucion
        ##############################
        circulo = genera_circulo_2(
            float(dictEntrada["latitud"]),
            float(dictEntrada["longitud"]),
            r_destruccion)

        Geometria.objects.create(
            class_info = 'generado por punto del cliente', 
            class_color = 'red', 
            class_coordinates = circulo,
            class_type = 'Polygon'
            )
        ##############################
        # agregar radio de radiacion
        ##############################
        circulo = genera_circulo_2(
            float(dictEntrada["latitud"]),
            float(dictEntrada["longitud"]),
            r_radiacion)

        Geometria.objects.create(
            class_info = 'generado por punto del cliente', 
            class_color = 'yellow', 
            class_coordinates = circulo,
            class_type = 'Polygon'
            )

        ##############################
        # agregar punto ingresado por usuario
        ##############################
        Geometria.objects.create(
            class_info = "si info",# dictEntrada['properties']['info'], 
            class_color = "blue", # dictEntrada['properties']['color'], 
            class_coordinates = [ float(dictEntrada["longitud"]), float(dictEntrada["latitud"]) ],
            #dictEntrada['geometry']['coordinates'],
            class_type = "Point"#dictEntrada['geometry']['type']
        )

        ##############################
        # respuesta al cliente
        ##############################
        respuesta = {
	        "type": "Feature",
            "properties": {
		        "mensaje": "Tudu ven! "
	        }
        }   
        print(type(JsonResponse(dictEntrada)))
        return JsonResponse(dictEntrada)

    def delete(self,request):
        Geometria.objects.filter(id=7).delete()
        respuesta = {
	        "type": "Feature",
            "properties": {
		        "mensaje": "se borro! "
	        }
        }   
        return JsonResponse(respuesta)

    def put(self,request, *args, **kwargs):
        muer = 0
        hola=json.loads(request.body)
        #print(hola)
        if(len(Geometria.objects.filter(id="1")) == 0): # punto
            Geometria.objects.create(
                id=1, 
                class_type="Point",   
                class_coordinates=[-77.0282400,-12.0431800])
        elif(len(Geometria.objects.filter(id="2")) == 0): # destruccion
            Geometria.objects.create(
                id=2, 
                class_type="Polygon", 
                class_color="red", 
                class_coordinates=[[ [-77.0282400,-12.0431800], [-87.0282400,-12.0431800], [-87.0282400,-22.0431800], [-77.0282400,-12.0431800] ]],
                class_strokeWeight =1 )
        elif(len(Geometria.objects.filter(id="3")) == 0): # radiacion
            Geometria.objects.create(
                id=3, 
                class_type="Polygon", 
                class_color="yellow",
                class_coordinates=[[ [-77.0282400,-12.0431800], [-87.0282400,-12.0431800], [-87.0282400,-22.0431800], [-77.0282400,-12.0431800] ]],
                class_strokeWeight = 1)
        elif(len(Geometria.objects.filter(id="4")) == 0): # interseccion
            Geometria.objects.create(
                id=4, 
                class_type="Polygon", 
                class_color="green",
                class_coordinates=[[ [-77.0282400,-12.0431800], [-87.0282400,-12.0431800], [-87.0282400,-22.0431800], [-77.0282400,-12.0431800] ]],
                class_strokeWeight = 4)
        else:
            if(hola["properties"]["bomba"] == "termo"):
                radio_radiacion=10
                radio_destruccion=4
            elif (hola["properties"]["bomba"] == "neutro"):
                radio_radiacion=20
                radio_destruccion=10
            else:
                radio_radiacion=2
                radio_destruccion=1
            ##############################
            # actualiza punto
            ##############################
            b = float(hola['geometry']['coordinates'][0])
            a = float(hola['geometry']['coordinates'][1])
            Geometria.objects.filter(id=1).update(
                class_coordinates=[ b,a ]
                )
            ##############################
            # actualiza circulo de destruccion
            ##############################
            circulo_d = genera_circulo_2(a,b,radio_destruccion)
            Geometria.objects.filter(id=2).update(
                class_coordinates=circulo_d
                )
            ##############################
            # actualiza circulo de radiacion
            ##############################
            circulo_r = genera_circulo_2(a,b,radio_radiacion)
            Geometria.objects.filter(id=3).update(
                class_coordinates=circulo_r
                )
            ##############################
            # calculando interseccion
            ##############################
            geo = json.loads(Geometria.objects.filter(id=5).get().class_coordinates)
            p_list_1 = conversor_poligonoGoogle_a_poligonoShapely(geo[0])
            p_list_2 = conversor_poligonoGoogle_a_poligonoShapely(circulo_d[0])
            p_1 = lista_a_poligono(p_list_1)
            p_2 = lista_a_poligono(p_list_2)
            inter = interseccion(p_1,p_2)
            mi_lista = poligono_a_lista_shapely(inter)
            salida = conversor_poligonoShapely_a_poligonoGoogle(mi_lista)
            Geometria.objects.filter(id=4).update(
                class_coordinates=[salida]
            )
            ##############################
            # calculando muertos
            ##############################
            muer = muertos(32970000,area(inter),area(p_1))

        respuesta = {
	        "type": "Feature",
            "properties": {
		        "mensaje": "se hizo update! ",
                "muertos": muer
	        }
        }
        return JsonResponse(respuesta)


# ========================================================
# MODULO
# ========================================================
from distutils.ccompiler import gen_lib_options
import json
import math
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

poligono_de_prueba = Polygon([(0, 5), (1, 1), (3, 0), (4, 6)])
numero_de_lados_del_circulo = 30

'''
MACRO: En general las funciones:

input: poligono / numero
output: poligono / numero / boleano / list
'''


'''
input: numero 
output: poligono 
'''
def genera_circulo(radio):
    circulo = 2 * math.pi # angulo total de la circunferencia en radianes
    angulo = 12
    arreglo = list()
    sec = numero_de_lados_del_circulo # numero de secciones que tiene el circulo
    angulo = circulo / sec # tamaño de la seccion en radianes
    for i in range(sec):
        x = radio*math.cos(angulo*i)
        y = radio*math.sin(angulo*i)
        arreglo.append((x,y))
    return Polygon(arreglo)

'''
input: numero 
output: lista [] 
'''
def genera_circulo_2(latitud,longitud, radio):
    circulo = 2 * math.pi # angulo total de la circunferencia en radianes
    angulo = 12
    arreglo = list()
    sec = numero_de_lados_del_circulo # numero de secciones que tiene el circulo
    angulo = circulo / sec # tamaño de la seccion en radianes
    for i in range(sec):
        x_circulo = radio*math.cos(angulo*i)
        y_circulo = radio*math.sin(angulo*i)
        arreglo.append([x_circulo,y_circulo])
    return arreglo

'''
input: poligono
output: nada
'''
def dibuja_3(polygon1,polygon2,polygon3):
    plt.rcParams["figure.figsize"] = [5.00, 5.0]
    plt.rcParams["figure.autolayout"] = True
    x, y = polygon1.exterior.xy
    plt.plot(x, y, c="red")
    x, y = polygon2.exterior.xy
    plt.plot(x, y, c="blue")
    x, y = polygon3.exterior.xy
    plt.plot(x, y, c="green")
    plt.show()

'''
input: poligono
output: nada
'''
def dibuja_2(polygon1,polygon2):
    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    x, y = polygon1.exterior.xy
    plt.plot(x, y, c="red")
    x, y = polygon2.exterior.xy
    plt.plot(x, y, c="blue")
    plt.show()

'''
input: poligono
output: poligono
'''
def interseccion(p1,p2):
    inter = p2.intersection(p1)
    return inter

'''
input: poligono
output: boleano
'''
def es_formato_poligono(poli):
    if poli.geom_type == 'Polygon':
        print(True)
    else:
        print(False)

'''
input: poligono
output: numero
'''
def area(p1):
    return p1.area

'''
input: numero
output: numero
'''
def muertos(habi_tota, supe_inte, supe_pais):
    habi_muer = supe_inte * habi_tota / supe_pais
    return habi_muer


# ========================================================
# PRUEBA DE MODULO
# ========================================================
'''
# usar el siguiente codigo de prueba para ver la funcionalidad de este modulo:

# este es un poligono de prueba
p1 = poligono_de_prueba

# hacer que el circulo generado tenga 30 lados
numero_de_lados_del_circulo = 30

# generas un circulo de radio 2
p2 = genera_circulo(2)

# intersectas ambos poligonos 
p3 = interseccion(p1,p2)

# imprime las areas de los tres poligonos
print("area 1: " + str(area(p1)) + "\narea 2: " + str(area(p2)) + "\narea 3: " + str(area(p3)) )

#calculamos muertos
habi_tota = 1000000 # asumiendo que el pais tiene 1M de habitantes
supe_inte = area(p3)
supe_pais = area(p1)
print(muertos(habi_tota, supe_inte, supe_pais))

# dibuja los tres poligonos (el de prueba, el circuilo generado y la interseccion)
dibuja_3(p1,p2,p3)
'''


# print(genera_circulo_2(5))
# simulador de bombas
 ¿quieres ver cuantos moririan?


# json
```json
{
    "id": 1,
    "nombre": "geometria 1",
    "tipo": "tipo",
    "coordenadas": "[-1.23234, 34.12331], [-1.23234, 34.12331], [-1.23234, 34.12331], [-1.23234, 34.12331]"
  },
```
# division
## front
Las entradas son:
- solo da un punto geografico
- tipo de bomba
## back
- los calculos los hace el back
## base de datos
- debe tener informacion de contorno de pais o continente
## calculos de funcion
el orden seria el siguiente:
- formula del circulo a partir del punto entregado por el front
- obtener superficie circulo
- realizar interseccion (circulo pais)
- obtener superficie de interseccion
- calculo de cantidad de muertos (superficie intereccion entre superficie pais)

```
 sup. pais      sup. interseccion
------------- = -----------------
# total de h.        # muertos
```

# informacion
asi comentamos el codigo en el back
```python
# ========================================================
# PRUEBA DE MODULO
# ========================================================
```
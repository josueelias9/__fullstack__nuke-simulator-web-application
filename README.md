# simulador de bombas
 ¿quieres ver cuantos moririan?

# funcionamiento alto nivel
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
# documentacion
- la forma de comunicacion es a traves de archivos json
- tener en cuenta tambien que el formato es geojson
- django entrega el feature collection completo de la base de datos
- en el back estara toda la infomacion. Si se quiere se ejecutara algo ene le view pero deber terminar el el db
## documentacion de codigo
asi comentamos el codigo en el back
```python
# ========================================================
# PRUEBA DE MODULO
# ========================================================
```

## flujo de comunicacion en json
```
+-----+                 +-----+             +-----+ 
|     |     tipo_f      |     |             |     | 
|front|      --->       |back |    --->     |db   | 
|     |      <---       |     |    <---     |     | 
+-----+     tipo_fc     +-----+             +-----+ 
```

- tipo_fc: feature colection completro

```json
{
	"type": "FeatureCollection",
	"features": [

		{
			"type": "Feature",
			"properties": {
				"color": "blue",
				"info": "es otro punto"
			},
			"geometry": {
				"type": "Polygon",
				"coordinates": [
					[
						[10.0, 0.0],
						[8.090169943749475, 5.877852522924732],
						[3.0901699437494745, 9.510565162951535],
						[-3.0901699437494736, 9.510565162951536],
						[-8.090169943749473, 5.877852522924733],
						[-10.0, 1.2246467991473533e-15],
						[-8.090169943749476, -5.87785252292473],
						[-3.0901699437494754, -9.510565162951535],
						[3.0901699437494723, -9.510565162951536],
						[8.090169943749473, -5.877852522924734],
						[10.0, 0.0]
					]
				]
			}
		},

		{
			"type": "Feature",
			"properties": {
				"color": "blue",
				"info": "este dato lo envio front"
			},
			"geometry": {
				"type": "Point",
				"coordinates": [-3.0901699437494736, 9.510565162951536]
			}
		}

	]
}
```

- tipo_f: feature

```json
{
	"type": "Feature",
	"properties": {
		"color": "blue",
		"info": "es otro punto"
	},
	"geometry": {
		"type": "Polygon",
		"coordinates": [
			[
				[10.0, 0.0],
				[8.090169943749475, 5.877852522924732],
				[3.0901699437494745, 9.510565162951535],
				[-3.0901699437494736, 9.510565162951536],
				[-8.090169943749473, 5.877852522924733],
				[-10.0, 1.2246467991473533e-15],
				[-8.090169943749476, -5.87785252292473],
				[-3.0901699437494754, -9.510565162951535],
				[3.0901699437494723, -9.510565162951536],
				[8.090169943749473, -5.877852522924734],
				[10.0, 0.0]
			]
		]
	}
}   
```
### tipos de properties
```json
"properties": {
		"color": "blue",               <->
		"info": "es otro punto",       <->
		"mensaje":"para señalizacion", <-
		"bomba": "tipo de bomba"        ->
	},
```
(buscar la referencia oficial de la estructura geojson)
## comunicacion 2
### funcion del frontend
- cuando hace GET, solo usa fecth para traer info. La funcion devuelve el response como tipo [object](https://www.w3schools.com/js/js_objects.asp).
- cuando es POST, el output es lo mismo que en get. El input es un tipo FomrData.

### funciones del backend
- GET, POST, PUT y DELETE reciben _request_. En _request.body_ se encuentra el json entregado por el back en formato binario (_<class 'bytes'>_).
- Todas devuelven _JsonResponse(respuesta)_ que es de tipo _<class 'django.http.response.JsonResponse'>_. _respuesta_ es un diccionario Python

# hacer funcionar
## set
```bash
cd (carpeta proyecto)/simulador-de-bombas/backend
python3 -m venv ./env
source (carpeta proyecto)/simulador-de-bombas/backend/env/bin activate
pip3 install -r requirements.txt
cd (carpeta proyecto)/simulador-de-bombas/backend/proyecto
python3 manage.py runserver
```
## usuario envia datos del punto
Interactuar con la GUI
# estructura del proyecto
```
|-- simulador-de-bombas
    |-- README.md (documentacion)
	|-- frontend
        |-- api_rest.js (definicion de funciones get, post para comunicacion con URL para la API)
        |-- google_api.js (codigo para mostrar la informacion de la bd en el front)
	|-- backend
        |-- requirements.txt
		|-- env
        |-- proyecto
            |-- aplicacion
	            |-- calculation.py (modulo creado por nosotros)
```

# referencia 
- Metodo fetch - [link](https://developer.mozilla.org/en-US/docs/Web/API/fetch)
- KML de paises del mundo - [link](https://laprovence.carto.com/tables/world_country_borders_kml/public/map)
- google map ioficial [link](https://developers.google.com/)
  - buscar “Maps Platform”
  - ir a SDK de Maps y dar click a “JS”
  - ir “Samples”
  - luego a “Layers”
  -  finalmente “Data Layer: Styling”

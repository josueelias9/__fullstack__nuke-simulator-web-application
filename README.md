# simulador de bombas
 ¿quieres ver cuantos moririan?

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
# 2022-03-10
- la forma de comunicacion es a traves de archivos json
- tener en cuenta tambien que el formato es geojson
- django entrega el feature collection completo de la base de datos
- en el back estara toda la infomacion. Si se quiere se ejecutara algo ene le view pero deber terminar el el db
## flujo de comunicacion en json
```
+-----+                     +-----+             +-----+ 
|     |       tipo_f        |     |             |     | 
|front|         --->        |back |    --->     |db   | 
|     |         <---        |     |    <---     |     | 
+-----+  tipo_fc / tipo_m   +-----+             +-----+ 
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
- tipo_m
modificarlo para que sea como uno de los anteriores y podamos homologenizar la comunucacions
### tipos de properties
```json
"properties": {
		"color": "blue", <->
		"info": "es otro punto", <->
		"radio":"10", ->
		"mensaje":"para señalizacion" <-
	},
```
(buscar la referencia oficial de la estructura geojson)

# hacer funcionar
## set
```bash
cd (carpeta proyecto)/simulador-de-bombas/backend
python3 -m venv ./env
source (carpeta proyecto)/simulador-de-bombas/backend/env/bin activate
pip3 install requirements
cd (carpeta proyecto)/simulador-de-bombas/backend/proyecto
python3 manage.py runserver
```
## usuario envia datos del punto
ir a _api_rest.js_ y modificar las coordenadas. Luego aplicar post y listo. 
```json
geometry: {
    type: "Point",
    coordinates: [
        -10.1801699437494736,
        9.82055162951536
    ]
}
```
## modificar base de datos
hacerlo atraves de la consola de django (por el momento)

# estructura del proyecto
```
|-- simulador-de-bombas
    |-- backend
        |-- env
        |-- proyecto
        |-- requirements
    |-- frontend
        |-- api_rest.js (definicion de funciones get, post para comunicacion con URL para la API)
        |-- google_api.js (codigo para mostrar la informacion de la bd en el front)
    |-- README.md (documentacion)
```
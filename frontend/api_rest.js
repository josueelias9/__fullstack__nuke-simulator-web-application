
// api url

// Defining async function
async function getapi() {

    // Storing response
    let response = await fetch("http://127.0.0.1:8000/aplicacion/casa/");
    // Storing data in form of JSON
    let data_json = await response.json();

    console.log(data_json["features"][2]["geometry"]["coordinates"]);
}
// Calling that async function

async function postapi() {
    data = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            type: "Feature",
            properties: {
                info: "llego este paquete del fron?",
                color: "blue",
                radio:"10"
            },
            geometry: {
                type: "Point",
                coordinates: [
                    -10.1801699437494736,
                    9.82055162951536
                ]
            }
        }
        )
    }
    let respo = await fetch("http://127.0.0.1:8000/aplicacion/casa/", data);
    let data_json = await respo.json();
    console.log(data_json);
}

postapi();
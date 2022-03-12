

async function getapi(api_url_django) {
    let response = await fetch(api_url_django);
    let data_json = await response.json();
    console.log(data_json["features"][2]["geometry"]["coordinates"]);
    return data_json;
}

async function povstapi() {
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
                bomba:"medium bomb"
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
    console.log(data_json["type"]);
}


async function postapi(api_url_django,formData) {
    
    const value = Object.fromEntries(formData.entries());
    let xx={
        method: 'post',
        body: JSON.stringify(value)
    }
    let respo = await fetch(api_url_django, xx);
    let data_json = await respo.json();
    console.log(data_json);
    return data_json;
}



async function putapi(api_url_django,formData){
    const value = Object.fromEntries(formData.entries());
    let xx = {
        method:'put',
        body: JSON.stringify(value)
    }
    let respo = await fetch(api_url_django,xx);
    let data_json = await respo.json();
    console.log(data_json);
    return data_json;
}
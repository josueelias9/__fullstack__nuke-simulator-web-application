
async function getapi(api_url_django) {
    let response = await fetch(api_url_django);
    let data_json = await response.json();
    //console.log(data_json) // borrar esta linea despues
    return data_json;
}


async function postapi(api_url_django, formData) {

    const value = Object.fromEntries(formData.entries());
    let xx = {
        method: 'post',
        body: JSON.stringify(value)
    }

    let respo = await fetch(api_url_django, xx);
    let data_json = await respo.json();
    // console.log(data_json) // borrar esta linea despues
    return data_json;
}



async function putapi(api_url_django, formData) {
    const value = Object.fromEntries(formData.entries());
    let mensaje = {
        type: "Feature",
        properties: {
            color: "",
            info: ""
        },
        geometry: {
            type: "",
            coordinates: [value["longitud"], value["latitud"]]
        }
    }
    let objeto_json = {
        method: 'put',
        body: JSON.stringify(mensaje)
    }
    let respuesta = await fetch(api_url_django, objeto_json);
    let data_json = await respuesta.json();

    return data_json;

}
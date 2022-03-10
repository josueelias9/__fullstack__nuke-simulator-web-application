
// api url
const api_url = "http://127.0.0.1:8000/aplicacion/casa/";
//"https://reqres.in/api/products/3";

// Defining async function
async function getapi(url) {

    // Storing response
    const response = await fetch(url);

    // Storing data in form of JSON
    var data = await response.json();

    console.log(data[0]);
}
// Calling that async function

async function postapi(url){
    data = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            punto: "donde caera la bomba",
            bomba: "que bomba sera?"
        })
    }
    const respo = await fetch(url,data);
    console.log("se ejecuto post");
}

// postapi(api_url);
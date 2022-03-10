
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: { lat: -3.0901699437494754, lng: -9.510565162951535 },

  });
  // Load GeoJSON.
  map.data.loadGeoJson(
    "http://127.0.0.1:8000/aplicacion/casa/"

  );
  // Set the stroke width, and fill color for each polygon


  // Add some style.
  map.data.setStyle((feature) => {
    return  {
      fillColor: feature.getProperty("color"),
      strokeWeight: 1,
    };
  });
}





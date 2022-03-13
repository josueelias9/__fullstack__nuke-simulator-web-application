
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: { lat: -12.0431800, lng: -77.0282400 },
  });
  // Load GeoJSON.
  map.data.loadGeoJson(
    "http://127.0.0.1:8000/aplicacion/casa/"

  );

  map.data.setStyle((feature) => {
    return {
      fillColor: feature.getProperty("color"),
      strokeWeight: feature.getProperty("strokeWeight"),
    };
  });
}





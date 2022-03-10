
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: { lat: -28, lng: 137 },
  });
  // Load GeoJSON.
  map.data.loadGeoJson(
    "http://127.0.0.1:8000/aplicacion/casa/"
    
  );
  // Set the stroke width, and fill color for each polygon
  map.data.setStyle({
    fillColor: "green",
    strokeWeight: 1,
  });
}
function setMap() {
    console.log("Loading map");

    // Norkart: var map = L.map("map").setView([63.43, 10.395], 14);
    var mymap = L.map('mapid').setView([51.505, -0.09], 13);
    //Set view takes two parameters;
    //1. The coordinates for the center of the map
    //2. The zoom level. Zoomlevel is from 0 -> 22, where 22 is zoomed in an 0 is zoomed out

    //Adding the base map. Base map decides how the background map looks like

    /* Norkart:
    var basemapUrl = "http://{s}.tile.osm.org/{z}/{x}/{y}.png";
    L.tileLayer(basemapUrl).addTo(map);
    */
   L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'pk.eyJ1IjoibWFydGVodmkiLCJhIjoiY2pyaG54N2V0MDlxdzQ1cWt3cTJldDV5ZiJ9.B09_TlrzbWF5AWOWUc6qUw',
    accessToken: 'mapbox://styles/martehvi/cjrholi4o4scq2to7klr96dpc'
    }).addTo(mymap);
    //Adding geoJSON layer to the map:

    // Norkart: L.geoJSON(utesteder).addTo(map);
}

window.onload = setMap;

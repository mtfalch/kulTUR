function setMap() {
    console.log("Loading map");
  
    var map = L.map('map').setView([63.40, 10.385], 11);
    //Set view takes two parameters;
    //1. The coordinates for the center of the map
    //2. The zoom level. Zoomlevel is from 0 -> 22, where 22 is zoomed in an 0 is zoomed out
  
    // Mapbox
    //const accessToken = "pk.eyJ1IjoibWFydGVodmkiLCJhIjoiY2pyaG54N2V0MDlxdzQ1cWt3cTJldDV5ZiJ9.B09_TlrzbWF5AWOWUc6qUw";
    //const id = "dark-v9";
    //var basemapUrl = "https://api.tiles.mapbox.com/v4/{id}/tiles/{z}/{x}/{y}.png?access_token={accessToken}";
    //dette funka v
    basemapUrl = "https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png"
    L.tileLayer(basemapUrl).addTo(map);
  
    // EKSTRA
    var marker = L.marker([63.43049, 10.39506]).addTo(map);
    var popUp = marker.bindPopup("<b>Heisann!</b><br>Klar for en tur i Trondheims flotte mark?");
    map.on('click', popUp.openPopup);

    //Adding geoJSON layer to the map:
    //L.geoJSON(utesteder).addTo(map);
  }
  
  window.onload = setMap();
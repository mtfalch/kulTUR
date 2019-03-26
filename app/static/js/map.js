function setMap() {
    console.log("Loading map");

    //Set view takes two parameters;
    //1. The coordinates for the center of the map
    //2. The zoom level. Zoomlevel is from 0 -> 22, where 22 is zoomed in an 0 is zoomed out
    map = L.map('map').setView([63.40, 10.385], 11);

    basemapUrl = "https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png"
    L.tileLayer(basemapUrl).addTo(map);

}

window.onload = setMap();
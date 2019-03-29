function setUserMap() {
    console.log("Loading usermap");

    //Set view takes two parameters;
    //1. The coordinates for the center of the map
    //2. The zoom level. Zoomlevel is from 0 -> 22, where 22 is zoomed in an 0 is zoomed out
    usermap = L.map('usermap').setView([63.43, 10.385], 11);

    basemapUrl = "https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png"
    L.tileLayer(basemapUrl).addTo(usermap);

}

    function highlightFeature(e) {
        var layer = e.target;

        layer.setStyle({
            //stroke: true,
            weight: 10,
            dashArray: '',
            opacity: 0.7,
            color: '#FFA061'

        });

        if (!L.Browser.ie && !L.Browser.opera) {
            layer.bringToFront();
        }
    }

    function resetHighlight(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 4,
            color: '#FFA061',
            dashArray: '',
            opacity: 1
        });
    }

    function onEachFeature2(feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight
        });

    }

    var userLayer = null
    function get_user_trips() {
        data = $.ajax({
            url: 'http://localhost:5000/usertrips',// må endres for localhost/heroku. 'https://kulturen.herokuapp.com/tracks'
            type: 'GET',
            datatype: 'json'
        })

        $.when(data).done(function (res) {
            console.log(res)

            userLayer = L.geoJSON(res, {onEachFeature: onEachFeature2}).addTo(usermap)

            userLayer.setStyle({
                weight: 4,
                color: '#FFA061',
                dashArray: '',
                Opacity: 1
            })
        });
    }

// ON/OFF tracks
    //function addDataToMap() {
    //    usermap.addLayer(turLayer);

    //}


window.onload = setUserMap();
window.onload = get_user_trips()
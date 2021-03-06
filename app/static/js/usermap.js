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
        var rutenavn = '<h5><span class="glyphicon glyphicon-tree-conifer"></span> '+feature.properties.RUTENAVN+' ('+feature.properties.OBJTYPE+')</h5>'
        layer.bindTooltip(rutenavn)
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight
        });

    }

    var userLayer = null
    function get_user_trips() {
        data = $.ajax({
            url: 'https://kulturen.herokuapp.com/usertrips',// må endres for localhost/heroku. 'https://kulturen.herokuapp.com/tracks'
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
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


    var turLayer = null;
    var data = null;

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
        var lid = feature.properties.LOKALID
        var rutenavn = '<h5><span class="glyphicon glyphicon-tree-conifer"></span> '+feature.properties.RUTENAVN+' ('+feature.properties.OBJTYPE+')</h5>'
        var chooseTrip = '<h4><span class="glyphicon glyphicon-map-marker"></span><a href="#" class="speciallink"> Velg denne turen</a></h4>'
        var link = $(chooseTrip).click(function() {
            clicked(lid)
        })[0];
        var res = rutenavn+chooseTrip

        layer.bindPopup(res)
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight
        });

    }

    function clicked(variabel) {
        console.log('clicked')
        console.log(variabel)
        var lokalid = variabel;
        console.log(lokalid)

        var today = new Date();
        dd = String(today.getDate()).padStart(2, '0');
        mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        yyyy = today.getFullYear();
        today = dd + mm + yyyy;
        console.log(typeof(today))

        $.ajax({
            url: 'http://localhost:5000/usertrips',
            headers: {
                'Content-Type': 'application/json'
            },
            type: 'POST',
            data: {
                date: today,
                lid: lokalid,
            },
            success: function() {
                alert('For deg som er logget inn: Turen er registrert. Om du ikke var innlogget må du gjøre dette for å få registrert en tur.')
            },
            error: function() {
                alert('du må logge inn')
            }
        })
    }

    function get_data() {
        console.log('running');
        data = $.ajax({
            url: 'http://localhost:5000/tracks',// må endres for localhost/heroku. 'https://kulturen.herokuapp.com/tracks'
            type: 'GET',
            datatype: 'json'
        })

        $.when(data).done(function (res) {

            turLayer = L.geoJSON(res, {onEachFeature: onEachFeature2});

            turLayer.setStyle({
                weight: 4,
                color: '#FFA061',
                dashArray: '',
                Opacity: 1
            })
        });
    }

// ON/OFF tracks
    function addDataToMap(checkboxElem) {

        if (checkboxElem.checked) {
            console.log('Checked')
            console.log(turLayer)
            map.addLayer(turLayer);
        } else {
            console.log('Not checked')
            map.removeLayer(turLayer);
        }
    }

    window.onload = get_data();

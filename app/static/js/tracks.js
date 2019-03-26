
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

function onEachFeature(feature, layer) {
    {
        layer.bindPopup('<b>'+feature.properties.RUTENAVN+'</b><p> Turtype: '+feature.properties.OBJTYPE+'</p>');
    }
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        //click: zoomToFeature
    });
}

// ON/OFF tracks
function get_data() {
    var data = $.ajax({
        url: 'http://localhost:5000/tracks',
        type: 'GET',
        datatype: 'json'
    });

    $.when(data).done(function addDataToMap(data, checkboxElem) {
        console.log(data)
        var re = L.geoJSON(data, {onEachFeature: onEachFeature2});
        if (checkboxElem.checked) {
            map.addLayer(re)
        } else {
            map.removeLayer(re);
        }
    });
}

function onEachFeature2(feature, layer) {
        layer.bindPopup(feature.properties.popupContent);
    }


//data.setStyle({
//    weight: 4,
//    color: '#FFA061',
//    dashArray: '',
//    Opacity: 1
//})

function toggletracks(data) {
    var data = L.geoJSON(data.responseJSON, {onEachFeature: onEachFeature})
    if (checkboxElem.checked) {
        map.addLayer(data)
        map.fitBounds(data.getBounds())
    } else {
        map.removeLayer(data);
    }
}
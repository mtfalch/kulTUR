var group = L.geoJSON(cabins, {
    onEachFeature: function (feature, layer) {
        layer.bindPopup('<b>'+feature.properties.name+'</b><p> Åpningstider: '+feature.properties.open+'</p>');
    }
})

function doalert(checkboxElem) {
    if (checkboxElem.checked) {
        map.addLayer(group)

    } else {
        map.removeLayer(group);
    }
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


function onEachFeature(feature, layer) {
    {
        layer.bindPopup('<b>'+feature.properties.RUTENAVN+'</b><p> Tur: '+feature.properties.OBJTYPE+'</p>');
    }
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        //click: zoomToFeature
    });
}

// ON/OFF tracks
var tracks = L.geoJSON(geojson, {
    onEachFeature: onEachFeature
})

tracks.setStyle({
    weight: 4,
    color: '#FFA061',
    dashArray: '',
    Opacity: 1
})

function toggletracks(checkboxElem) {
    if (checkboxElem.checked) {
        map.addLayer(tracks)

    } else {
        map.removeLayer(tracks);
    }
}







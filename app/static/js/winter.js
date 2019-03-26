
var winterLayer = null;
var data = null;

function highlightFeatureW(e) {
  var layer = e.target;

  layer.setStyle({
    //stroke: true,
    weight: 10,
    dashArray: '',
    opacity: 0.7,
    color: '#396d7c'

  });

  if (!L.Browser.ie && !L.Browser.opera) {
    layer.bringToFront();
  }
}

function resetHighlightW(e) {
  var layer = e.target;

  layer.setStyle({
      weight: 4,
      color: '#396d7c',
      dashArray: '',
      opacity: 1
  });
}

function onEachFeature3(feature, layer) {
    layer.on({
        mouseover: highlightFeatureW,
        mouseout: resetHighlightW,
        //click: zoomToFeature
    });
}

function get_data() {
    console.log('running');
    data = $.ajax({
            url: 'https://kulturen.herokuapp.com/tracks/winter', // må endres for localhost
            type: 'GET',
            datatype: 'json'
    })

    $.when(data).done(function (res) {

        winterLayer = L.geoJSON(res, {onEachFeature: onEachFeature3});

        winterLayer.setStyle({
            weight: 4,
            color: '#396d7c',
            dashArray: '',
            Opacity: 1
        })
    });
}

// ON/OFF tracks
function addWinterToMap(checkboxElem) {
     if (checkboxElem.checked) {
         console.log('Checked')
         console.log(winterLayer)
         map.addLayer(winterLayer);
     } else {
         console.log('Not checked')
         map.removeLayer(winterLayer);
     }
}
window.onload = get_data();
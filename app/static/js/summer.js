
var summerLayer = null;
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

function onEachFeature4(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        //click: zoomToFeature
    });
}

function get_data() {
    console.log('running');
    data = $.ajax({
            url: 'http://localhost:5000/tracks/summer',// må endres for localhost
            type: 'GET',
            datatype: 'json'
    })

    $.when(data).done(function (res) {

        summerLayer = L.geoJSON(res, {onEachFeature: onEachFeature4});

        summerLayer.setStyle({
            weight: 4,
            color: '#FFA061',
            dashArray: '',
            Opacity: 1
        })
    });
}

// ON/OFF tracks
function addSummerToMap(checkboxElem) {
     if (checkboxElem.checked) {
         console.log('Checked')
         console.log(summerLayer)
         map.addLayer(summerLayer);
     } else {
         console.log('Not checked')
         map.removeLayer(summerLayer);
     }
}
window.onload = get_data();
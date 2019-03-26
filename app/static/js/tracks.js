
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
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        //click: zoomToFeature
    });
}

function get_data() {
    console.log('running');
    data = $.ajax({
            url: 'https://kulturen.herokuapp.com/tracks',
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



function toggletracks(data) {
    var data = L.geoJSON(data.responseJSON, {onEachFeature: onEachFeature})
    if (checkboxElem.checked) {
        map.addLayer(data)
        map.fitBounds(data.getBounds())
    } else {
        map.removeLayer(data);
    }
}
window.onload = get_data();
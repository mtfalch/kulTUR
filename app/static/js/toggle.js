var group = L.geoJSON(cabins, {
    onEachFeature: function (feature, layer) {
        layer.bindPopup('<h3><span class="glyphicon glyphicon-home"></span> '+feature.properties.name+'</h3><p> Åpningstider: '+feature.properties.open+'</p>');
    }
})

function doalert(checkboxElem) {
    if (checkboxElem.checked) {
        map.addLayer(group)
    } else {
        map.removeLayer(group);
    }
}

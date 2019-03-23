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
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

var objectData = {
    input: document.getElementById('Input').value,
}

function getData(){
    $.ajax({
        url: 'http://127.0.0.1:5000/tracks/<location>', // Må kanskje ha en url foran også typ localhost
        type: 'GET',
        data: {
            o: objectData
        },
        success: function (data){

        }
    })
}

function successCallback(response){
    var res = L.geoJSON(response)
    map.addLayer(res);
}

function search(data){
    print(data);
    var x = getElementByID("Input");
    var res = L.geoJSON(data)
    map.addLayer(res)
}



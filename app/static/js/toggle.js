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

var selectLayer = null;
var data = null;

function choose_data(value) {
    console.log('running');
    data = $.ajax({
            url: 'http://localhost:5000/tracks/<location>',
            type: 'GET',
            datatype: 'json'
    })

    $.when(data).done(function (res) {

        selectLayer = L.geoJSON(res, {onEachFeature: onEachFeature2});

        turLayer.setStyle({
            weight: 4,
            color: '#FFA061',
            dashArray: '',
            Opacity: 1
        })
    });
}

window.onload = get_data();


/*var objectData = {
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
    map.addLayer(res)*/




var bymarka = null;
var data = null;


function get_bymarka() {
    console.log('running');
    data = $.ajax({
            url: 'http://localhost:5000/tracks/Bymarka',
            type: 'GET',
            datatype: 'json'
    })

    $.when(data).done(function (res) {

        bymarka = L.geoJSON(res, {onEachFeature: onEachFeature2});

        bymarka.setStyle({
            weight: 4,
            color: '#FFA061',
            dashArray: '',
            Opacity: 1
        })
    });
}

function addDataToMap1(checkboxElem) {

        if (checkboxElem.checked) {
            console.log('Checked')
            console.log(bymarka)
            map.addLayer(bymarka);
        } else {
            console.log('Not checked')
            map.removeLayer(bymarka);
        }
}

function toggletracks2(data) {
    var data = L.geoJSON(data.responseJSON, {onEachFeature: onEachFeature})
    if (checkboxElem.checked) {
        map.addLayer(data)
        map.fitBounds(data.getBounds())
    } else {
        map.removeLayer(data);
    }
}
window.onload = get_bymarka();
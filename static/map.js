var map;
var myLatLng = {lat: 44.479956, lng: -73.197765};
function initMap() {
map = new google.maps.Map(document.getElementById('map'), {
  center: myLatLng,
  zoom: 19
});


var contentString = '<h2>GPR Path Point</h2>' +

    '<ol>' +
    '<li>Latitude = ' + myLatLng.lat + '</li>' +
    '<li>Longitutde = ' + myLatLng.lng + '</li>' +
    '</ol>' +
    "<div style='float:left;'><img src='../static/images/gpr-figure-lab.png'></div>"
    ;

var infowindow = new google.maps.InfoWindow({
      content: contentString
});





var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
marker.addListener('click', function() {
          infowindow.open(map, marker);
});



var gprPathCoordinates = [
    {lat: 44.479999, lng: -73.197765},
    {lat: 44.479956, lng: -73.197765}
  ];
  var gprPath = new google.maps.Polyline({
    path: gprPathCoordinates,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 5
  });

  gprPath.setMap(map);



}

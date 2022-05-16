let map = null;
let zoom = 15;
window.onload = onLoadActions;


function onLoadActions() {
    drawMap()
    addMapClickEvent();
    centerPosition();
}

function drawMap(){
    let mapOptions = {
        center: new naver.maps.LatLng(37.558182258806, 126.92890711141),
        zoom: zoom,
        zoomControl: true,
    };
    
    map = new naver.maps.Map('map', mapOptions);
    
}


function centerPosition(){
    navigator.geolocation.getCurrentPosition((position) => {
        setCenter(position.coords.longitude, position.coords.latitude);
    });
}


let currentCenterMarker;
let currentInfoWindow;


function drawMap(){
    let mapOptions = {
        center: new naver.maps.LatLng(37.558182258806, 126.92890711141),
        zoom: 15,
        zoomControl: true,
    };
    map = new naver.maps.Map('map', mapOptions);
}

let clickedMarkers = [];
function addMapClickEvent(){
    console.log(map);
    naver.maps.Event.addListener(map, "click", (e) => {
        console.log(e);
        if(currentCenterMarker != null){
            hideMarker(currentCenterMarker);
        }
        
        currentCenterMarker = null;
        currentCenterMarker = drawNewMarker(map, e.coord.y, e.coord.x);
        // clickedMarkers.push(drawNewMarker(map, e.coord.y, e.coord.x));
    });
}

function showMarker(map, marker) {
    if(marker.getMap()) return;
    marker.setMap(map);
}

function hideMarker(marker) {
    if(!marker.getMap()) return;
    marker.setMap(null);
}



function infoWindowDefaultListener(marker, infoWindow){
    naver.maps.Event.addListener(marker, "click", (e) => {
        if (infoWindow.getMap()) {
            infoWindow.close();
        } else {
            infoWindow.open(map, marker);
        }
    });
}




function reset(){
    clickedMarkers.forEach(marker => {
        hideMarker(marker);
    });
    clickedMarkers.splice(0, clickedMarkers.length);
    clickedMarkers.length = 0;
}

function sendSelectedPointsToServer(){
    let payload = {
        points: []
    }
    clickedMarkers.forEach(marker => {
        let point = {
            lat: marker.getPosition().x,
            long: marker.getPosition().y,
        }
        payload.points.push(point);
    });

    fetch("/map/save-points/", {
        method: "post",
        headers: {
            "X-CSRFToken": getCsrfToken(),
        },
        body: JSON.stringify(payload),
    }).then(response => {
        if(response.status != 200){
            alert("저장에 실패 했습니다!");
        } else {
            alert("저장에 성공 했습니다!");
        }
    });
}

function getPoints(){
    fetch("/map/get-points/")
        .then(response => {
            if (response.status == 200){
                response.json().then((responseBody) => drawPoints(responseBody.points));
            }
        });
}


function setCenter(lat, long){
    map.setCenter(new naver.maps.Point(lat, long));
}

function drawPoints(pointList){
    console.log(pointList);
    pointList.forEach(point => {
        console.log(point.lat);
        console.log(drawNewMarker(map, point.lat, point.long));
    });
}


function drawPoints(pointList){
    console.log(pointList);
    pointList.forEach(point => {
        console.log(point.lat);
        console.log(drawNewMarker(map, point.lat, point.long));
    });
}



function findInCookie(cookieName){
    return document.cookie.split(";")
        .find((item) => item.includes(cookieName))
        .split("=")[1];
}

function getCsrfToken(){
    return findInCookie("csrftoken")
}



function drawNewMarker(map, lat, long){
    return new naver.maps.Marker({
        map: map,
        position: new naver.maps.LatLng(lat, long),
        zIndex: 100
    });
}   

function drawCenterMarker(map){
    if (currentCenterMarker) hideMarker(currentCenterMarker);
    if (currentInfoWindow) currentInfoWindow.close();
    currentCenterMarker = drawNewMarker(map, map.getCenter().y, map.getCenter().x);
    currentInfoWindow = addInfoWindowToMarker(
        currentCenterMarker,
        `<div class="info-window">Last Center: ${map.getCenter().x}, ${map.getCenter().y}</div>`
    );
}

const defaultInfoElement = "Hello World!";
function addInfoWindowToMarker(marker, infoElement) {
    let infoWindow = new naver.maps.InfoWindow({
        content: infoElement ? infoElement : defaultInfoElement,
        marker: marker,
        zIndex: 150,
    });
    infoWindowDefaultListener(marker, infoWindow);
    return infoWindow;
}

function distance(){
    var map = new naver.maps.Map('map'),  
    coord1 = new naver.maps.LatLng(position.coords.latitude, position.coords.longitude),
    coord2 = new naver.maps.LatLng(37.638786, 127.2826951);
    map.getPrimitiveProjection().getDistance(coord1, coord2);
}
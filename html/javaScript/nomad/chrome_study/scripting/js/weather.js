// https://home.openweathermap.org/api_keys
const API_KEY = "406ccf356586ca4dee1d05e50923c2af";
const COORDS = 'coords';

function saveCoords(coordsObj){
    localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}

function handleGeoSuccess(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const coordsObj = {
        // 객체.. 키를 적지 않으면 값과 키는 동일한 이름 (latitude = latitude: latitude)
        latitude, 
        longitude
    };
    saveCoords(coordsObj);
}

function handleGeoError() {
    console.log("can't access geo location");
}

function askForCoords() {
    navigator.geolocation.getCurrentPosition(handleGeoSuccess, handleGeoError);
}

function loadCoords(){
    const loadedCoords = localStorage.getItem(COORDS);
    if (loadedCoords === null) {
        askForCoords();
    } else {
        // getWeather
    }
}

function init() {
    loadCoords();
}

init();
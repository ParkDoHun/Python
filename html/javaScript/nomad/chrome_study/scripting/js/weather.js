// https://home.openweathermap.org/api_keys
const weather = document.querySelector(".js-weather");

const API_KEY = "406ccf356586ca4dee1d05e50923c2af";
const COORDS = 'coords';

function getWeather(lat, lon) {
    fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        ).then(function(response) {
            return response.json();
        }).then(function(json) {
            const temperature = json.main.temp;
            const place = json.name;
            weather.innerText = `${temperature}℃ @ ${place}`
        });
        // then은 함수를 호출
}

function saveCoords(coordsObj){
    localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}

function handleGeoSuccess(position) {
    // 위도
    const latitude = position.coords.latitude;
    // 경도
    const longitude = position.coords.longitude;
    const coordsObj = {
        // 객체.. 키를 적지 않으면 값과 키는 동일한 이름 (latitude = latitude: latitude)
        latitude, 
        longitude
    };
    saveCoords(coordsObj);
    getWeather(latitude, longitude);
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
        const parseCoords = JSON.parse(loadedCoords);
        getWeather(parseCoords.latitude, parseCoords.longitude);
        // console.log(parseCoords);
    }
}

function init() {
    loadCoords();
}

init();
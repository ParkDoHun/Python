const clockContainer = document.querySelector('.js-clock');
const clockTitle = clockContainer.querySelector("h1");

function getTime () {
    const date = new Date();        // new 있어야 작동
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();

    clockTitle.innerText = `${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}:${seconds < 10 ? '0' + seconds : seconds}`;

}

function init () {
    getTime();
    setInterval(getTime, 1000);     // 콜백 함수, 매 초 마다 실행
}

init();
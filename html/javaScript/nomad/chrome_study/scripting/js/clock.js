const clockContainer = document.querySelector('.js-clock');
const clockTitle = clockContainer.querySelector("h1");

function getTime () {
    const date = new Date();        // Data 생성자 함수
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();

    clockTitle.innerText = `${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}:${seconds < 10 ? '0' + seconds : seconds}`;

}

function init () {
    getTime();
    setInterval(getTime, 1000);     // 매 초 마다 실행
}

init();

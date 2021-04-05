const mark = document.getElementById('mark');

const BASE_COLOR = "rgb(52, 73, 94)"; // 기본 색
const OTHER_COLOR = "#7f8c8d";  // 변경할 색

function handleEvent() {
    const currentcolor = mark.style.color;
    if(currentcolor == BASE_COLOR) {
        mark.style.color = OTHER_COLOR;
    }
        else {
            mark.style.color = BASE_COLOR;
        }
}

function init() {
    mark.style.color = BASE_COLOR;
    mark.addEventListener("mouseenter", handleEvent);
}
init();

function handleOffline() {
    console.log("lol");
}

function handleOnline() {
    console.log('Hi')
}

window.addEventListener("offline", handleOffline); // offline : 인터넷이 끊겼을때. 웹브라우저가 아님.
window.addEventListener("online", handleOnline);
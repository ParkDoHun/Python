const form = document.querySelector('.js-form');
const input = form.querySelector('input');
const greeting = document.querySelector('.js-greetings');

const USER_LS = "currentUser";
const SHOWING_CN = "showing";

function saveName(text) {
    localStorage.setItem(USER_LS, text);
}


function handleSubmit(event) {
    event.preventDefault(); // text폼 엔터키 기본 동작 막음
    const currentValue = input.value;
    paintGreeting(currentValue);
    saveName(currentValue);
}

function askForName() {
    form.classList.add(SHOWING_CN);
    form.addEventListener('submit', handleSubmit);
}

function paintGreeting(text) {
    form.classList.remove(SHOWING_CN);
    greeting.classList.add(SHOWING_CN);
    greeting.innerText = `Hello ${text}`;
}

function loadName() {
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null) {
        // 유저가 없을 때
        askForName();
    }else {
        // 유저가 있을 때
        paintGreeting(currentUser);
    }
}


function init() {
    loadName();
}

init();
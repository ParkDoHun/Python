const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector('input');
const toDoList = document.querySelector('.js-toDoList');

// LocalStorage
const TODOS_LS = 'toDos';

let toDos = [];

// 리스트 삭제
function deleteToDo(event) {
    const btn = event.target;
    const li = btn.parentNode;
    toDoList.removeChild(li);
    const cleanToDos = toDos.filter(function(toDo) {
        return toDo.id !== parseInt(li.id);
    });
    toDos = cleanToDos;
    saveToDos();
}

function saveToDos() {
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}

function paintToDo(text) {
    const li = document.createElement('li');
    const delBtn = document.createElement('button');
    const span = document.createElement('span');
    const newId = toDos.length + 1;

    // 이모지 : 윈도우키 + 세미콜론
    delBtn.innerText = "❌";
    delBtn.addEventListener('click', deleteToDo);
    span.innerText = text;
    li.appendChild(span);
    li.appendChild(delBtn);
    li.id = newId;
    toDoList.appendChild(li);

    const toDoObj = {
        text: text,
        id: newId
    };
    toDos.push(toDoObj);
    saveToDos();
}

function handleSubmit(event) {
    event.preventDefault();
    const currentValue = toDoInput.value;
    paintToDo(currentValue);
    // 입력 후 텍스트 리셋 (submit(?))
    toDoInput.value = "";
}

function loadToDos() {
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if(loadedToDos !== null) {
        // JSON : JavaScript Object Notarion, 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷
        const parsedToDos = JSON.parse(loadedToDos);
        // forEach는 배열 안에 있는 것을 한번씩 실행
            parsedToDos.forEach(function(toDo) {
                paintToDo(toDo.text);
            });
    } 
}

function init() {
    loadToDos();
    toDoForm.addEventListener("submit", handleSubmit);
}

init();
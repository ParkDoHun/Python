// 함수의 다양한 형태 : 콜백 함수
/*
    콜백 함수는 주로 비동기식 처리 모델(Asynchronous processing model)에 사용된다. 
    비동기식 처리 모델이란 처리가 종료하면 호출될 함수(콜백함수)를 미리 매개변수에 전달하고 처리가 종료하면 콜백함수를 호출하는 것이다.

    콜백함수는 콜백 큐에 들어가 있다가 해당 이벤트가 발생하면 호출된다. 콜백 함수는 클로저이므로 콜백 큐에 단독으로 존재하다가 호출되어도 콜백함수를 전달받은 함수의 변수에 접근할 수 있다.
*/

function doSomething() {
    var name = 'Lee';

    setTimeout(function () {
        console.log('My name is ' + name);
    }, 100);
}

doSomething();  // My name is Lee
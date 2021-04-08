// 7. 함수의 다양한 형태 : 즉시 실행 함수

    /*
    함수의 정의와 동시에 실행되는 함수를 즉시 실행 함수(IIFE, Immediately Invoke Function Expression)라고 한다.
    최초 한번만 호출되며 다시 호출할 수는 없다.
    이러한 특징을 이용하여 최초 한번만 실행이 필요한 초기화 처리등에 사용할 수 있다.
    */


    // 기명 즉시 실행 함수
    (function myFunction() {
        var a = 3;
        var b = 5;
        return a * b;
    }());

    // 익명 증시 실행 함수
    (function() {
        var a = 3;
        var b = 5;
        return a * b;
    }());

    // SyntaxError : Unexpected token (
    // 함수선언문은 자바스크립트 엔진에 의해 함수 몸체를 닫는 중괄호 뒤에 ;가 자동 추가된다.
    function () {
        // ...
    }();    // => };();

    // 따라서 즉시 실행 함수는 소괄호로 감싸준다.
    (function () {
        // ...
    }());

    (function () {
        // ...
    }());

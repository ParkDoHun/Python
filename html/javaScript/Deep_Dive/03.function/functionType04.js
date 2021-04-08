// 7. 함수의 다양한 형태 : 내부 함수

    function sayHello(name) {
        var text = 'Hello' + name;
        var logHello = function(){ console.log(text); }
        logHello();
    }

    // 내부함수는 부모함수의 외부에서 접근할 수 없다.
    sayHello('lee');    // Hello lee
    logHello('lee');    // Uncaught ReferenceError: logHello is not defined


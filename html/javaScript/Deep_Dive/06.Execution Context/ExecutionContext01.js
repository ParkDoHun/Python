// 실행 컨텍스트(Execution Context)는 scope, hoisting, this, 
// function, closure 등의 동작원리를 담고 있는 자바스크립트의 핵심원리이다.

var x = 'xxx';

function foo() {
    var y = 'yyy';

    function bar () {
        var z = 'zzz';
        console.log(x + y + z); // xxxyyyzzz
    }
    bar();
}
foo();
// 클로저(closure)
function outerFunc() {
    var x = 10;
    var innerFunc = function() {
        console.log(x);
    };
        return innerFunc;
}

/*
함수 outerFunc를 호출하면 내부 함수 innerFunc가 반환된다.
그리고 함수 outerFunc의 실행 컨텍스트는 소멸한다.
*/

var inner = outerFunc();
inner();    // 10

// 자신을 포함하고 있는 외부함수보다 내부함수가 더 오래 유지되는 경우,
// 외부 함수 밖에서 내부함수가 호출되더라도 외부함수의 지역 변수에 접근할 수 있는데
// 이러한 함수를 클로저(Closure)라고 부른다.
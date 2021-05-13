// apply/call/bind 호출
/*
    apply() 메소드의 대표적인 용도는 arguments 객체와 같은 유사 배열 객체에 배열 메소드를 사용하는 경우이다.
    arguments 객체는 배열이 아니기 때문에 slice() 같은 배열의 메소드를 사용할 수 없으나 apply() 메소드를 이용하면 가능하다.
*/
function convertArgsToArray() {
    console.log(arguments); // [Arguments] { '0': 1, '1': 2, '2': 3 }
    // arguments 객체를 배열로 변환
    // slice: 배열의 특정 부분에 대한 복사본을 생성

    var arr = Array.prototype.slice.apply(arguments); // arguments.slice
    // var arr = [].slice.apply(arguments);

    console.log(arr); // [ 1, 2, 3 ]
    return arr;
}

convertArgsToArray(1, 2, 3);
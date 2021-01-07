// object operator 관계연산 객체 비교 [객체의 속성값을 하나씩 비교하여 같은 객체인지 아닌지를 비교]

const ObjectOperator = (x,y) => {
    // 각 속성 이름을 추출
    var xValue = Object.getOwnPropertyNames(x);
    var yValue = Object.getOwnPropertyNames(y);

    if(xValue.length !== yValue.length) {
        return false; // 각 속성 이름의 길이가 같지 않다면 당연히 같은 객체가 아님.
    }

    // 각 속성 이름의 길이가 같다면, 더 들어가 값을 하나씩 추출 & (반복문 사용)
    for(var i=0; i<xValue.length; i++) {    // array 객체까지 고려해야 하기 때문에 xValue.length 사용
        var ValueOperator = xValue[i];      // xValue[1], xValue[2] ....
        // 하나씩 비교
        if(x[ValueOperator] !== y[ValueOperator]) {
            return false;
        }

    }
    // 위의 케이스가 아니라면 true (같은 객체임을) 리턴
    return true;
}
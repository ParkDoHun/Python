/* 프로토타입 : Prototype chain */

var student = {
    name: 'Park',
    score: 95
}

// Object.prototype.hasOwnProperty()
console.log(student.hasOwnProperty('name'));  // true

/*
student 객체는 hasOwnProperty 메소드를 가지고 있지 않으므로 에러가 발생하여야 하나 정상적으로 결과가 출력되었다. 
이는 student 객체의 [[Prototype]]이 가리키는 링크를 따라가서 student 객체의 부모 역할을 하는 프로토타입 객체(Object.prototype)의 메소드 hasOwnProperty를 호출하였기 때문에 가능한 것이다.
*/

var student1 = {
    name: 'Park',
    score: 95
}

console.dir(student);               // { name: 'Park', score: 95 }
console.log(student.hasOwnProperty('name'));    // ture
console.log(student.__proto__ === Object.prototype);    // true
console.log(Object.prototype.hasOwnProperty('hasOwnProperty'));  // true
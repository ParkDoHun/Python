/* 프로토타입 : constructor 프로퍼티 */
// constructor 프로퍼티는 객체의 입장에서 자신을 생성한 객체를 가리킨다.

function Person(name) {
    this.name = name;
}

var foo = new Person('Park');

// Person() 생성자 함수에 의해 생성된 객체를 생성한 객체는 Person() 생성자 함수이다.
console.log(Person.prototype.constructor === Person); // true

// foo 객체를 생성한 객체는 Person() 생성자 함수이다.
console.log(foo.constructor === Person);            // ture

// Person() 생성자 함수를 생성한 객체는 Function() 생성자 함수이다.
console.log(Person.constructor === Function);       // true


/*
foo 객체를 생성한 객체는 Person() 생성자 함수이다. 
이때 foo 객체 입장에서 자신을 생성한 객체는 Person() 생성자 함수이며, foo 객체의 프로토타입 객체는 Person.prototype이다. 
따라서 프로토타입 객체 Person.prototype의 constructor 프로퍼티는 Person() 생성자 함수를 가리킨다.
*/
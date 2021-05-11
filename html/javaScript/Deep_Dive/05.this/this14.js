// apply/call/bind 호출

var Person = function(name) {
    this.name = name;
};

var foo = {};

// apply 메소드는 생성자함수 Person을 호출한다.
// 이때 this에 객체 foo를 바인딩한다.
Person.apply(foo, ['name']);

console.log(foo);   // { name: 'name' }

/*
빈 객체 foo를 apply() 메소드의 첫번째 매개변수에, argument의 배열을 두번째 매개변수에 전달하면서 Person 함수를 호출하였다.
이때 Person 함수의 this는 foo 객체가 된다. Person 함수는 this의 name 프로퍼티에 매개변수 name에 할당된 인수를 할당하는데
this에 바인딩된 foo 객체에는 name 프로퍼티가 없으므로 name 프로퍼티가 동적 추가되고 값이 할당된다.
*/
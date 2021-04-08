// 7. 함수의 다양한 형태 : 내부 함수


    /*
    함수 내부에 정의된 함수를 내부함수(Inner function)라 한다.
    내부함수 child는 자신을 포함하고 있는 부모함수 parent의 변수에 접근할 수 있다. 
    하지만 부모함수는 자식함수(내부함수)의 변수에 접근할 수 없다.
    */

    function parent(param) {
      var parentVar = param;
      function child() {
        var childVar = 'lee';
        console.log(parentVar + ' ' + childVar); // Hello lee
      }
      child();
      console.log(parentVar + ' ' + childVar);
      // Uncaught ReferenceError: childVar is not defined
    }
    parent('Hello');

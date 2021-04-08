// 7. 함수의 다양한 형태 : 재귀 함수

    // 재귀 함수는 자기 자신을 호출하는 함수이다.
    // 피보나치 수열
    // 피보나치 수는 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
    // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
    function fibonacci(num) {
        if (num < 2) {
            return num;
        } else {
            
        } return fibonacci(num - 1) + fibonacci(num - 2);
    }

    console.log(fibonacci(0)); // 0
    console.log(fibonacci(1)); // 1
    console.log(fibonacci(2)); // 1
    console.log(fibonacci(3)); // 2
    console.log(fibonacci(4)); // 3
    console.log(fibonacci(5)); // 5
    console.log(fibonacci(6)); // 8

    console.log('');
    // 팩토리얼
    // 팩토리얼(계승)은 1부터 자신까지의 모든 양의 정수의 곱이다.
    // n! = 1 * 2 * ... * (n-1) * n
    function factorial(num) {
        if (num < 2) {
            return 1;
        } else {
            return factorial(num - 1) * num;
        }
    }

        console.log(factorial(0)); // 1
        console.log(factorial(1)); // 1
        console.log(factorial(2)); // 2
        console.log(factorial(3)); // 6
        console.log(factorial(4)); // 24
        console.log(factorial(5)); // 120
        console.log(factorial(6)); // 720


        /*
        재귀 함수는 자신을 무한히 연쇄 호출하므로 호출을 멈출 수 있는 탈출 조건을 반드시 만들어야 한다. 
        탈출 조건이 없는 경우, 함수가 무한 호출되어 stackoverflow 에러가 발생한다.
        */
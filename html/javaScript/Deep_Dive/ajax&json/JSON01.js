const o = { name: 'Lee', gender: 'male', age: 20, test1: 11, test2: 33 };

// 객체 => JSON 형식의 문자열
const strObject = JSON.stringify(o);
console.log(typeof strObject, strObject);
console.log('----------하단은 테스트----------')
// string {"name":"Lee","gender":"male","age":20}

// 객체 => JSON 형식의 문자열 + prettify
const strPrettyObject = JSON.stringify(o, null, 2);
console.log(typeof strPrettyObject, strPrettyObject);

// 숫자 거르는 필터
function filter(key, value) {
    return typeof value === 'number'? undefined : value;
}


const strFilteredObject = JSON.stringify(o, filter, 2); // 2 : 2칸 들여쓰기
console.log(typeof strFilteredObject, strFilteredObject);

const arr = [1, 5, 'false'];

// 배열객체 => 문자열
const strArray = JSON.stringify(arr, null, 2);
console.log(typeof strArray, strArray);

// 문자를 대문자로 변환하는 필터
function replaceToUpperFilter(key, value) {
    return value.toString().toUpperCase();
}

// 배열 객체 => 문자열 + replace
const strFileredArray = JSON.stringify(arr, replaceToUpperFilter, 2);
console.log(typeof strFileredArray, strFileredArray)
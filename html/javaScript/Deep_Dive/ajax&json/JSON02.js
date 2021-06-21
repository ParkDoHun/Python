const o = {name: 'Park', gender: 'male', age: 25};

// 객체 => JSON 형식 문자열
const strObj = JSON.stringify(o, null, 2);
console.log(typeof strObj, strObj);
/*
string {
  "name": "Park",
  "gender": "male",
  "age": 25
}
*/

const arr = [1, 5, 'false'];

// 배열 객체 => 문자열
const strArray = JSON.stringify(arr);
console.log(typeof strArray, strArray);
// string [1,5,"false"]

console.log('--------------------parse---------------------');


// JSON 형식의 문자열 => 객체
const obj = JSON.parse(strObj);
console.log(typeof obj, obj);
// object { name: 'Park', gender: 'male', age: 25 }

// 문자열 => 배열 객체
const objArray = JSON.parse(strArray);
console.log(typeof objArray, objArray);
// object [ 1, 5, 'false' ]
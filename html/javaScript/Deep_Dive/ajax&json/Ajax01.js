// XMLHttpRequest
const xhr = new XMLHttpRequest();

xhr.open('GET', '/users');

// POST타입, json으로 전송하는 경우
// xhr.open('POST', '/users');
xhr.send();

xhr.send(null);

xhr.setRequestHeader('Content-type', 'application/json');

const data = {id:3, title: 'JavaScript', author: 'Park', price: 10000};
xhr.send(JSON.stringify(data, null, 2));

xhr.open('POST', '/users');

CharacterData.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')

const data1 = {title: 'JavaScript', author: 'Park', price: 10000};

xhr.send(Object.keys(data1).map(key => `${key}=${data1[key]}`).join('&'));

xhr.setRequestHeader('Accept', 'application/json')
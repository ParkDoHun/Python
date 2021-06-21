const todos = [
    {id: 1, content: 'HTML', completed: true},
    {id: 2, content: 'CSS', completed: true},
    {id: 3, content: 'JS', completed: false}
];

const str = JSON.stringify(todos, null, 2);
console.log(typeof str, str);

console.log('------------parse-------------------')

const parsed = JSON.parse(str);
console.log(typeof parsed, parsed);



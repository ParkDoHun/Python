var arr = [];

for (var i = 0; i < 5; i++){
  arr[i] = (function (id) { // 1
    return function () {
      return id; // 2
    };
  }(i)); // 3
}

for (var j = 0; j < arr.length; j++) {
  console.log(arr[j]()); // 0 1 2 3 4
}
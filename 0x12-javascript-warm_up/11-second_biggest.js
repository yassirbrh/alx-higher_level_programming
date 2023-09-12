#!/usr/bin/node
const arr = [];
for (let elem in process.argv) {
  if (!isNaN(parseInt(process.argv[elem]))) {
    arr.push(parseInt(process.argv[elem]));
  } else {
    elem = 0;
  }
}
for (let i = 0; i < arr.length; i++) {
  let max = i;
  for (let j = i + 1; j < arr.length; j++) {
    if (arr[max] < arr[j]) {
      max = j;
    }
  }
  if (arr[max] !== arr[i]) {
    let tmp = arr[i];
    arr[i] = arr[max];
    arr[max] = tmp;
    tmp = 0;
  }
}
if (arr.length < 2) {
  console.log(0);
} else {
  console.log(arr[1]);
}

#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }
  if (number === 1 || number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(parseInt(process.argv[2])));

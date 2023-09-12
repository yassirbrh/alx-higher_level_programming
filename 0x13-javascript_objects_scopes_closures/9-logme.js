#!/usr/bin/node
let numberAcc = 0;
exports.logMe = function (item) {
  console.log(numberAcc + ' : ' + item);
  numberAcc++;
};

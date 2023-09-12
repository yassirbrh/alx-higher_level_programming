#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const newList = [];
  for (let i = len - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  len = 0;
  return newList;
};

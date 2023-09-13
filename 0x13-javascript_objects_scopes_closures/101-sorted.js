#!/usr/bin/node
const dict = require('./101-data.js').dict;
const ids = [];
const newDict = {};
for (const key in dict) {
  if (ids.indexOf(dict[key]) === -1) {
    ids.push(dict[key]);
  }
}
ids.sort((a, b) => a - b);
for (let i = 0; i < ids.length; i++) {
  const arr = [];
  for (const key in dict) {
    if (ids[i] === dict[key]) {
      arr.push(key);
    }
  }
  newDict[ids[i].toString()] = arr;
}
console.log(newDict);

#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let shape = '';
      for (let j = 0; j < this.height; j++) {
        shape += c;
      }
      console.log(shape);
    }
  }
}
module.exports = Square;

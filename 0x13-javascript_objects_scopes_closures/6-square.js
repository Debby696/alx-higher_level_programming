#!/usr/bin/node

const prevSquare = require('./5-square.js');

class Square extends prevSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += c;
        y++;
      }

      console.log(myVar);
    }
  }
}
module.exports = Square;

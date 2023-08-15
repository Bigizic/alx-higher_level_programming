#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.wh = size;
  }

  charPrint (c) {
    let i = 0;
    let word = '';
    if (c) {
      for (i = 0; i < this.wh; i++) {
        word = c.repeat(this.wh);
        console.log(word);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;

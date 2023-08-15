#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    let word = '';
    if (c === undefined) {
      c = 'X';
    }

    for (i = 0; i < this.height; i++) {
      word = c.repeat(this.width);
      console.log(word);
    }
  }
}

module.exports = Square;

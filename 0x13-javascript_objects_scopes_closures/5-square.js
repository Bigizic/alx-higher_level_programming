#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/* class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return (0);
    }
    if (w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let word = '';
    for (i = 0; i < this.height; i++) {
      word = 'X'.repeat(this.width);
      console.log(word);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
} */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

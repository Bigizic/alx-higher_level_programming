#!/usr/bin/node

class Rectangle {
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
}

module.exports = Rectangle;

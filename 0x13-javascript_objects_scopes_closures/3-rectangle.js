#!/usr/bin/node
// class Rectangle that defines a rectangle
// With an instance method called print()

class Rectangle {
  constructor (w, h) {
    if (w && h && w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;

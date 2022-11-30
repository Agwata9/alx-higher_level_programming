#!/usr/bin/node
// a class Rectangle that defines a rectangle:
// if w or h is equal to 0 or -ve, create an empty object

class Rectangle {
  constructor (w, h) {
    if (w && h && w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;

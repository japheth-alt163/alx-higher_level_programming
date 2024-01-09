#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is equal to 0 or not a positive integer
      this.width = undefined;
      this.height = undefined;
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    // Exchange the width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Multiply the width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

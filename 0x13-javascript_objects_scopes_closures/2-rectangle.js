#!/usr/bin/node
module.exports = class Rectangle {
  contructor (w, h) {
    if (w > 0 || h > 1) {
      this.width = w;
      this.height = h;
    }
  }
};

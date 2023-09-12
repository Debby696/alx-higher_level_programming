#!/usr/bin/node
/**
 * Square class that inherits from rectangle class
 * Here, it calls the parent class' constructor with size
 *  provided for the Rectangle's width and height
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.name = "Square";
  }
}
module.exports = Square;

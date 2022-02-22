//super
"use strict";
class Car {
    constructor(brand) {
      console.log("I am from car constructor 5");
      this.carname = brand;
    }
    show1() {
      return 'I have a ' + this.carname;
    }
  }
class Model extends Car {
    constructor(brand, model) {
      console.log("I am from model constructor 13");
      super(brand);
      console.log("I am from model constructor 15");
      this.model = model;
    }
    show2() {
      return super.show1() + ', it is ' + this.model;
    }
}
let mycar = new Model("BMW", "Q3");
console.log(mycar.show2());
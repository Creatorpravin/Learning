//super
"use strict";
class Car {
    constructor(brand) {
      this.carname = brand;
    }
    show1() {
      return 'I have a ' + this.carname;
    }
  }
class Model extends Car {
    constructor(brand, model) {
      super(brand);
      this.model = model;
    }
    show2() {
      return super.show1() + ', it is ' + this.model;
    }
}
let mycar = new Model("BMW", "Q3");
console.log(mycar.show2());
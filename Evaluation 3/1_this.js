"use strict";
let a = 10;
//this inside arrow function
let b = () => {
    console.log(this);
    console.log(this.a);
}
b();

//this inside object
let obj = {
    myMethod:() => {
        console.log(this);
        console.log(this.a);
    }
};
obj.myMethod();

//this access inside value of object
let myObject = {
    a:20,
    myArrowFunction: null,
    myMethod: function () {
       this.myArrowFunction = () => { console.log(this.a) };
    }
};   
myObject.myMethod(); // this === myObject

myObject.myArrowFunction(); // this === myObject

let myArrowFunction = myObject.myArrowFunction;
myArrowFunction(); //this === myObject
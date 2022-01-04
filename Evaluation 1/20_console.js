"use strict"
//console.log
console.log("Hello world!");//Hello world!
const myObj = {firstname:"Praveen", lastname:"Kumar"};
console.log(myObj);
//console.dir
let x = {property: 1, prop1: 2, method: function(){}};
console.dir(x);
let user = "";
//console.count
function greet() {
  console.count(user);
  return user;
}

user = "praveen";
greet();
user = "kumar";
greet();
greet();
console.count("kumar");

//console.table
function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  
  var arun = new Person("Arun", "Pandian");
  var dinesh = new Person("Dinesh", "Kumar");
  var bala = new Person("Bala", "Subramani");
  
  console.table([arun, dinesh, bala]);
// console.time/timeLog/timeEnd
console.time("answer time");
console.timeLog("answer time");
console.timeEnd("answer time");
//console.trace
function foo() {
    function bar() {
      console.trace();
    }
    bar();
  }
    foo();

//console.group()/console.groupEnd()
console.log("This is the outer level");
console.group();
console.log("Level 2");
console.group();
console.log("Level 3");
console.warn("More of level 3");
console.groupEnd();
console.log("Back to level 2");
console.groupEnd();
console.log("Back to the outer level");
//console.assert
const errorMsg = 'the # is not even';
for (let number = 2; number <= 5; number += 1) {
    console.log('the # is ' + number);
    console.assert(number % 2 === 0, {number: number, errorMsg: errorMsg});
}

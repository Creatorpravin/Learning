"use strict";
let number = "";
let count=1;
for (let i = 1;i<5;i++) {
  for (let j = 1;j<= 5 - i;j++){
    number += " ";
  }
  for (let k = 0; k < 2*i-i ; k++) {
    number += count;
    count++;
    number += " ";
  }
  number += "\n";
}
console.log(number);
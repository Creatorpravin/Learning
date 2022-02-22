"use strict"
function countSheep() {
    console.log(1);
    console.log(2);
    console.log(3);
    return "ZZZzzzzz...";
    // we never reach this point
    console.log(4);
    console.log(5);
}
console.log(countSheep());
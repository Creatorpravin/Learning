"use strict"
const check = function(value){
    console.log((value +"") ==value);
    console.log((value +"") ===value);

}
check(25);//call the function
//work with strings
console.log("yavar"==new String ("yavar"));//true
console.log("yavar"===new String ("yavar"));//false

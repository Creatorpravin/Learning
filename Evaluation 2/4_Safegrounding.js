"use strict";
let obj = {};
let f = function(){return "This is function";}
(typeof func == "function")?console.log(func()):console.log("This is not function");
function myFunction(func){     
}   
myFunction(obj);     //pass object instead of function 
myFunction(f); //pass function 
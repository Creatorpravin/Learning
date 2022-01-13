"use strict";
//'this' inside function
var thisFunction = function () {
    return this;
};
var obj = new thisFunction();
console.log(obj);
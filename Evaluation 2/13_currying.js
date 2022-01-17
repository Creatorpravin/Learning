"use strict";
const volume=function(a) {
    return function(b) {
       return function(c) {
          return a * b * c;
       };
    };
}
 console.log(volume(2)(4)(6));
const h=volume(2)(4);
 console.log(h(6));
const w=volume(2);
 const y = w(4);
console.log(h(6));

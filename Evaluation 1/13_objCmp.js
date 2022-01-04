"use strict";
var a={id: 1, name: "edison"};
var b={id: 1, name: "edison"};
var c={id: 1, name: "edison"};
var d={id: 2, name: "edison"};
function objcmp(x,y){
    let A=Object.getOwnPropertyNames(x);
    let B=Object.getOwnPropertyNames(y);
    if(A.length!=B.length)
      return false;
    for(let i=0;i<A.length;i++){
         let propName=A[i];
         if(x[propName]!==y[propName])
           return false;
     } 
     return true;
}
console.log(objcmp(a,b));     //true
console.log(objcmp(c,d));     //false
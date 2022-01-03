"use strict"
let arr1=[1,2,9,3,5,1,4,5],arr2 = [11,54,70,40];
function merge(){
let merge=[...arr1,...arr2];
 return merge;
}
console.log(merge());
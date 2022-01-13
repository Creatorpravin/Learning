"use strict";
const arr1 = [2001,2002,2003,2004,2005];
const arr2 = [2003,2005,2006,2007];
function commonNumber(arr1, arr2) {
    let common = []; 
    for (let i in arr1) {
      for (let j in arr2) {
        if (arr1[i] === arr2[j]) { 
          common.push(arr2[j]); 
        }
      }
    }
   console.log(common); 
}
commonNumber(arr1, arr2); 
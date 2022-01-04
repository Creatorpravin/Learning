"use strict"
function reverseString(Str){
    if (typeof Str === 'string'){
     let reversed = '';
    for (let c of Str) {
        reversed = c + reversed;
    }
    console.log(reversed);
  }else{
      console.log(Str,"Not a string");
  }
}
reverseString("Yavar technologies");
/*//using Inbuilt function
let str = 'yavar';
let reverse = [...str].reverse().join('');
console.log(reverse);*/

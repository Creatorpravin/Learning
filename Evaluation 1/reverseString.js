"use strict"
function reverseString(String){
    let reversed = '';
    for (let c of String) {
        reversed = c + reversed;
    }
    console.log(reversed);
}
reverseString("yavar technologies");
/*//using Inbuilt function
let str = 'yavar';
let reverse = [...str].reverse().join('');
console.log(reverse);*/

"use strict";
////give input range find number of zero
const start = 1;
const end = 50;
//convert input value to string
const startConvertToString = start + "" ;
const endConvertToString = end + "" ;
// check if type of value is number or not 
if(typeof start === "number" && typeof end === "number" ){
   if(startConvertToString.indexOf(".") === -1 && endConvertToString.indexOf(".") === -1){
        let count = 0;
        for(let i = start ; i <= end ; i++ ){
            let numberToString = i + "" ;
            count += numberToString.split("0").length - 1;
        }
        console.log(count);
    }
    else{
        console.log("The float value not accepted"); 
    }
}
else{
    console.log("The string value not accepted");
}
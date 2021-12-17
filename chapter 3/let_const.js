let a = "global a";
let b = "global b";
 function x(){
     console.log("x();global b="+b);
     console.log("x();global a="+a);
     let a = 1;
 }
 x();
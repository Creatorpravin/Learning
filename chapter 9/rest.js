/*let arr = [1,2,3,4];
arr.map(print);
let arr1 = [...arr,5];
console.log(arr1);*/

/*let print = item => console.log(item);
 let f = (...item) => item.map(print);
 f(1, 2, 3, 4, 3); 

 function sum(...args){
 console.log(args);
 
 }
 sum(1,2,3,4);*/
 function print(a, ...args){
    console.log(a);
    console.log(args);
  }
  print(...[1,2,3],4,5);  //here it is ...spread
  //a=1
  // args =[2,3,4,5]
 
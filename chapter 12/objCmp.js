let a = [1,2];
let b = [1,2];
let c = [5,5];
function is_array(value) {
    return typeof value.reduce=="function"&&
           typeof value.filter=="function"&&
           typeof value.map=="function"&&
           typeof value.length=="number";
}
function arrcmp(a,b){
    // one or more values are not arrays:
    if(!(is_array(a)&&is_array(b)))
     return false;
   //Not equal by length
   if(a.length != b.length)
   return false;
   //compare by value
   for(let i=0;i<a.length;i++)
   if(i[a]!==b[i])
   return false;
   //All test passed: array a and b are equal
return true;

}
function objcmp(a,b){
    //copy properties into A and B
    let A=Object.getOwnPropertyNames(a);
    let B=Object.getOwnPropertyNames(b);
    if(A.length != B.length)
     return false;
    
     for (let i=0;i<A.length;i++){
         let propName=A[i];
         let p1 = a[propName];
         let p2 = b[propName];
         
         if(is_array(p1)&&is_array(p2)){
             if(!arrcmp(p1, p2))
              return false;

         } else
         if(p1.constructor === Object &&
            p2.constructor === Object){
                if(!objcmp(p1, p2))
                  return false;
            } else if (p1 !== p2)
             return false;

     }

   return true;
}
console.log(objcmp(a,b))//true
console.log(objcmp({a:{b:12}},{a:{b:12}}));//true
console.log(objcmp({a:{b:12}},{a:{b:13}}));//false
console.log(objcmp({a:function(){}},{a:function(){}}));//false

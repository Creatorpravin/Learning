"use strict"
const oddEven= function(value){
    let even=0,odd=0;
    for(let i=0;i<=value;i++){
if(i % 2 == 0) {
    even = even + i;
}

else {
    odd = odd + i;
}

}
console.log("The sum of even numbers:",even);
console.log("The sum of odd numbers:",odd);
};
oddEven(100);

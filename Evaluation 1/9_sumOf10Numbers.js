"use strict"

function sum(number){
    if (!isNaN(number)){
let sum = 0, i = 1;
while(i <= number) {
    sum += i;
    i++;
}
   
console.log('The sum of 10 natural numbers:', sum);
}else{
    console.log('Not a valid number');
}

}
sum('loop');
sum(10);
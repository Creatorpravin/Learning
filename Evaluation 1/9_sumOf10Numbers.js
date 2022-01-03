"use strict"

function sum(number){
let sum = 0, i = 1;
while(i <= number) {
    sum += i;
    i++;
}

console.log('The sum of 10 natural numbers:', sum);
}
sum(10);
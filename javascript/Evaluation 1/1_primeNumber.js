"use strict"
// check if a number is prime or not



let output;
//const number = 23;
const primeNumber = function (number){
    let isPrime = true;
// check if number is equal to 1
if (number === 1 || typeof number === "string"|| number < 1) {
    output = "Enter the valid value";
}

// check if number is greater than 1
else if (number > 1) {

    // looping through 2 to number-1
    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) {
        output = `${number} is a prime number`;
    } else {
        output = `${number} is a not prime number`;
    }
}

// check if number is less than 1
else {
    output = "The number is not a prime number.";
}
return output;
}
console.log(primeNumber("two"));
console.log(primeNumber(1));
console.log(primeNumber(2));
console.log(primeNumber(3));
console.log(primeNumber(4));
console.log(primeNumber(5));
console.log(primeNumber(6));
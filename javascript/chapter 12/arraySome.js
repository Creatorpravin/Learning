let number = [0,10,2,3,4,5,6,7];
let condition = value => value < 10;
let some = number.some(condition);
let every = number.every(condition);
console.log(some);
console.log(every);
let miles = [50,6,9,20,15,30];
const R =(accumulator,value) => accumulator + value;
const result = miles.reduce(R);
console.log(result);
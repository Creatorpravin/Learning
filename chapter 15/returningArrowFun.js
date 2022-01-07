let boomerang = a => "returns";
let karma = a => {return "returns";}
//let prayer = a => {return random()>=0.5};
let time = a => {"won't return";}
console.log(boomerang(1));//"returns"
console.log(karma(1));//"returns"
console.log(time(1));//[undefined]
//]
 let a = [1];
 console.log(a.map(boomerang));//"returns"
 console.log(a.map(karma));//"returns"
 console.log(a.map(time));//[undefined]
//  console.log(y);
//   console.log(z);
  //prayer("Make me understand JavaScript")

function sumTwoSmallestNumbers(numbers) {  
  let a=numbers.sort((a,b)=>a-b)//use to make is descending order
  return a[0]+a[1]
 }

console.log(sumTwoSmallestNumbers([5, 8, 12, 19, 22]));
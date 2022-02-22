//const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function getEvenNumbers(numbersArray){
    
     const even = numbersArray.filter(number => {
     return number % 2 === 0;
      });
    
      return even;
}
//const arr = [2,4,5,6];

console.log(getEvenNumbers([2,4,5,6]));

// const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// const even = arr.filter(number => {
//   return number % 2 === 0;
// });

// console.log(even); // 👉️ [2, 4, 6, 8]

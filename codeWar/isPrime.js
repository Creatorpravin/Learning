// function isPrime(num) {
//     for(var i = 2; i < num; i++)
//       if(num % i === 0) return false;
//     return num > 1;
//   }

  console.log(isPrime(1));
  console.log(isPrime(25));
  console.log(isPrime(71));
  console.log(isPrime(11));

  function isPrime(num) {
    if (num < 2) return false;
    const limit = Math.sqrt(num);
    for (let i = 2; i <= limit; ++i) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }
function sortArray(array) {
    const odd = array.filter(x => x % 2).sort((a, b) => a - b);
    return array.map(x => (x % 2 ? odd.shift() : x)); //shift() removes the first item of an array:
  }

console.log(sortArray([5, 8, 6, 3, 4]));
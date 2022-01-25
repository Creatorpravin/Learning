

function findUniq(arr) {
    return +arr.filter( (value) => { return arr.indexOf(value) == arr.lastIndexOf(value) } );
  }
console.log(findUniq([ 1, 8, 4, 4, 6, 1, 8 ]));
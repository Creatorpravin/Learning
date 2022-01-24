//method 1
function findShort(s){
     return Math.min(...s.split(" ").map (s => s.length));
}

console.log(findShort("The quick brown fox jumped over the lazy dog"));
  //method 2
  function findShortestWord(str) {
    //var words = str.split(' ');
    var shortest =str.split(' ').reduce((shortestWord, currentWord) => {
      return currentWord.length < shortestWord.length ? currentWord : shortestWord;
    },);
    return shortest.length;
  }
  console.log(findShortestWord("The quick brown fox jumped over the lazy dog"));
  //method 3
  function findShort(s){
    var arr = s.split(' ');
    var smallest = arr[0];
    for (var i = 0; i < arr.length; i++) {
      if(arr[i].length < smallest.length){
        smallest = arr[i];
      }
    }
    return smallest.length;
  }
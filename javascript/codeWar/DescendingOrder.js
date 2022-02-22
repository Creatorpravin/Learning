
function descendingOrder(n){
    //The parseInt() function parses a string argument and returns an integer of the specified
    return parseInt((n+'').split('').sort().reverse().join(''))
}
console.log(descendingOrder(42145));
// var a = [2,5,6,8,6];
// console.log(a.sort());
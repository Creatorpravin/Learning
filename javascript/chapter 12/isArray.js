function isArray(value){
    return typeof value.reduce == "function" &&
    typeof value.filter == "function" &&
    typeof value.map == "function" &&
    typeof value.length == "number" ;


}
//Test the function 
console.log(isArray(1));//false
console.log(isArray("string"));//false
console.log(isArray({a:1}));//false
console.log(isArray(true));//false
console.log(isArray([]));//true
console.log(isArray([1,2,3,4,5]));//true

function fun(func){
    console.log(func());//call the function by it's parameters name

}
var array = [];
var f = function() {return true}
fun(array);//pass array instead of function

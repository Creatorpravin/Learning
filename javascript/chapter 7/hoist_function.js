//hoisting applies to function name
fun();                        //function1
function fun(){
    console.log("function1");
}
//variable name will take precedence over function definitions
function fun(){
    console.log("function1");
}
var fun=function(){
    console.log("function2");
}
fun();
//function that was defined last will take precedence.
function fun(){
    console.log("function1");
}
function fun(){
    console.log("function2");
}
fun();
//Defining Variables Inside Function Scope
function fun(){
    var ap=1;
}
console.log(ap);  //ReferenceError: ap is not defined


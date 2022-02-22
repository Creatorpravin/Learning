//var 
x = 5;                         // Assign 5 to x                    
console.log(x);                //5
var x;                         // Declare x

//let
y = 5;                         // Assign 5 to y                   
console.log(y);                // ReferenceError: Cannot access 'y' before initialization
let y;                         // Declare y

//const
z = 5;                          // Assign 5 to z
console.log(z);                 // SyntaxError: Missing initializer in const declaration
const z;                        // Declare z

//define a variable inside a block scope?
console.log(apple);              //undefined
{
var apple=1;
}
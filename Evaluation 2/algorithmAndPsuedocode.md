# JavaScript Evaluation-2

## 1. Display prime numbers 1 to 200?

**Algorithm**
- Step 1. Use strict mode as public. Declare the function with partameter.
- 
**Psuedocode**

**Code**

```javascript

"use strict"
function primeNumber(value){
    const numberToString= value + "";
 if(typeof value === "number" && value > 2 && numberToString.indexOf(".") === -1 ){
      for (let counter = 0; counter <= value; counter++) {

    var notPrime = false;
    for (var i = 2; i <= counter; i++) {
        if (counter%i===0 && i!==counter) {
            notPrime = true;
        }
    }
    if(counter >= 2)
    if (notPrime === false) {
        
                console.log(counter);
    }
}

}else
    console.log("Enter the valid value");

}

primeNumber(200);


```
primeNumber(200);

*output*
```console
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
```

## 2. From two sorted arrays, how would you find the common numbers?
**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
const array1 = [1,2,3,4,5];
const array2 = [2,4,8,10,15];
function commonNumber(array1, array2) {
    let common = []; 
    for (let i = 0; i < array1.length; i++) {
      for (let j = 0; j < array2.length; j++) {
        if (array1[i] === array2[j]) { 
          common.push(array1[i]); 
        }
      }
    }
   console.log(common); 
}
commonNumber(array1, array2); 
```


*Output:*

```console
[ 2003, 2005 ]
```

## 3. Explain about function Anatomy, Anonymous function and Assigning function to a variable with an example?

**function Anatomy :**

- A function is a sequence of instructions within a larger program.
- It consist of the function keyword and following by name of the function.
- The function can have 0, 1 or many parameters. The order of these paramaters determine the function's signature. The number of paramaters is called arity.
- In JavaScript, a function always returns a value. The default return value of a function is undefined.
 - The return statement ends function execution and specifies a value to be returned to the function caller.

**Algorithm**



**Psuedocode**

**code**
```javascript
"use strict"
function countSheep() {
    console.log(1);
    console.log(2);
    console.log(3);
    return "ZZZzzzzz...";
    // we never reach this point
    console.log(4);
    console.log(5);
}
countSheep();
```

*Output:*
```console
1
2
3
ZZZzzzzz...
```
**Anonymous function :**
 - Anonymous functions are functions without names.
- This anonymous function is used in an assigned expression. This combination is called an "anonymous function expression"
- Anonymous functions can be used as an argument to other functions or as an immediately invoked function execution.

**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict"
setTimeout(function () {
    console.log("I am anonymous function");
}, 2000);
```

*Output:*
```console
I am anonymous function 
```

**Assigning function to a variable :**
  - A function expression can be stored in a variable.
 - An anonymous function is not accessible after its initial creation, 
 - It can only be accessed by a variable it is stored in as a function as a value.

**Algorithm**


**Psuedocode**

**code**
```javascript
const x = function (a, b) {return a * b};
console.log(x(2,4));
```
*Output:*
```console
8
```
## 4. Show an example ofSafegrounding function parameters?

 - The solution is to safeguard the value by checking its type.  
  - JavaScript has a built-in directive typeof that we can use before calling the function.
**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
let obj = {};
let f = function(){return "This is function";}
(typeof func == "function")?console.log(func()):console.log("This is not function");
function myFunction(func){     
}   
myFunction(obj);     //pass object instead of function 
myFunction(f); //pass function 
```
*Output:*
```console
This is not function
This is function
```

## 5. Explain `this` keyword with an example?
 - The JavaScript this keyword refers to the object it belongs to. It refers to current object.
 - In a method, this refers to the owner object.
 - Alone, this refers to the global object.
 - In a function, this refers to the global object.

**Algorithm**




**Psuedocode**

**code**
```javascript
const x = 25;
function y(){
    var a = 35;
    console.log(a);
    console.log(this.a);
}
y();
console.log(this);
const test = {
          prop: 42,
          func: function() {
          return this.prop;
      },

    };
  console.log(test.func());
```

*Output:*
```console
35
undefined
{}
42

```

## 6. How ‘this’ inside the function and class?

**‘this’ inside the function**
 - In a function, this refers to the global object.

 - In a function, in strict mode, this is undefined.


**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
//'this' inside function
var thisFunction = function () {
    return this;
};
var obj = new thisFunction();
console.log(obj);
```

*Output:*
```console
thisFunction {}
```

**‘this’ inside the class**
 - This keyword is used inside of a class and refers to the current instance.
**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
//'this' inside class
class thisClass{
    constructor() {
      return this;
    }
}
let obj = new thisClass();
console.log(obj);
```
*Output:*
```console
thisClass {}
```

## 7. Difference between map, reduce and filter methods? With an example

**map**
 - The map() method creates a new array with the results of calling a function for every array element.

 - The map() method calls the provided function once for each element in an array, in order.

 - map() does not execute the function for empty elements.

 - map() does not change the original array.
**Algorithm**


**Psuedocode**

**code**
```javascript.
"use strict";
let twice = [1,2,3,4,5,6];
let resultTwice = twice.map(value => value * 2);
console.log(resultTwice);

```

*Output:*
```console
[ 2, 4, 6, 8, 10, 12 ]
```

**reduce**
 - The reduce() method reduces an array of values down to just one value. To get the output value, it runs a reducer function on each element of the array. 

**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
let total = [1,2,3,4,5,6,7,8];
let count = total.reduce((previous,current) => previous + current);
console.log(count);
```

*Output:*

```console
36

```
**filter**
- The filter() method creates a new array with all elements that pass the test implemented by the provided function.
- If the condition returns false, the element does not get pushed to the output array.


**Algorithm**



**Psuedocode**

**code**
```javascript
"use strict"
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter(word => word.length > 6);

console.log(result);
```

*Output:*
```console
[ 'exuberant', 'destruction', 'present' ]
```
## 8. Count Total number of zeros from 1 up to 50
**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
//give input range find number of zero
const start = 1;
const end = 50;
//convert input value to string
const startConvertToString = start + "" ;
const endConvertToString = end + "" ;
// check if type of value is number or not 
if(typeof start === "number" && typeof end === "number" ){
   if(startConvertToString.indexOf(".") === -1 && endConvertToString.indexOf(".") === -1){
        let count = 0;
        for(let i = start ; i <= end ; i++ ){
            let numberToString = i + "" ;
            count += numberToString.split("0").length - 1;
        }
        console.log(count);
    }
    else{
        console.log("The float value not accepted"); 
    }
}
else{
    console.log("The string value not accepted");
}
```

*Output:*
```console
5
```

## 9. The following array of numbers show the missing number? ([1,2,3,5,6])

**Algorithm**


**Psuedocode**

**code**
```javascript
var a = [1,2,3,5,6], count = Math.max(...a);
var missing = [];
for ( var i = 1; i <= count; i++ ) {
	if (a.indexOf(i) == -1) {
		missing.push(i);
	}
}
console.log(missing);
```


*Output:*

```console
[ 4 ]
```
## 10. Write a program for calculating age using Date of birth? (1990)

**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict"
function calAge(birthYear){
    const convertToString = birthYear + "";
if(typeof birthYear === "number" && convertToString.indexOf(".") === -1)    {
    const year = new Date();
    const currentYear = year.getFullYear();
    const age = currentYear - birthYear;
    console.log(age);
}else
 console.log("enter the valid value");
}
calAge(1990);
```
*Output:*
```console
32

```
## 11. In the Javascript function, what are the differences between call by value and reference?
**Algorithm**


**Psuedocode**

**code**

*Output:*

## 12. What is Arity in Javascript? 
Explain with a real time example.
**Algorithm**


**Psuedocode**

**code**

*Output:*

## 13. What is Currying in Javascript? Explain with a real time example.
**Algorithm**


**Psuedocode**

**code**

*Output:*

## 14. What is ES6?
**Algorithm**


**Psuedocode**

**code**

*Output:*

## 15. What is an anonymous function? Where do we use it? Why do we need it?
**Algorithm**


**Psuedocode**

**code**

*Output:*

## 16. List the differences between named function and assigning functions to variable with
examples
**Algorithm**


**Psuedocode**

**code**

*Output:*
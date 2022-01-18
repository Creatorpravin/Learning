# JavaScript Evaluation-2

## 1. Display prime numbers 1 to 200?

**Algorithm**
- Step 1. Use strict mode as public. Declare the function with partameter.
- Step 2. Check the validation of parameter value.
- Step 3. Assign false to a variable. Use for loop to increase the count.
- Step 4. Check the value of boolean with help of if condition.
- Step 5. Then print the value in console.
- Step 6. call the function with parameters

**Psuedocode**
```markdown
BEGIN
"use strict"
FUNCTION primeNumber(value)
   INIT numberToString= value + "";
  IF (typeof value === "number" && value > 2 && numberToString.indexOf(".") === -1 ) THEN
   FOR (let counter = 0; counter <= value; counter++) DO 
      INIT notPrime = false;
      FOR (var i = 2; i <= counter; i++) DO
        IF (counter%i===0 && i!==counter) THEN
          SET notPrime = true;
         ENDIF
        IF (counter >= 2) THEN
        IF (notPrime === false) THEN
          PRINT counteR
          ENDIF
        ENDIF
      ENDFOR
    ENDFOR
    ELSE
      PRINT "Enter the valid value"
FUNCTION CALL primeNumber(200);
```

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
- Step 1. Use strict mode globally. create two set of array.
- Step 2. Write a function commonNumber with parameters.
- Step 3. Declare an empty array.
- Step 4. Create for loop and nested for loop to iterate all the values in array.
- Step 5. Check the iterated values with if condition.
- Step 6. Then print the values.
- Step 7. Call the function with parameters.

**Psuedocode**
```markdown
BEGIN
"use strict"
INIT arr1 = [2001,2002,2003,2004,2005];
INIT arr2 = [2003,2005,2006,2007];
FUNCTION commonNumber(arr1, arr2) 
   INIT common = []; 
   FOR (let i in arr1) DO 
    FOR (let j in arr2) DO
     IF (arr1[i] === arr2[j]) THEN
      SET common.push(arr2[j])
     ENDIF
    ENDFOR
   ENDFOR   
 PRINT common
 END FUNCTION
FUNCTION CALL commonNumber(arr1, arr2)
  
```


**code**
```javascript

"use strict";
const arr1 = [2001,2002,2003,2004,2005];
const arr2 = [2003,2005,2006,2007];
function commonNumber(arr1, arr2) {
    let common = []; 
    for (let i in arr1) {
      for (let j in arr2) {
        if (arr1[i] === arr2[j]) { 
          common.push(arr2[j]); 
        }
      }
    }
   console.log(common); 
}
commonNumber(arr1, arr2); 
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
- Step 1. Use strict mode as global.
- Step 2. Declare a function and print some integer values.
- Step 3. return some values and again print some integer values.
- Step 4. Then call the function outside the scope.

**Psuedocode**
```markdown
"use strict"
FUNCTION countSheep() 
    PRINT (1)
    PRINT (2)
    PRINT (3)
    RETURN "ZZZzzzzz...";
    PRINT (4)
    PRINT (5)
FUNCTION END
FUNCTION CALL countSheep()
```

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
- Step 1. Use strict mode as global.
- Step 2. Declare a function without name within the setTimeout.
- Step 3. Print some statement in function.
- Step 4. Run the program.

**Psuedocode**

```markdown
BEGIN
"use strict"
FUNCTION setTimeout(function () 
    PRINT ("I am anonymous function")
, 2000);
```

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
- Step 1. Use Strict mode as global. Declare a function with parameter.
- Step 2. Assign function to a variable.
- Step 3. return the multiplication of values.
- Step 4. call the funciton  with varibale name and print it.


**Psuedocode**
```markdown
BEGIN 
"use strict"
INIT x = FUNCTION (a, b)
 RETURN a * b
 FUNCTION END 
PRINT(x(2,4))
```
**code**
```javascript
"use strict"
const x = function (a, b) {return a * b};
console.log(x(2,4));
```
*Output:*
```console
8
```
## 4. Show an example of Safegrounding function parameters?

 - The solution is to safeguard the value by checking its type.  
 - JavaScript has a built-in directive typeof that we can use before calling the function.

**Algorithm**
- Step 1. Use Strict mode as global. Declare a function and assingn to variable.
- Step 2. Then check the validation fo value using typeOf method using tenary operator.
- Step 3. Then call function with diffrent parameter values.

**Psuedocode**

```markdown
BEGIN
"use strict";
INIT obj = {};
INIT f = FUNCTION function()
              RETURN "This is function"
FUNCTION myFunction(func)
    TENARY(typeof func == "function")?console.log(func()):console.log("This is not function");
FUNCTION END    
   
FUNCTION CALL myFunction(obj)
FUNCTION CALL  myFunction(f)
```

**code**
```javascript
let obj = {};
let f = function(){return "This is function";}

function myFunction(func){  
    (typeof func == "function")?console.log(func()):console.log("This is not function");   
}   
myFunction(obj);     //pass object instead of function 
myFunction(f);
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
 - Step 1. Use Strict mode as global.
 - Step 2. Declare two functions one within primitive data and another within object.
 - Step 3. Print the variables with this keyword.
 - Step 4. Call the function 

**Psuedocode**

```markdown
BEGIN
INIT x = 25
FUNCTION y()
    INIT a = 35;
    PRINT(a)
    PRINT(this.a)
FUNCTION END
FUNCTION CALL y()
PRINT (this);
INIT test = {
          prop: 42,
          func: FUNCTION () 
                   RETURN this.prop;
          };
  PRINT FUNCTION CALL test.func()

```

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
 - It is reuse functions in different execution contexts. It means, a function once defined can be invoked for different objects using the this keyword.
 - In a function, in strict mode, this is undefined.


**Algorithm**
 - Step 1. Use Strict mode as global.
 - Step 2. Declare a function and assign to a variable.
 - Step 3. Return this in function.
 - Step 4. Create new constructor object for fucntion.
 - Step 5. Then print the object.


**Psuedocode**

```markdown
BEGIN
"use strict"
INIT thisFunction = FUNCTION () 
    RETURN this
INIT obj = new thisFunction()
PRINT(obj)
```

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
```consol.e
thisFunction {}
```

**‘this’ inside the class**

 - This keyword is used inside of a class and refers to the current instance.

**Algorithm**

- Step 1. Use Strict mode as global.
- Step 2. Create a class and create a object constructor in class.
- Step 3. Then return this.
- Step 4. Create a new object constructor to the class.
- Step 5. Call the object constructor.



**Psuedocode**

```markdown
BEGIN
"use strict";
CLASS thisClass
    constructor() 
        RETURN this 
INIT obj = new thisClass()
PRINT(obj)
```

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

- Step 1. Use Strict mode as global.
- Step 2. Create a array.
- Step 3. Use arrow function to work with map.
- Step 4. Do something with array and store in variable.
- Step 5. print the value.

**Psuedocode**
```markdown
BEGIN
"use strict"
INIT twice = [1,2,3,4,5,6]
INIT resultTwice = twice.map(value => value * 2)
PRINT(resultTwice);
```

**code**
```javascript

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
- Step 1. Use Strict mode as global.
- Step 2. Create a array assign to variable.
- Step 3. create arrow function for work with reduce.
- Step 4. Do something with previous value and converted to single value.
- Step 5. Print the value.

**Psuedocode**
```markdown
BEGIN
"use strict";
INIT total = [1,2,3,4,5,6,7,8];
INIT count = total.reduce((previous,current) => previous + current);
PTINT(count);
```
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
- Step 1. Use Strict mode as global.
- Step 2. Create a array assign to variable.
- Step 3. Create arrow function for work with filter.
- Step 4. Do some conditon to filter the values.
- Step 5. Print the value.


**Psuedocode**

```markdown
BEGIN
"use strict"
INIT words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present']

INIT result = words.filter(word => word.length > 6)

PRINT(result)
```

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

- Step 1. Use Strict mode as global.
- Step 2. Create two variables globally. Then convert it to string for validation of float
- Step 3. Validate it of number and float. Create a variable with 0.
- Step 4. Use for loop to iterate the number and convert it to string.
- Step 5. Split the number by 0 then make it count to a varibale.
- Step 6. Then print the value.

**Psuedocode**
```markdown
BEGIN
"use strict";
INIT start = 1;
INIT end = 50;
INIT startConvertToString = start + "" ;
INIT endConvertToString = end + "" ;
IF(typeof start === "number" && typeof end === "number" )THEN
   IF(startConvertToString.indexOf(".") === -1 && endConvertToString.indexOf(".") === -1)THEN
        INIT count = 0;
        FOR (let i = start ; i <= end ; i++ ) DO
            INIT numberToString = i + "" ;
            SET count += numberToString.split("0").length - 1;
        ENDFOR
        PRINT(count);
    ELSE
        PRINT("The float value not accepted"); 
    ENDIF
ELSE
    PRINT("The string value not accepted");
ENDIF

```

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
            //split the number by 0 and add length - 1 to count
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

- Step 1. Use Strict mode as global.
- Step 2. Create a array and use max method to get the max value in arrray.
- Step 3. Use math to generate numbers in array.
- Step 4. Use for loop to iterate the values in array.
- Step 5. Check the condition if it already exists or not.
- Step 6. Then push into new one and print it.


**Psuedocode**
```markdown
BEGIN
"use strict"
INIT a = [1,2,3,5,6], count = Math.max(...a);
INIT missing = [];
FOR ( var i = 1; i <= count; i++ ) DO
	IF (a.indexOf(i) == -1) 
		SET missing.push(i);
PRINT(missing)
```
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
- Step 1. Use Strict mode as global.
- Step 2. Create a function with a parameter of age.
- Step 3. Check the validation of the input.
- Step 4. Get today date by Date() and get the year from date.
- Step 5. Subract current year from birth year.
- Step 6. Call the function.

**Psuedocode**
```markdown
BEGIN
"use strict"
FUNCTION calAge(birthYear)
  INIT convertToString = birthYear + "";
IF(typeof birthYear === "number" && convertToString.indexOf(".") === -1)THEN
    INIT year = new Date();
    INIT currentYear = year.getFullYear();
    INIT age = currentYear - birthYear;
    PRINT(age);
ELSE
 PRINT("enter the valid value");
ENDIF 
FUNCTION END
FUNCTION CALL calAge(1990);
```

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

**Call by value**
 - Function arguments are always passed by value.
 - It copies the value of a variable passed in a function to a local variable.
 - Both these variables occupy separate locations in memory. Thus, if changes are made in a particular variable it does not affect the other one.
**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict"
let a = 5;
let b;
b = a;
//diffrent memory location
a = 3;
console.log(a);
console.log(b);
```

*Output:*

```console
3
5
```

**Call by referance**

 - In JavaScript, all objects interact by reference.
 - If an object is stored in a variable and that variable is made equal to another variable then both of them occupy the same location in memory.
 - Changes in one object variable affect the other object variable.

**Algorithm**


**Psuedocode**

**code**
```Javascript
 "use strict"
 // By reference (all objects (including functions))
 var c = { greeting : 'YAVAR' };
 var d;
 d = c;
 c.greeting = 'Yavar Tech Works';
 console.log(c);
 console.log(d);

```


*Output:*
```console
{ greeting: 'Yavar Tech Works' }
{ greeting: 'Yavar Tech Works' }
```

## 12. What is Arity in Javascript? 
Explain with a real time example.

 - The arity property used to return the number of arguments expected by the function.
 - You can access function’s arity via Function.length property.

**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
function Details(age,name,location){

}
let arity=Details.length;
console.log(arity);
```
*Output:*

```console
3
```

## 13. What is Currying in Javascript? Explain with a real time example.

 - Currying is a transformation of functions that translates a function from callable as f(a, b, c) into callable as f(a)(b)(c).
 - Currying doesn’t call a function. It just transforms it.



**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict";
const volume=function(a) {
    return function(b) {
       return function(c) {
          return a * b * c;
       };
    };
}
 console.log(volume(2)(4)(6));
const h=volume(2)(4);
 console.log(h(6));
const w=volume(2);
 const y = w(4);
console.log(h(6));
```

*Output:*

## 14. What is ES6?

 - ECMAScript 2015 is also known as ES6 and ECMAScript 6.
 - It brought several new features like, let and const keyword, rest and spread operators, template literals, classes, modules and many other enhancements to make JavaScript programming easier.
 - iterators and for...of loops
 - arrow function expression (() => {...})
 - let keyword for local declarations
 - const keyword for constant local declarations
 - Multi-line Strings
 - binary data
 - typed arrays
 - new collections (maps, sets and WeakMap)
 - promises
 - number and math enhancements
 - reflection
 - proxies (metaprogramming for virtual objects and wrappers)
 - template literals for strings.


## 15. What is an anonymous function? Where do we use it? Why do we need it?
**Anonymous function :**

- Anonymous functions are functions without names.
- This anonymous function is used in an assigned expression. This combination is called an "anonymous function expression"
- Anonymous functions can be used as an argument to other functions or as an immediately invoked function execution.
- An anonymous function is not accessible after its initial creation

**Algorithm**


**Psuedocode**

**code**
```javascript
"use strict"
let total;
(function(x,y){
    total = x + y;
    console.log(total);
})(12,45);
```

## 16. List the differences between named function and assigning functions to variable with examples

**named function**
- A function is a sequence of instructions within a larger program.
- We call the function with parameters anywhere in the program.

**Algorithm**



**Psuedocode**

**code**
```javascript
"use strict"
add(12,45);
function add(x,y){
    const total = x + y;
    console.log(total);
}
add(12,45);
```

*Output:* 
```console
57
```

**assigning functions to variable**
 - The function call after the function assigned to the variable.if it is call before the function assign to variable it throw the typeError like multiply is not function.

 - Use methods after declaration

 - Assigning function to variable may be syntactically lighter than using a named function.

**Algorithm**


**Psuedocode**

**code**

```javascript
"use strict"
const sub = function(x,y){
    const total = x - y;
    console.log(total);
}
sub(45,12);
```

*Output:* 

```console
33
```
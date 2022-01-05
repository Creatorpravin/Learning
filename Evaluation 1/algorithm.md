# JavaScript Evaluation-1

**1. Check prime number?**

**Algorithm**
  - Step 1. Use strict mode as public. Create two variable one is boolean=true another undefined.
  - Step 2. Write a function with parameter and assign to a variable.
  - Step 3. Check the number is == 1 then print  is neither prime nor composite number.
  - Step 4. else number is > 1 then generate a count of numbers using for loop.
  - Step 5. Check the condtion number % i == 0 then prime = false.
  - Step 6. if condition check isPrime is true or false.
  - Step 7. true - is a prime number false - is not a prime number  and return it.
  - Step 8. Call the function with a parameter number.
  - Step 9. Stop.
  
**Psuedocode**

```markdown
BEGIN
"use strict"
INIT sPrime = true, output
INIT primeNumber = FUNCTION(number)
   IF(number === 1) THEN
      PRINT 1 is neither prime nor composite number.
   ELSEIF(number > 1)
       FOR (2<100) DO
         IF(number % i == 0)THEN
            sPrime = false;
            BREAK;
            ENDIF
        ENDFOR
      IF(isprime)
       PRINT number is a prime number         
      ELSE
       PRINT number is not a prime number   
      ENDIF       
   ELSE 
     PRINT The number is not a prime number
   ENDIF    
```
       
       
**code**
```javascript
"use strict"
let isPrime = true;
let output;

const primeNumber = function (number){
// check if number is equal to 1
if (number === 1) {
    output = "1 is neither prime nor composite number.";
}

// check if number is greater than 1
else if (number > 1) {

    // looping through 2 to number-1
    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) {
        output = `${number} is a prime number`;
    } else {
        output = `${number} is a not prime number`;
    }
}

// check if number is less than 1
else {
    output = "The number is not a prime number.";
}
return output;
}
console.log(primeNumber(2));
console.log(primeNumber(2));
console.log(primeNumber(1));
console.log(primeNumber(25));
```

*Output:*
```console
console.log(primeNumber(2));
console.log(primeNumber(1));
console.log(primeNumber(25));
```


**2. What is difference between == and === with an example?**
*Definition:*
  - The ‘==’ operator tests for abstract equality i.e. it does the necessary **type conversions** before doing the equality comparison.
  - But the ‘===’ operator tests for strict equality i.e it **will not do the type conversion** hence if the two values are not of the same type, when compared, it will return false.

**Algorithm**
 - Step 1. Use strict mode as public. 
 - Step 2. Create a funcion with parameter and assing to a variable.
 - Step 3. Then duplicate one value to string by adding empty string.
 - Step 4. Check the both value with "==" and "===" operator and print it.
 - Step 5. Call the funciton with any number.
 - Step 6. Compare a string and string constructor with "==" and "===" operator and print in console.
 - Step 7. Stop.

**psuedocode**
```markdown
BEGIN
"use strict"
INIT check = FUNCTION(value)
    PRINT (value +"") ==value);
    PRINT (value +"") ===value);
    FUNCTION END
check(25);
PRINT("yavar"==new String ("yavar"));
PRINT("yavar"===new String ("yavar"));
```

**code**
```javascript
"use strict"
const check = function(value){
    console.log((value +"") ==value);
    console.log((value +"") ===value);

}
check(25);//call the function
//work with strings
console.log("yavar"==new String ("yavar"));//true
console.log("yavar"===new String ("yavar"));//false
```
*Output*
```console
true
false
true
false
```

**3.How would you reverse a string in JavaScript?**

**Algorithm**
- Step 1. Use strict mode as public. 
- Step 2. Create a function with string parameters and initialise reversed variable as empty string.
- Step 3. Check the string with if consition and use for...of loop to get individual string.
- Step 4. Then add the string reversly with reversed variable.
- Step 5. Call the function with string.
- Step 6. Stop.

**psuedocode**
```markdown
BEGIN
"use strict"
FUNCTION reverseString(String)
   IF(typeof Str === 'string')
     SET  reversed = TYPEOF STRING;
     FOR (let c of String) DO
      SET reversed = c + reversed;
    ENDFOR
       PRINT reversed;
     ELSE
      PRINT (Str,"Not a string");
    FUNCTION END
reverseString("yavar technologies");
```

**code**

```javascript
"use strict"
function reverseString(Str){
    if (typeof Str === 'string'){
     let reversed = '';
    for (let c of Str) {
        reversed = c + reversed;
    }
    console.log(reversed);
  }else{
      console.log(Str,"Not a string");
  }
}
reverseString("Yavar technologies");
/*//using Inbuilt function
let str = 'yavar';
let reverse = [...str].reverse().join('');
console.log(reverse);*/

```

*output*
```console
seigolonhcet ravay
```

**4. How would you reverse words in a sentence?**

**Algorithm**
 - Step 1. Use strict mode as public. Use the split(" ") method to return a new array
 - Step 2. Use the reverse() method to reverse the new created array 
 - Step 3. Use the join(" ") method to join all elements of the array into a string
 - Step 4. Return the reversed string
 - Step 5. Call the string function with string parameters
 - Step 6. Stop.

**psuedocode**
```markdown
BEGIN
"use strict"
FUNCTION reverseString(str) 
     SET splitString = str.split(" "); 
     SET reverseArray = splitString.reverse(); 
     SET joinArray = reverseArray.join(" "); 
   RETURN joinArray;
  ENDFUNCTION
PRINT (reverseString("hello world");
```

**code**
```javascript
"use strict"
function reverseString(str) {
   
   var splitString = str.split(" "); 
    var reverseArray = splitString.reverse(); 
     var joinArray = reverseArray.join(" "); 
    return joinArray; 
}
 
console.log(reverseString("hello world"));
//compress the program 
/*let reverse = function (str) {
 return str.split(" ").reverse().join(" ")};

console.log(reverse("world hello"));*/
```

*Output*

```console
world hello
hello world
```

**5. How will you verify a word as a palindrome?**
**Algorithm**
 - Step 1. Use strict mode as public.
 - Step 2. Create a function with string parameter 
 - Step 3. Initialise the varibale to know the length of string.
 - Step 4. Run the for loop for iteration of half word.
 - Step 5. Use if condition to check first value with last value else print not palindrome.
 - Step 6. Then call the function with string parameter.
 - Step 7. Stop.

**psuedocode**
```markdown
BEGIN
"use strict"
FUNCTION checkPalindrome(str)
     SET len = str.length;
     FOR (let i = 0; i < len / 2; i++) DO
       IF str[i] !== str[len - 1 - i]) 
         RETURN It is not a palindrome.
        ENDIF
       ENDFOR
     RETURN  It is a palindrome
PRINT (checkPalindrome("redivider")
PRINT (checkPalindrome("redivide")
```

**code**
```javascript
"use strict"

function checkPalindrome(str) {

    // find the length of a string
    const len = str.length;

    // loop through half of the string
    for (let i = 0; i < len / 2; i++) {

        // check if first and last string are same
        if (str[i] !== str[len - 1 - i]) {
            return 'It is not a palindrome';
        }
    }
    return 'It is a palindrome';
}


// call the function

console.log(checkPalindrome("redivider"));
console.log(checkPalindrome("redivide"));
```

*Output*
```console
It is a palindrome
It is not a palindrome
```

**6. Write your own program to explain the difference between forEach and map?**
**.map**
  - The map method receives a function as a parameter. Then it applies it on each element and returns an entirely new array populated with the results of calling the provided function.
**.foreach**
  - The forEach() method calls a function for each element in an array.

  - Note:Array.map is like Array.forEach but it returns a copy of the modified array.That original array is still unchanged.

**.forEach**

**Algorithm**
  - Step 1. Use strict mode as public.
  - Step 2. Create a array with string values.
  - Step 3. Use the forEach to iterate the values.
  - Step 4. Print the values.
  - Step 5. Stop.
 
**psuedocode**
  ```markdown
   BEGIN
    "use strict"
    INIT fruit = ['pear','banana','orange','apple','cherry'];
    fruit.forEach(item => PRINT (item));
  ```

**code**

```javascript
"use strict"
let fruit = ['pear',
'banana',
'orange',
'apple',
'cherry'];

fruit.forEach(item=>console.log(item));
//fruit.forEach((item,index,object)=>{
//console.log(item,index,object);});
```
*Output*
```console
pear
banana
orange
apple
cherry

```

**.map**

**Algorithm**
  - Step 1. Use strict mode as public.
  - Step 2. Create a array with string values.
  - Step 3. Use map method with the array and write the event.
  - Step 4. Assing to variable.
  - Step 5. Print the variable.
  - Step 6. Stop.
 
**psuedocode**
```markdown
BEGIN
"use strict"
SET number = [24,24,2,4,56,85,63];
SET condition = number.map(value => value + 1);
PRINT condition;
```
**code**

```javascript
"use strict"
let number = [24,24,2,4,56,85,63];
let condition = number.map(value => value + 1);
console.log(condition);
```

*Output*
```console
[
  25, 25,  3, 5,
  57, 86, 64
]
```

**7. Generate a random number between 1 to 5?**

**Algorithm**
  - Step 1. Use strict mode as public.
  - Step 2. Use Math.floor to returns the largest integer less than or equal to a given number
  - Step 3. Math.random to get the random value till given number.
  - Step 5. Add the number 1 to avoid the 0 values.
  - Step 6. Then print the number.
  - Step 7. Stop. 
   
**psuedocode**
```markdown
BEGIN
PRINT (Math.floor((Math.random() * 5) + 1));
```

**code**

```javascript
"use strict"
console.log(Math.floor((Math.random() * 5) + 1));

```

*Output*

```console
4
3
1
2

```

**8. Remove duplicate from the following array?([1,2,9,4,5,8,3,5,1,4,5])**

**Algorithm**
  - Step 1. Use strict mode as public.
  - Step 2. Create one array with duplicate values and one empty array.
  - Step 3. Use for...each to iterate the values in array. 
  - Step 4. Use if condition to check if true or false. 
  - Step 5. arr.include for check extisting values with current values and push them into empty array.
  - Step 6. Call the function with array.
  - Step 7. Print the new array.
  - Step 8. Stop.
**psuedocode**

```markdown
BEGIN
 SET animals = [1,2,9,4,5,8,3,5,1,4,5];
 SET unique = [];  
 animals.forEach((item) =>
  IF(!unique.includes(item))
      unique.push(item);  
  ENDIF
 PRINT unique;
```

**code**
```javascript
let animals = [1,2,9,4,5,8,3,5,1,4,5];
let unique = [];  
animals.forEach((item) => {  
   if(!unique.includes(item)){  
      unique.push(item);  
   }  
});  
console.log(unique); 
```

*Output*

```console
[
  1, 2, 9, 4,
  5, 8, 3
]
```
**9. Write a program to calculate the sum of the first 10 natural numbers.**

**Algorithm**
  - Step 1. Use strict mode as public.
  - Step 2. Create a function with parameter.
  - Step 3. Declare two varibale sum = 0 , i = 1.
  - Step 4. Use while to iterate the values.
  - Step 5. Add the iterated values inside the while.
  - Step 6. Print the value and call the fucntion.
  - Step 7. Stop.   
**psuedocode**
```markdown
BEGIN
  FUNCTION sum(number)
  INIT sum = 0, i = 1;
  WHILE (i <= number) DO
  SET sum += i;
  SET i++;
  PRINT ('The sum of 10 natural numbers:', sum);
  ENDFUNCTION
  sum(10);
```
  
 **code**
```javascript
"use strict"

function sum(number){
let sum = 0, i = 1;
while(i <= number) {
    sum += i;
    i++;
}

console.log('The sum of 10 natural numbers:', sum);
}
sum(10);
```

*Output*

```console
The sum of 10 natural numbers: 55
```

**10. Write a program to print the sum of the even and odd numbers for a given number?(100)**

**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Create a fucntion with parameter.
- Step 3. Declare two variables odd and even with 0 value.
- Step 4. Iterate for loop till 100 times.
- Step 5. Filter the even by if(i % 2 == 0) then add the every number.
- Step 6. Use else statement add all the odd numbers.
- Step 7. Print both values in console.
- Step 8. Call the function.
- Step 9. Stop.

 **psuedocode**
```markdown
BEGIN
 "use strict"
INIT oddEven= function(value)
    INIT even=0,odd=0;
    FOR(let i=0;i<=value;i++) DO
        IF (i % 2 == 0) THEN
             even = even + i;
        ELSE 
            odd = odd + i;
        ENDIF
    PRINT ("The sum of even numbers:",even);
    PRINT ("The sum of odd numbers:",odd);
oddEven(100);     
```
    

**code**
```javascript
"use strict"
const oddEven= function(value){
    let even=0,odd=0;
    for(let i=0;i<=value;i++){
if(i % 2 == 0) {
    even = even + i;
}

else {
    odd = odd + i;
}

}
console.log("The sum of even numbers:",even);
console.log("The sum of odd numbers:",odd);
};
oddEven(100);

```

*Output*
```console
The sum of even numbers: 2550
The sum of even numbers: 2500
```

**11. Write a program to merge two arrays? ([1,2,9,3,5,1,4,5], [11,54,70,40])**

**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Declare two arrays arr1 and arr2.
- Step 3. Write a function merge.
- Step 4. Use ...rest operator to merge the array.
- Step 5. Return the array.
- Step 6. Call the function and print it's return value.
- Step 7. Stop.
 
**psuedocode**

```markdown
BEGIN
"use strict"
INIT arr1=[1,2,9,3,5,1,4,5],arr2 = [11,54,70,40];
FUNCTION merge()
  INIT merge=[...arr1,...arr2];
  RETURN merge;
  ENDFUNCTION
PRINT (merge());
```

**code**
```javascript
"use strict"
let arr1=[1,2,9,3,5,1,4,5],arr2 = [11,54,70,40];
function merge(){
let merge=[...arr1,...arr2];
 return merge;
}
console.log(merge());
```
*Output*
```console
[
   1,  2, 9,  3,  5,
   1,  4, 5, 11, 54,
  70, 40
]
```
**12. Remove duplicate from an array of an object by id and name? a. [{id: 1, name: ‘Stephen covey’ }, {id: 2, name: ‘Robin Sharma’ }, {id: 3, name:‘Tolstoy’}, {id: 3, name: ‘Tolstoy’}, {id: 5, name: ‘James clear’}]**

**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Declare a constructor and a array.
- Step 3. Use filter function to iterate the values in array.
- Step 4. Declare two variable to check the name and id in consructor with has() method indicates whether the Set object contains the specified value.
- Step 5. Check both values using ! && return the value.
- Step 6. Then call the function with array and print it.
- Step 7. Stop.
 
**psuedocode**
```markdown
BEGIN
"use strict";
INIT x = new Set();
INIT array = [
    {id: 1, name: 'Stephen covey'},
    {id: 2, name: 'Robin Sharma' }, 
    {id: 3, name: 'Tolstoy'}, 
    {id: 3, name: 'Tolstoy'}, 
    {id: 5, name: 'James clear'}
];
INIT filteredArray = array.filter(value => {
  INIT duplicate1 = x.has(value.id);
  SET x.add(value.id);
  var duplicate2 = x.has(value.name);
  SET x.add(value.name);
  RETURN !duplicate1&&!duplicate2;
PRINT (filteredArray);
```

**code**
```javascript
"use strict";
var x = new Set();
var array = [
    {id: 1, name: 'Stephen covey'},
    {id: 2, name: 'Robin Sharma' }, 
    {id: 3, name: 'Tolstoy'}, 
    {id: 3, name: 'Tolstoy'}, 
    {id: 5, name: 'James clear'}
];
var filteredArray = array.filter(value => {
  var duplicate1 = x.has(value.id);
  x.add(value.id);
  var duplicate2 = x.has(value.name);
  x.add(value.name);
  return !duplicate1&&!duplicate2;
});
console.log(filteredArray);

```
*Output*
```console
[
  { id: 1, name: 'Stephen covey' },
  { id: 2, name: 'Robin Sharma' },
  { id: 3, name: 'Tolstoy' },
  { id: 5, name: 'James clear' }
]
```
**13. Compare two objects, If all properties are equal return true or return false? a. ({id: 1, name: “edison”}, {id: 1, name: “edison”})b. ({id: 1, name: “edison”}, {id: 2, name: “edison”})**

**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Create four objects.
- Step 3. Create a function with two parameters.
- Step 4. Get the property name of two parameters then check both length.
- Step 5. Use for loop to iterate the peoperty in A.
- Step 6. Check both of properties with if condition return the boolean value.
- Step 7. Call the function with two properties.
- Step 8. Stop.
 
**psuedocode**

```markdown
BEGIN
INIT a={id: 1, name: "edison"};
INIT b={id: 1, name: "edison"};
INIT c={id: 1, name: "edison"};
INIT d={id: 2, name: "edison"};
FUNCTION objcmp(x,y)
    INIT A=Object.getOwnPropertyNames(x);
    INIT B=Object.getOwnPropertyNames(y);
    IF(A.length!=B.length)THEN
      RETURN false;
      ENDIF
    FOR(let i=0;i< A.length;i++) DO
       INIT propName=A[i];
       IF(x[propName]!==y[propName]) THEN
         RETURN false;
       ELSE
          RETURN true;
        ENDIF
    ENDFOR
    ENDFUNCTION
     
```


**code**
```javascript
"use strict";
var a={id: 1, name: "edison"};
var b={id: 1, name: "edison"};
var c={id: 1, name: "edison"};
var d={id: 2, name: "edison"};

function objcmp(x,y){
    let A=Object.getOwnPropertyNames(x);
    let B=Object.getOwnPropertyNames(y);
    if(A.length!=B.length)
      return false;
    for(let i=0;i<A.length;i++){
         let propName=A[i];
         if(x[propName]!==y[propName])
           return false;
     } 
     return true;
}
console.log(objcmp(a,b));     //true
console.log(objcmp(c,d));     //false
```
*Output*
```console
true
false
```
**14. Take a multidimensional array and flat the array?[1,4,2,3,[10,20,20], [100,500,700,600],[2000,1000]]**
**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Create a muiltidimentional array.
- Step 3. Use multi.flat to flat the array to single array.
- Step 4. Print the Array.
- Step 5. Stop.
**psuedocode**
```markdown
BEGIN
"use strict"
INIT multi = [1,4,2,3,[10,20,20], [100,500,700,600],
[2000,1000]];
PRINT (multi.flat(Infinity));
```

**code**
```javascript
"use strict"
let multi = [1,4,2,3,[10,20,20], [100,500,700,600],
[2000,1000]]
console.log(multi.flat(Infinity));
```

*Output*
```console
[
     1,   4,   2,    3,
    10,  20,  20,  100,
   500, 700, 600, 2000,
  1000
]
```

**15. Group by the id of the following array of objects using the Array.reduce method?[{id: 1, name: ‘edison’ }, {id: 2, name: ‘Annand’ }, {id: 3, name: ‘Vasnath’}]**
**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Delare the array of objects.
- Step 3. Use the reduce function to iterate previous value with current value.
- Step 4. Check the both value and add count into previous value or make it one
- Step 5. Print the value.
- Step 6. Stop. 
 
**psuedocode**
```markdown
BEGIN
"use strict";
INIT peoples=[
    {id: 1, name: 'edison' }, 
    {id: 2, name: 'Annand' }, 
    {id: 3, name: 'Vasnath'}
];
INIT groupByid = peoples.reduce((acc, intex) => {
    acc[intex.id] = acc[intex.id] + 1 || 1;
    RETURN acc;
PRINT (groupByid); 

```

**code**
```javascript
"use strict";
var peoples=[
    {id: 1, name: 'edison' }, 
    {id: 2, name: 'Annand' }, 
    {id: 3, name: 'Vasnath'}
];
var groupByid = peoples.reduce((acc, intex) => {
    acc[intex.id] = acc[intex.id] + 1 || 1;
    return acc;
  }, {} );
console.log(groupByid); 
```
*Output*
```console
{ '1': 1, '2': 1, '3': 1 }
```

**16. Write a program in Javascript to display the pattern like right angle triangle using an asterisk.The pattern like :**
```console
*
**
***
****
*****
```
**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Declare variable with 5 value and make another one with empty string.
- Step 3. Run for loop 5 times then run the nested for loop i times.
- Step 4. Add the "*" in nested loop and add /n at the end of nested loop.
- Step 5. Then print the string values.
- Step 6. Stop. 

**psuedocode**
```markdown
BEGIN
"use strict";
INIT n = 5;
INIT string = "";
FOR(let i = 1; i <= n; i++) DO
  FOR (let j = 0; j < i; j++) DO
    SET string += "*";
    ENDFOR
  SET string += "\n";
  ENDFOR
PRINT (string);
```

**code**
```javascript
"use strict";
const n = 5;
let string = "";
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);
```
*Output*
```console
*
**
***
****
*****
```

**17. Write a program in Javascript to make such a pattern like right angle triangle with number increased by 1**
```console
1
2 3
4 5 6
7 8 9 10
```
**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Declare variable with 4 value and make another one with empty string.
- Step 3. Declare count variable at public with number 1.
- Step 4. Run for loop 4 times then run the nested for loop i times.
- Step 5. Add the count value to a variable as string and increment it.
- Step 6. Add the count in nested loop and add /n at the end of nested loop.
- Step 7. Print the string variable.
- Step 8. Stop.

 
**psuedocode**
```markdown
BEGIN 
"use strict"
INIT n = 4; 
INIT string = "";
INIT count = 1;
FOR(let i = 1; i <= n; i++)
   FOR(let j = 1; j <= i; j++)
     SET tring += " " + count;
     SETcount++;
     ENDFOR
   SET string += "\n";
   ENDFOR
PRINT (string);
```
**code**

```javascript
"use strict"
const n = 4; 
let string = "";
let count = 1;
for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= i; j++) {
    string += " " + count;
    count++;
  }
  string += "\n";
}
console.log(string);
```
*Output*
```console
1
2 3
4 5 6
7 8 9 10
```

**18. Write a program in Javascript to make such a pattern like a pyramid with numbers increased by 1**
```console
   1
  2 3
 4 5 6
7 8 9 10

```
**Algorithm**
- Step 1. Use strict mode as public.
- Step 2. Declare count variable at public with number 1 and a empty string.
- Step 3. Run for loop 4 times then run the nested for loop 5 - i times for print spaces.
- Step 4. Then create another for loop with condition of (2*i)-i 
- Step 5. Add the count value to a variable as string and increment count.
- Step 6. Add the count in nested loop and add /n at the end of nested loop.
- Step 7. Then print the value.

**psuedocode**
```markdown
BEGIN
"use strict";
INIT number = "";
INIT count=1;
FOR (let i = 1;i<5;i++) DO
  FOR (let j = 1;j<= 5 - i;j++) DO
    SET number += " ";
    ENDFOR
  FOR (let k = 0; k < 2*i-i ; k++) DO
   SET number += count;
   SET count++;
   SET number += "
   ENDFOR
  SET += "\n";
  ENDFOR
PRINT (number);
```

**code**
```javascript
"use strict";
let number = "";
let count=1;
for (let i = 1;i<5;i++) {
  for (let j = 1;j<= 5 - i;j++){
    number += " ";
  }
  for (let k = 0; k < 2*i-i ; k++) {
    number += count;
    count++;
    number += " ";
  }
  number += "\n";
}
console.log(number);
```

*Output*
```console
   1
  2 3
 4 5 6
7 8 9 10

```

**19. Write a program in Javascript to display the pattern like a diamond**
```console
    *
   ***
  *****
 *******
*********
 *******
  *****
   *** 
    *
```
**Algorithm**
 - Step 1. Use strict mode as public.
 - Step 2. Declare n variable at public with number 1 and a empty string.
 - Step 3. Run for loop nth times do spaces then run the nested for loop 2*i-1 times for print stars.
 - Step 4. Add /n at the end of nested loop.
 - Step 5. Again run loops to print reverse prymid.
 - Step 6. for loop nth - 1 times do spaces then run the nested for loop 2*(n-1) times for print stars.
 - Step 7. Add /n at the end of nested loop.
 - Step 8. Stop.

**psuedocode**
```markdown
BEGIN
"use strict"
INIT n = 5;
INIT string = "";
FOR (let i = 1; i <= n; i++) DO
  FOR (let j = 1; j < n - i + 1; j++)
   SET string += " ";
  ENDFOR
  FOR (let k = 1; k <= 2 * i - 1; k++)
   SET string += "*"; 
 SET string += "\n";
  ENDFOR
 ENDFOR
 FOR (let i = 1; i <= n - 1; i++)
    FOR (let j = 1; j < i + 1; j++)
     SET string += " ";
     ENDFOR
    FOR (let k = 1; k <= 2 * (n - i) - 1; k++)
      SET string += "*"; 
   SET string += "\n";
  ENDFOR
PRINT (string);
```

**code**
```javascript
"use strict"
let n = 5;
let string = "";
// Pyramid
for (let i = 1; i <= n; i++) {
  for (let j = 1; j < n - i + 1; j++) {
    string += " ";
  }
  for (let k = 1; k <= 2 * i - 1; k++) {
    string += "*";
  }
  string += "\n";
}
// Reverse Pyramid
for (let i = 1; i <= n - 1; i++) {
  for (let j = 1; j < i + 1; j++) {
    string += " ";
  }
  for (let k = 1; k <= 2 * (n - i) - 1; k++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);
```
*Output*
```console
    *
   ***
  *****
 *******
*********
 *******
  *****
   *** 
    *
```

**20. Explain following terms**
**a. console.log**
  - The console.log() is a function in JavaScript which is used to print any kind of variables defined before in it or to just print any message that needs to be display.
**code**
```javascript
console.log("Hello world!");//Hello world!
const myObj = {firstname:"Praveen", lastname:"Kumar"};
console.log(myObj);
```
*Output*
```console
Hello world!
{ firstname: 'Praveen', lastname: 'Kumar' }

```
**b. console.dir**
  - If you want to take a look at all object’s properties and methods, you can print it
out directly into the console using console.dir method.

**code**
```javascript
let x = {property: 1, prop1: 2, method: function(){}};
console.dir(x);
```

*Output*
```console
{ property: 1, prop1: 2, method: [Function: method] }
```
**c. console.count**
  - The console.count() method logs the number of times that this particular call to count() has been called.
**code**
```javascript
function greet() {
  console.count(user);
  return user;
}

user = "praveen";
greet();
user = "kumar";
greet();
greet();
console.count("kumar");
```
*Output*

```console
praveen: 1
kumar: 1
kumar: 2
kumar: 3
```


**d. console.table**
 - The console.table() method displays tabular data as a table.

 - This function takes one mandatory argument data, which must be an array or an object, and one additional optional parameter columns.

**code**
```javascript
function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  
  var arun = new Person("Arun", "Pandian");
  var dinesh = new Person("Dinesh", "Kumar");
  var bala = new Person("Bala", "Subramani");
  
  console.table([arun, dinesh, bala]);

```
*Output*
  | (index)  |        firstname   | lastName   
   | ------   |     ---------- |   ---------- 
   |  0	     |        'Arun'    |'Pandian'  
   |  1	     |     'Dinesh'     |'Kumar'   
   |  2	     |    'Bala'    |'Subramani' 


│ (index) │ firstName │  lastName   │
| -----   | -------   |  --------- | 
│    0    │  'Arun'   │  'Pandian'  │
│    1    │ 'Dinesh'  │   'Kumar'   │
│    2    │  'Bala'   │ 'Subramani' │

**e. console.time/timeLog/timeEnd**
  - The console.timeLog() method logs the current value of a timer that was previously started by calling console.time() to the console.
  - **console.time/console.timeEnd**You can track the amount of time between function calls. This can be helpful
when optimizing code:

**code**
```javascript
console.time("answer time");
console.timeLog("answer time");
console.timeEnd("answer time");
```
*Output*
```console
answer time: 0.099ms
answer time: 0.467ms
```

**f. console.trace**
  - The trace() method displays a trace that show how the code ended up at a certain point.
  - The console.trace() method outputs a stack trace
**code**
```javascript
function foo() {
    function bar() {
      console.trace();
    }
    bar();
  }
    foo();
```
*Output*

```console
bar	
foo	
(anonymous)

```

**g. console.group/groupEnd**
  - The console.group() method creates a new inline group in the Web console log. This indents following console messages by an additional level, until console.groupEnd() is called.

**code**
```javascript
console.log("This is the outer level");
console.group();
console.log("Level 2");
console.group();
console.log("Level 3");
console.warn("More of level 3");
console.groupEnd();
console.log("Back to level 2");
console.groupEnd();
console.log("Back to the outer level");

```

*Output*
```console
This is the outer level
  Level 2
    Level 3
    More of level 3
  Back to level 2
Back to the outer level
```

**h. console.assert**
 - The console.assert() method writes an error message to the console if the assertion is false. If the assertion is true, nothing happens.
**code**
```javascript
const errorMsg = 'the # is not even';
for (let number = 2; number <= 5; number += 1) {
    console.log('the # is ' + number);
    console.assert(number % 2 === 0, {number: number, errorMsg: errorMsg});
}
```
*Output*
```console
the # is 2
the # is 3
Assertion failed: [object Object]
the # is 4
the # is 5
Assertion fa
```
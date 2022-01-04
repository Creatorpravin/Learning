# JavaScript Evaluation-1

**1. Check prime number?**

**Algorithm**
 
**Psuedocode**

**code**
```javascript
"use strict"
// check if a number is prime or not


let isPrime = true;
let output;
//const number = 23;
let primeNumber = function (number){
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
 
**psuedocode**

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
 
**psuedocode**

**code**

```javascript
"use strict"
function reverseString(String){
    let reversed = '';
    for (let c of String) {
        reversed = c + reversed;
    }
    console.log(reversed);
}
reverseString("yavar technologies");
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
 - Step 1. Use the split(" ") method to return a new array
 - Step 2. Use the reverse() method to reverse the new created array 
 - Step 3. Use the join(" ") method to join all elements of the array into a string
 - Step 4. Return the reversed string
 - Step 5. Call the string function with string parameters

**psuedocode**

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
let reverse = function (str) {
 return str.split(" ").reverse().join(" ")};

console.log(reverse("world hello"));
```

*Output*

```console
world hello
hello world
```

**5. How will you verify a word as a palindrome?**
**Algorithm**
 
**psuedocode**

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
**Algorithm**
 
**psuedocode**

**code**

**.forEach**

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
 
**psuedocode**

**code**

```javascript
"use strict"
console.log(Math.floor((Math.random() * 5) + 1));

```

*Output*

```console
4
```

**8. Remove duplicate from the following array?([1,2,9,4,5,8,3,5,1,4,5])**

**Algorithm**
 
**psuedocode**

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
 
**psuedocode**

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
 
**psuedocode**

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
 
**psuedocode**

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
 
**psuedocode**

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
 
**psuedocode**

**code**
```javascript
"use strict"
var a={id: 1, name: "edison"};
var b={id: 1, name: "edison"};
var c={id: 1, name: "edison"};
var d={id: 2, name: "edison"};
function is_array(value) {
    return typeof value.reduce=="function"&&
           typeof value.filter=="function"&&
           typeof value.map=="function"&&
           typeof value.length=="number";
}
function arrcmp(a,b){
    // one or more values are not arrays:
    if(!(is_array(a)&&is_array(b)))
     return false;
   //Not equal by length
   if(a.length != b.length)
   return false;
   //compare by value
   for(let i=0;i<a.length;i++)
   if(i[a]!==b[i])
   return false;
   //All test passed: array a and b are equal
return true;

}
function objcmp(a,b){
    //copy properties into A and B
    let A=Object.getOwnPropertyNames(a);
    let B=Object.getOwnPropertyNames(b);
    if(A.length != B.length)
     return false;
    
     for (let i=0;i<A.length;i++){
         let propName=A[i];
         let p1 = a[propName];
         let p2 = b[propName];
         
         if(is_array(p1)&&is_array(p2)){
             if(!arrcmp(p1, p2))
              return false;

         } else
         if(p1.constructor === Object &&
            p2.constructor === Object){
                if(!objcmp(p1, p2))
                  return false;
            } else if (p1 !== p2)
             return false;

     }

   return true;
}
console.log(objcmp(a,b));//true
console.log(objcmp(c,d));//false
```
*Output*
```console
true
false
```
**14. Take a multidimensional array and flat the array?[1,4,2,3,[10,20,20], [100,500,700,600],[2000,1000]]**
**Algorithm**
 
**psuedocode**

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
 
**psuedocode**

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
 
**psuedocode**

**code**
```javascript
"use strict"
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
 
**psuedocode**

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
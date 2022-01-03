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

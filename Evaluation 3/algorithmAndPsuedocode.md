1. What is the scope of ‘this’ inside the Arrow function? Explain with an example? 
  
   - The value of this inside a function is usually defined by the function's call. So, this can have different values inside it for each execution of the function.

**Algorithm**

**Psuedocode**

**Code**
```javascript
"use strict";
var a = 10;
//this inside arrow function
var b = () => {
    console.log(this);
    console.log(this.a);
}
b();

//this inside object
var obj = {
    myMethod:() => {
        console.log(this);
        console.log(this.a);
    }
};
obj.myMethod();

//this access inside value of object
let myObject = {
    a:20,
    myArrowFunction: null,
    myMethod: function () {
       this.myArrowFunction = () => { console.log(this.a) };
    }
};   
myObject.myMethod(); // this === myObject

myObject.myArrowFunction(); // this === myObject

let myArrowFunction = myObject.myArrowFunction;
myArrowFunction(); //this === myObject
```

*Output*


2. How would you create all permutations of a string?
 - A Permutation of a string is another string that contains same characters, only the order of characters can be different. 

**Algorithm**

**Psuedocode**

**Code**
```javascript
"use strict";
let string="ABC";
function permutation( string, result){
    if(string.length === 0){
        count++;
        console.log(result);
    }else{
        for(let i = 0; i < string.length ; i++ ){
            let remain = string.substring( 0, i) + string.substring( i + 1 );
            permutation( remain, result + string[i]);
        }
    }
}
if(typeof string === "string"){
    if(string.length > 0){
        var count = 0;
        permutation( string, "");
        console.log("Total number of permutation are :",count);
    }else{
        console.log("This is empty string");
    }

}else{
    console.log("This is not string")
}

```
*Output*


3. What is the difference between when classic and arrow functions are used as event
callbacks?

**Classic function**

**Algorithm**

**Psuedocode**

**Code**

```htm
<html>
    <head>
        <title>Arrow event call back</title>
        <script>
            function clicked(){
                console.log("You Clicked!!!");
                console.log(this)
            }
            document.addEventListener("click",clicked);
        </script>
    </head>
    <body>
        <h1 style="color: firebrick; text-align-last: center; text-decoration-line: underline;">CLICK</h1>
    </body>
</html>

```
*Output*
```console
You Clicked!!!
```

**Arrow Function**

**Algorithm**

**Psuedocode**

**Code**
```htm
<html>
    <head>
        <title>Arrow event call back</title>
        <script>
            var clicked = () =>{
                console.log("You Clicked!!!");
                console.log(this)
            }
            document.addEventListener("click",clicked);
        </script>
    </head>
    <body>
        <h1 style="color: firebrick; text-align-last: center; text-decoration-line: underline;">CLICK</h1>
    </body>
</html>
```

*Output*
```console
You Clicked!!!
```

4. Look at the code below, you have a for loop if you have setTimeout inside it. If log the
loop counter inside setTimeout, what will be logged?
```javascript
for(var i = 0; i < 10; i++) {
setTimeout(function() {
console.log(i);
}, 10);
}
```
- First, It will run the loop and add the iteration of i to 10.
- Then print the number.

*Output*
```console
10
10
10
10
10
10
10
10
10
10
```

5. Explain the Class instance method and static method with an example?

**Static Method**
 - If it's a static method (doesn't use any instance data), then declare it as a static method and you can directly call it.

**Algorithm**

**Psuedocode**

**Code**

```javascript
//Static method in class
class StaticMethod {
    static staticMethod() {
    return 'static method has been called.';
  }
}
console.log(StaticMethod.staticMethod());
```

*Output*

```console
static method has been called.
```

**Instance Method**
- if it's an instance method, then you would typically create an object of type one and then call the method on that object (usually in the constructor).
 
**Algorithm**

**Psuedocode**

**Code**
```javascript
"use strict";
//Instance method in class
class InstanceMethod {
    instanceMethod() {
    return 'instance method has been called.';
  }
}
let obj = new InstanceMethod();
console.log(obj.instanceMethod()); //"instance method has been called."
```

*Output*
```console
instance method has been called.
```


6. How does “this” works inside the Class method with an example?

**Algorithm**

**Psuedocode**

**Code**

*Output*



7. What is the execution order of the following block of code?
```javascript
const ex1 = () => console.log(ex1)
const ex2 = () => console.log(ex2)
const ex = () => {
console.log(ex)
setTimeout(ex1, 1000)
ex2()
}
ex()
```

8. Explain the event loop with an example?

**Algorithm**

**Psuedocode**

**Code**

*Output*


9. Create a custom event listener and explain?

**Algorithm**

**Psuedocode**

**Code**

*Output*

10. Explain the ‘super’ and ‘constructor’ keywords inside the Class with an example?

**Algorithm**

**Psuedocode**

**Code**

*Output*

## 1. What is the scope of ‘this’ inside the Arrow function? Explain with an example? 
  
   - The value of this inside a function is usually defined by the function's call. So, this can have different values inside it for each execution of the function.

**Algorithm**

Step 1. Use strict mode as public. Declare a variable with a value.
Step 2. Declare arrow function and access the variable a by this.a.
Step 3. Create arrow function inside a object and call the variable a by this.a.
Step 4. Create a object and create a property with value and a arrow function.
Step 5. Access the value from arrow function.
Step 6. Call the function.


**Psuedocode**
```markdown
"use strict";
INIT a = 10;
INIT b = () => 
    PRINT(this);
    PRINT(this.a);
FUNCTIONCALLb();
INIT obj = {
    myMethod:() => 
        PRINT(this);
        PRINT(this.a);
    };
obj.myMethod();
let myObject = {
    a:20,
    myArrowFunction: null,
    myMethod: function () 
       this.myArrowFunction = () =>  PRINT(this.a)
    };   
myObject.myMethod(); 
myObject.myArrowFunction(); 
let myArrowFunction = myObject.myArrowFunction;
myArrowFunction(); 
```

**Code**
```javascript
"use strict";
const a = 10;
//this inside arrow function
let b = () => {
    console.log(this);
    console.log(this.a);
}
b();

//this inside object
let obj = {
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


## 2. How would you create all permutations of a string?
 - A Permutation of a string is another string that contains same characters, only the order of characters can be different. 

**Algorithm**

Step 1. Use strict mode as public. Declare a variable.
Step 2. Create a function with parameters.
Step 3. Check the length of the string and increase the count at every time.
Step 4. Declare a for loop and run till the length of the string.
Step 5. Use recursion method to call the function again and again.
Step 6. Outside the function check length and type of string then call the function.


**Psuedocode**
```markdown
"use strict"
INIT string="ABC";
FUNCTION permutation( string, result)
    IF(string.length === 0)THEN
        count++;
        PRINT(result);
    ELSE
        FOR(let i = 0; i < string.length ; i++ )DO
            let remain = string.substring( 0, i) + string.substring( i + 1 );
            permutation( remain, result + string[i]);
        ENDFOR
    ENDIF
FUNCTIONEND
IF(typeof string === "string")THEN
    IF(string.length > 0)THEN
        var count = 0;
        permutation( string, "");
        PRINT("Total number of permutation are :",count);
    ELSE
        PRINT("This is empty string");
    ENDIF

ELSE
        PRINT("This is not string")
ENDIF
```
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


## 3. What is the difference between when classic and arrow functions are used as event
callbacks?

**Classic function**

**Algorithm**

Step 1. Create a html file.
Step 2. Inside the script tag write a function with name of clicked.
Step 3. Print something inside the function.
Step 4. Add event of click then function is executed.

**Psuedocode**
```htm
<html>
    <head>
        <title>Arrow event call back</title>
        <script>
            FUNCTION clicked(){
                PRINT("You Clicked!!!");
                PRINT(this)
            }
            document.addEventListener("click",clicked);
        </script>
    </head>
    <body>
        <h1 style="color: firebrick; text-align-last: center; text-decoration-line: underline;">CLICK</h1>
    </body>
</html>

```

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

Step 1. Create a html file.
Step 2. Inside the script tag write arrow function clicked.
Step 3. Print something inside the function.
Step 4. Add event of click then function is executed.

**Psuedocode**
```htm
<html>
    <head>
        <title>Arrow event call back</title>
        <script>
            let clicked = () =>{
                PRINT("You Clicked!!!");
                PRINT(this)
            }
            document.addEventListener("click",clicked);
        </script>
    </head>
    <body>
        <h1 style="color: firebrick; text-align-last: center; text-decoration-line: underline;">CLICK</h1>
    </body>
</html>
```

**Code**
```htm
<html>
    <head>
        <title>Arrow event call back</title>
        <script>
            let clicked = () =>{
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

## 4. Look at the code below, you have a for loop if you have setTimeout inside it. If log the
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

## 5. Explain the Class instance method and static method with an example?

**Static Method**
 - If it's a static method (doesn't use any instance data), then declare it as a static method and you can directly call it.

**Algorithm**

Step 1. Use strict mode as public.
Step 2. Declare a class inside the class create a method.
Step 3. Then return the value.
Step 4. Outside the class call the method of class directly.

**Psuedocode**

```markdown
"use strict"
//Static method in class
CLASS StaticMethod 
    static staticMethod() 
    RETURN 'static method has been called.'
PRINT(StaticMethod.staticMethod())
```
**Code**

```javascript
"use strict"
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

Step 1. Use strict mode as public.
Step 2. Create a class inside the class create a method and return something.
Step 3. Create new constructor object for the class.
Step 4. Use the constructor call the method of class.

**Psuedocode**
```markdown
"use strict"
CLASS InstanceMethod 
    instanceMethod() 
    RETURN 'instance method has been called.'
INIT obj = new InstanceMethod();
PRINT(obj.instanceMethod())
```

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


## 6. How does “this” works inside the Class method with an example?

**Algorithm**

Step 1. Use strict mode as public.
Step 2. Create a class name of student with constructor.
Step 3. Getdetails method will create inside class.
Step 4. Access the value by this keyword.
Step 5. Create constructor object and call the class.

**Psuedocode**
```markdown
CLASS student
    constructor(name,location)
        this.name=name;
        this.location=location;
    getdetails()
       PRINT('Hi, i am '+this.name+' from '+this.location+'.')
ENDCLASS
INIT std1 = new student("Pravin","Chennai")
std1.getdetails();
INIT std2 = new student("Dinesh","Covai");
std2.getdetails();
```

**Code**
```javascript
class student{
    constructor(name,location){
        this.name=name;
        this.location=location;
    }
    getdetails(){
        console.log('Hi, i am '+this.name+' from '+this.location+'.');
    }
}

const std1 = new student("Pravin","Chennai")
std1.getdetails();

const std2 = new student("Dinesh","Covai");
std2.getdetails();
```

*Output*

```console
Hi, i am Pravin from Chennai.
Hi, i am Dinesh from Covai.
```

## 7. What is the execution order of the following block of code?
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
*Output*
```console
[Function: ex]
[Function: ex2]
[Function: ex1]
```
## 8. Explain the event loop with an example?

 - JavaScript has a runtime model based on an event loop, which is responsible for executing the code, collecting and processing events, and executing queued sub-tasks. This model is quite different from models in other languages like C and Java.


**Algorithm**

Step 1. Use strict mode as public.
Step 2. Declare the annonymous function.
Step 3. Create two set timeout function and print something.
Step 4. Then call the fucntion.


**Psuedocode**
```markdown
(FUNCTION() {

    PRINT('this is the start');
  
    setTimeout(FUCNTION cb() {
      PRINT('Callback 1: this is a msg from call back');
    },0); 
  
    PRINT('this is just a message');
  
    setTimeout(FUNCTION cb1() {
      PRINT('Callback 2: this is a msg from call back');
    }, 500);
  
    PRINT('this is the end');
  
  })();
```
**Code**
```javascript
(function() {

    console.log('this is the start');
  
    setTimeout(function cb() {
      console.log('Callback 1: this is a msg from call back');
    },0); // has a default time value of 0
  
    console.log('this is just a message');
  
    setTimeout(function cb1() {
      console.log('Callback 2: this is a msg from call back');
    }, 500);
  
    console.log('this is the end');
  
  })();
```

*Output*

```console
this is the start
this is just a message
this is the end
Callback 1: this is a msg from call back
Callback 2: this is a msg from call back
```


## 9. Create a custom event listener and explain?
 - It demonstrates how to create and dispatch DOM events. Such events are commonly called synthetic events, as opposed to the events fired by the browser itself.

**Algorithm**

Step 1. Use strict mode as public.
Step 2. Create a new event as start.
Step 3. Add the event listener.
Step 4. Dispatch the event.        
**Psuedocode**
```markdown
"use strict";
INIT startEvent = new Event("start");
document.addEventListener("start",FUNCTION(event) PRINT("hello world") PRINT(event),FALSE)
document.dispatchEvent(startEvent);
```
**Code**
```javascript
"use strict";
//create a new custom event  “start”
let startEvent = new Event("start");
//listen for the "start" event
document.addEventListener("start",function(event){console.log("hello world");console.log(event);},false);
//dispatch the “start” event
document.dispatchEvent(startEvent);

```
*Output*
```console
hello world
Event {isTrusted: false, type: 'start', target: document, currentTarget: document, eventPhase: 2, …}
true

```


## 10. Explain the ‘super’ and ‘constructor’ keywords inside the Class with an example?

**Constructor**

**Algorithm**

Step 1. Use strict mode as public.
Step 2. Create a class with parameters and create a method.
Step 3. Use this keyword to access constructor value inside the method.
Step 4. Create constructor object and pass the value.
Step 5. Call the method.

**Psuedocode**
```markdown
CLASS vehicle{
    constructor(vname)
        this.vname = vname;
    getdetails(){
        PRINT("The vehicle is "+this.vname);
ENDCLASS
INIT veh1 = new vehicle("bus");
veh1.getdetails();

INIT veh2 = new vehicle("car");
veh2.getdetails();
```

**Code**
```javascript
class vehicle{
    constructor(vname){
        this.vname = vname;
    }
    getdetails(){
        console.log("The vehicle is "+this.vname);
    }
}

const veh1 = new vehicle("bus");
veh1.getdetails();

const veh2 = new vehicle("car");
veh2.getdetails();
```

*Output*

```console
The vehicle is bus
The vehicle is car
```

**Algorithm**

Step 1. Use strict mode as public.
Step 2. Create a class with parameters and create a method.
Step 3. Use this keyword to access constructor value inside the method.
Step 4. Create a child class for car use super keyword to access the properties of parent class.
Step 5. Call the parent method in child method.
Step 6. Create constructor object for child class and call the method.

**Psuedocode**
```markdown
"use strict";
CLASS Car 
    constructor(brand) 
      this.carname = brand;
    show1() 
      RETURN 'I have a ' + this.carname;
CLASSEND
CLASS Model extends Car 
    constructor(brand, model) 
      super(brand);
      this.model = model;
    show2() 
      RETURN super.show1() + ', it is ' + this.model;
INIT mycar = new Model("BMW", "Q3");
PRINT(mycar.show2());
```

**Code**
```javascript
//super
"use strict";
class Car {
    constructor(brand) {
      this.carname = brand;
    }
    show1() {
      return 'I have a ' + this.carname;
    }
  }
class Model extends Car {
    constructor(brand, model) {
      super(brand);
      this.model = model;
    }
    show2() {
      return super.show1() + ', it is ' + this.model;
    }
}
let mycar = new Model("BMW", "Q3");
console.log(mycar.show2());
```

*Output*

```console
I have a BMW, it is Q3
```

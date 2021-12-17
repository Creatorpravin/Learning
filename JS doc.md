# **Chapter 1**
* Presentation Format
   - JavaScript Grammar is not a complete JavaScript reference or manual. The subjects were reduced to only what’s important in modern-day JavaScript environment.
   - Namely: imports, classes, constructors, key principles behind functional programming, including many features ranging from ES5 - ES10 are covered in this book.
* Creative Communication:
   - Some of JavaScript is easy, some of it is difficult. Not everything can be explained by source code alone. Some things are based on intangible ideas or principles. 
   - Throughout this tutorial book you will come across many creative communication devices, designed to make the learning process a bit easier and perhaps more fun. One example of that is color-coded diagrams.
* Theory:
   - Not all subjects require extensive theory. On the other hand, some things won’t make any sense without it.  
   - Additional discussion will be included, where it becomes absolutely necessary, in order to fully understand a particular concept.
* Color-Coded Diagrams:
       - A significant amount of effort went into creating diagrams describing fundamental ideas behind JavaScript.
       - They were designed for communicative value, hopefully  they will speed up the learning process in places where hard to grasp abstract ideas need to be explained visually.
       

* Source code:
 - Source code listings will be provided to cement the foundational principles from preceding text.  

**Example:**  
 ```css
  // Create (instantiate) a sparrow from class Bird  
  let sparrow = new Bird(“sparrow”,”gray”);  
  sparrow.fly();  
  sparrow.walk();  
  sparrow.lay_egg();  
  sparrow.talk();  //error,only parrot can talk  
 ```
 
 - This is an example of instantiating sparrow object from Bird class and using some of its methods.
* Code close ins:
     - Most of the source code is accompanied by source code listings. 
     - But when we need to close in on a particular important subject, a slightly larger diagram with source code and additional color-coded highlighting will be shown. 
For example, here is exploration of an anonymous function when used in the context of a event callback function:

    ```
    setTimeout(function() {    
    console.log(“print  something  in  1 second”);
    }, 1000);


# **Chapter 2**
**Chrome Console**
* 2.0.1 Beyond Console Log
   - Many programmers only know Chrome’s console.log but the console API contains few other methods that have practical use, especially when time is of essence.
* copy(obj) function
Copying JSON representation of an existing object to your copy buffer:
```javascript
let x = {property: 1, prop1: 2, method: function(){}};
copy(x);

```
 - Now the JSON is in your copy-paste buffer, you can paste it into any text editor.
 - In this example x is a simple self-created object. But imagine a situation where a
much more complex object is returned from a database API.
- **Note:** Only JSON is returned, this means that methods will not make it to the
copy buffer. (JSON string format does not support methods, only properties.)


**2.0.2 console.dir**
 - If you want to take a look at all object’s properties and methods, you can print it
out directly into the console using console.dir method:

```javascript
console.dir(x)
VM129:1 Objectmethod: ƒ ()prop1: 2property: 1[[Prototype]]: Object
```
 - Note: In simple words, the console.log() returns the object in its string representation and console.dir() recognizes the object just as an object and outputs its properties. Both log() and dir() returns the string just as a string.

 - Get the output of **DOM Element**
```javascript
console.dir(document.body)
```

* 2.0.3 console.error
```javascript
let fuel = 99;
function launch_rocket(){
    function warning_mgs(){
        console.error("Not enough fuel.");  
    }

if(fuel >= 100)
{
    //looks everything is fine
 }
  else
        warning_mgs(); 
}
launch_rocket();
```
The great thing about console.error is that it also provides the stack trace:
```
VM1971:4 Not enough fuel.
warning_mgs	@	VM1971:4
launch_rocket	@	VM1971:13
(anonymous)	@	VM1971:16
```
**2.0.4 console.time() and console.timeEnd()**
  - You can track the amount of time between function calls. 
   - This can be helpful
when optimizing code:
```javascript
console.time();
let arr = new Array(1000);
for (let i = 0; i < arr.length;i++){
    arr[i]=new Object();
}
console.timeEnd();
```
 **Output:**
 ```
 default: 127.450927734375 ms
 ```
**2.0.5 console.clear**
   - It is used to clear the previous console ouputs.
  ```javascript
  console.clear();
  ```
**Printing Objects**
  - In JavaScript all objects have .toString() method.
  -  When providing an object
to **console.log(value)** it can print it either as an object, or as a string.
```javascript
let obj = {Name:'praveen',location:"coimbatore" };
console.log(obj);
console.log("object = "+ obj);
console.log(`${obj}`);

```
# **Chapter 3**
## **Welcome To JavaScript**
**3.1 Entry Point**
  - Every computer program has an entry point.
You can start writing your code directly into <script> tags.
 -  But this means it
will be executed instantly and simultaneously as the script is being downloaded
into the browser, without concern for DOM or other media.
  - This can create a problem because your code might be accessing DOM elements
before they are fully downloaded from the server.
  - To remedy the situation, you may want to wait until the DOM tree is fully available.
  - **The Document Object Model (DOM)** is a programming API for HTML and XML documents. It defines the logical structure of documents and the way a document is accessed and manipulated.
**DOMContentLoaded**
  - To wait on the DOM event, add an event listener to the document object. The
 name of the event is DOMContentLoaded.
```javascript
<html>
    <head>
        <title> DOM Loaded.</title>
        <script type="text/javascript">
            function load() {
                console.log("DOM Loaded.");
            }
            document.addEventListener("DOMContentLoaded", load);
        </script>
    </head>
    <body>
      <h1>HEAD</h1>
    </body>
</html>
```
  - Here the entry point is your own custom function load(). This is a
good place for initializing your application objects.
   - You can rename the load function to start, ready or initialize – it doesn’t matter.
What matters is that at this entry point we’re 100% guaranteed that all DOM
elements have been successfully loaded into memory and trying to access them
with JavaScript will not produce an error.
 - **EVENT'S**
```javascript
document.addEventListener("mouseover", myFunction);
document.addEventListener("click", someOtherFunction);
document.addEventListener("mouseout", someOtherFunction);
```

**3.1.1 Dos and Dont’s**
 - Do not write your code just in <script> tags, without entry point function.
 - Do use the entry point to initialize the default state of your data and objects.
 - Do make your program entry point either DOMContentLoaded, readyState or
the native window.onload method for waiting on media (see next,) depending on
whether you need to wait for just the DOM or the rest of media.
**.readyState**
 - For added safety you might also check the value of readyState property before
attaching the DOMContentLoaded event:
```javascript
<html>
    <head>
        <title> DOM Loaded.</title>
        <script type="text/javascript">
            function load() {
                console.log("DOM Loaded.");
            }
            if(document.readyState == "loading"){
            document.addEventListener("DOMContentLoaded", load);
            } else {
                load();
            }
        </script>
    </head>
    <body>
      <h1>HEAD</h1>
    </body>
</html>
```
**DOM vs Media**
  - We’ve just created a safe place for initializing our application. But because DOM
is simply a tree-like structure of all HTML elements on the page, it usually becomes
available before the rest of the media such as images and various embeds.
  - Even though <image src = "http://url" /> is a DOM element, the URL content specified in image’s src attribute might take more time to load.
  - To check if any non-DOM media content has finished downloading we can overload
the native window.onload event as shown in the following example

**window.onload**
 - With window.onload method, you can wait until all images and similar media
have been fully downloaded:

```javascript
<html>
    <head>Window media loaded.
    <script type = "text\javascript">
        window.onload = function(){

        }
    </script>
    </head>
    <body></body>
</html>
```

**Including External Scripts**
 - Let’s say we have the following definitions in
  my-script.js file:
```
let variable = 1;
function myfunction(){return 2;}
```
  - Then you can add them into your main application file as follows:
```javascript
<html>
    <head>
        <title>Include External Script</title>
        <script src="external.js"></script>
        <script type="text/javascript">
            let result= myfunction(); 
            console.log(variable);
            console.log(result);
        </script>
    </head>
    <body></body>
</html>
```

**Import**
  - Starting from ES6 we should use import (and export) keyword to import variables,
functions and classes from an external file.
  - Let’s say we have a file script.js and it has following definition of a mouse class.
```javascript
export function mouse(){
   console.log("Import successfully");
}
```

 - In order to make a variable, object or a function available for export, the export
keyword must be prepended to its definition.

 - Not everything in a module will be exported. Some of the items will (and should)
remain private to it. 
 - Be sure to prepend export keyword to anything you want to
export from the file. This can be any named definition.
``` javascript
script type = "module"
```
 - In order to export the Mouse class and start using it in the application, we must
make sure the script tag’s type attribute is changed to ”module” (this is required.)

```javascript
<html>
    <head>
        <title>Import Module</title>
        <script type="module">
            import{mouse}from"./script.js";
            mouse();
        </script>
    </head>
    <body>
    </body>
</html>
```
**Importing And Exporting Multiple Definitions**
  - It’s uncommon for a complex program to import only one class, function or variable.
  - Here is an example of how to import multiple items from two imaginary files

  ```javascript
  <html>
    <head>
        <title>Import Module</title>
        <script type = "module">
            import { mouse } from "./external.js";
            import {add, sub, mul, div } from "./export.js";
            mouse();
            console.log(mouse);
            add(5,10);
            console.log(add);
            sub(10,2);
            console.log(sub);
            mul(12,2);
            console.log(mul);
            div(15,6);
            console.log(div);
        </script>
    </head>
    <body></body>
</html>

  ```

  - The Mouse class were imported 
from script.js file. 
  - We’ve also imported some math functions add, subtract, divide and multiply
from export.js. 

```javascript
function add(a,b){
    return(a+b);
}
function mul(a,b){
    return(a*b);
}
function sub(a,b){
    return(a-b);
}
function div(a,b){
    return(a/b);
}
export{add, mul, sub, div}
```
**3.1.2 Dynamic Import**
 - Imports can be assigned to a variable since EcmaScript 10 (may not be available
in your browser yet, at the time of this writing.)
```javascript
<html>
    <head>
        <title>Dynamic imports</title>
        <script type="type/javascript">
            element.addEventListener('click',async()=>{
                const module = await import('./script.js');
                module.clickEvent();
            });
        </script>
    </head>
</html>

```

**3.2 Strict Mode**
  - The strict mode is a feature available since ECMAScript 5 that allows you to place
your entire program, or an isolated scope, in a ”strict” operating context. This
strict context prevents certain actions from being taken and throws an exception.
For example, in strict mode you cannot use undeclared variables.
  -  Without strict
mode, using an undeclared variable will automatically create that variable.
Without strict mode, certain statements might not generate an error at all – even
if they are not allowed – but you wouldn’t know something was wrong
```javascript
var variable=1;
delete variable;
```
  - Without strict mode on, code above will fail silently, variable will not be deleted,
and delete variable will return false but your program will continue to run.

**But what will happen in strict mode?**

  - Eliminates some JavaScript silent errors by changing them to throw errors.
  - Fixes mistakes that make it difficult for JavaScript engines to perform optimizations: strict mode code can sometimes be made to run faster than identical code that's not strict mode.

```javascript
"use strict";
var variable=1;
delete variable;

X Uncaught SyntaxError: Delete of an unqualified identifier in strict mode.
```
**Limiting ”strict mode” To A Scope**
 - The strict mode doesn’t have to be enabled globally. It is possible to isolate a
single block (or function) scope to strict mode:
```javascript
function strict_function(){
    'use strict';
    function inner(){console.log("me too");}
    return 'I am in strict mode.'+inner();
}
strict_function();
```
  - In a professional environment, it is common to have strict mode on, because it
can potentially prevent many bugs from happening and generally supports better
software practice.

**3.3 Literal Values**
  - The literal representation of a number can be the digit 1, 25, 100 and so on. A
string literal can be "some text";
You can combine literals using operators (+,-,/,*, etc.) to produce a single result.
  -  For example, to perform a 5 + 2 operation, you will simply use the literal number
values 5 and 2: 
```javascript
console.log(5+7);
console.log("Hello" + " there.");
console.log("username"+123456);
```
  - There is an array literal [] and object literal {}.
  - You can add {} + [] without breaking the program, but the results will not be
meaningful. These types of cases are usually non-existent.
  - Note: that a JavaScript function can be used as a value. You can even pass them
into other functions as an argument. We don’t usually y refer to them as function
literals, however, but rather function expressions.
   - The typeof(value) function can be used to determine type of the literal value.
You can also use typeof as stand-alone keyword without parenthesis: typeof x.
  - For example typeof 1 will return string "number" and typeof {} will return string
"object". But ”object” doesn’t mean its an object-literal – for example – typeof
new Number also returns "object" as does typeof new Array.

**Number(1) vs new Number(1)**
  - You can instantiate a value using constructor function associated with the type of
that value. But using literal values is more common:
```javascript
//literal values
console.log(1+1);
//using number function
console.log(Number(1)+Number(2));
//using number object constructor
console.log(new Number(1)+new Number(2));
//combination
console.log(1+ Number(2)+new Number(4));
```
3.4 Variables
Value Placeholders
Variables are placeholder names for different types of values.






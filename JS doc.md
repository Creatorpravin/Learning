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

Access to script at 'file:///C:/Users/sys/Documents/github/javascript/chapter%203/including%20external/script.js' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, chrome-extension, edge, https, chrome-untrusted.
script.js:1 
        
       Failed to load resource: net::ERR_FAILED
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
**3.4 Variables**
**Value Placeholders**
 - Variables are placeholder names for different types of values.
 - Keywords for defining variables include: **var, let and const:** but they don’t
determine variable’s type, only how they can be used. We’ll go over the rules in
more detail at a later time. 
 - When you assign 1 to a variable name the type of that variable automatically
 **Dynamic Typing**
  - JavaScript is a dynamically-typed language. It means that variables created using
var or let keywords can be dynamically re-assigned to a value of another type at
some point later in your JavaScript program.
  - In statically-typed languages doing that would generate an error.
Definition Or Declaration?
  - In the previous diagram we looked at a JavaScript variable declaration.
Some will argue that the definition is the declaration. But this type of logic
comes from statically typed languages, of which JavaScript is not. In statically
typed languages the declaration determines the type of the variable – it’s what
the compiler needs to allocate memory for the variable type (left hand side). But
JavaScript is a dynamically typed language – the variable type is determined by
the the type of value itself (right hand side).
  - Hence, the confusion. Is the left side the declaration, definition or both? These
types of details are more relevant in statically typed languages, but in JavaScript
(and other dynamically-typed languages) it might not make much sense.

**3.5 Passing Values By Reference**
  - Copying data from place to place is a common operation in computing. It is
natural to think that when we assign a value to a variable from another variable,
a copy is made.
  - But JavaScript assigns values by reference without actually making a copy of the
original value. Here is an example

```javascript
let x ={p:1};
let y=x;
x.p=2;
console.log(y.p);

```
  - Here we created variable x and assigned object literal {p: 1} to it.
  - This means that from now on the value of x.p will be equal 1.
  - A new variable called y was created and assigned x to it.
  - Now x has become a reference to y, not a copy.
  - From now on, any changes made to x will be also reflected in y.
  - This is why when we changed value of x.p to 2, y.p was also changed.
  - You can say that now y ”points” to the original object assigned to x variable.
  - Only one copy of {p: 1} existed in computer memory all along from start to finish
of this code block. Multiple assignments are chained by reference:
```javascript
let a ={p:5};
let b=a;
let c=b;
let d=c;
let f=d;
a.p=10;
console.log(f.p);
```
**3.6 Scope Quirks**
JavaScript has two known quirks when it comes to scope rules, that you might
want to know about to save debugging time later.
**Quirk 1 – let and const inside function vs. global variable**
A variable defined using let or const keywords inside a function cannot coexist
with global variable of the same name.

```javascript
let a = "global a";
let b = "global b";
 function x(){
     console.log("x();global b="+b);
     console.log("x();global a="+a);
     let a = 1;
 }
 x();

```
  - The let keyword doesn’t hoist definitions, and we have a global variable a, so
logically, inside function x() variable a should be taken from global scope, before
it is defined later with let a = 1 but that’s not what happens.
  - If variable a already exists inside a function (and it’s defined using let or const
keywords) then using a, prior its definition within the function will produce ReferenceError, even if global variable a exists!

**Quirk 2 – var latches onto window/this object, let and const don’t**
 - In global scope this reference points to instance of window object / global context.
When variables are defined using var keyword they become attached to window
object, but variables defined using let (and const) are not.

```javascript
console.log(this===window);
var c="c";//latches on to window("this" is global scope)
let d="d";//exists separately from "this"
console.log(c);
console.log(this.c);
console.log(window.c);

console.log(d);//c
console.log(this.d);//undefined
console.log(window.d);//undefined

```
# **Chapter 4**
## **Statements**
**4.0.1 Evaluating Statements**
  - A statement is the smallest building block of a computer program. In this chapter
we will explore a few common cases.
  - Definitions made with var, let or const keywords return undefined because they
behave only as value assignments: the value is simply stored in the variable name:
```javascript
let a = 1;
```
If, however, the assigned variable a is used as a stand-alone statement afterwards,
it will produce value of 1:
```javascript
a;
```
 - Statements usually produce a value. But when there isn’t anything to return, a
statements will evaluate to undefined, which can be interpreted as ”no value
```javascript
; //undefined
1; //undefined
"text"; //undefined
[]; //undefined
{}; //undefined
let a = 1; //undefined
let b = []; //undefined
let c = {}; //undefined
let d = new String("text"); //undefined
let e = new number(12345); //undefined
new String("text"); //"text"
new String(12345); //12345
let f = function() {return 1}; //undefined
f(); //1
let o = (a,b)=>a+b; //undefined
o(1,2); //3
fuction name(){} //undefined
```
 - Some evaluation rules make sense, but special cases should probably be just memorized. For example, what would it mean to evaluate an empty object literal?
 - According to JavaScript it should evaluate to undefined.
 - Yet, empty array brackets [] (a close relative to empty object literal) evaluate to
an empty array: [], and not undefined.

**4.0.2 Expressions**
 - Here is an expression: 1 + 1 that produces the value of 2:

```javascript
1+1; //2
```
 - Expressions don’t have to be variable definitions. You can create them
by simply using some literal values in combination with operators.
```javascript
let f = function () {return 1};
f();
```
  - Function f() evaluates to value 1, because it returns 1. This is why f() is often
referred to as a function expression.

# **Chapter 5**
## **Primitive Types**

**Primitive Types**
  - A primitive (primitive value, primitive data type) is data that is not an object and has no methods.
 - JavaScript has 7 primitive types: null, undefined, number, bigint, string,
boolean and symbol. Primitives helps us work with simple values such as strings,
numbers and booleans.
```javascript
let a = undefined;
let b = null;
let c =12;
let d = 40.3;
let e = 100n;
let f = "hello";
let g = Symbol();
console.log(typeof g);
```
  - Numbers, strings and booleans are basic value units. You can write them out
in literal form: a number can be 123 or 3.14, a string can be "string", or
a template string: ‘I have {$number} apples.‘ (note the back-tick quotes,
which allow you to embed variables into the string dynamically.) A boolean can
only be either true or false. You can combine primitive types using operators,
pass them to functions or assign them as values to object properties.
**Number(), BigInt(), String() and Boolean()** are primitive constructor functions. 

**5.0.1 boolean**
  - The boolean primitive can be assigned either true or false value. 
 ```javascript
 Boolean(10 > 9);
 ```
**5.0.2 null**

  - Running typeof operator on null will say it’s an ”object”.
  - Some believe this is a bug in JavaScript because null is not an object since it
doesn’t have a constructor. And they are probably right...

**5.0.3 undefined**
  - Undefined is a type of its own. It’s not an object. Just a value JavaScript will use
when you named a variable but don’t assign a value to it. 
  - Your hoisted variables
will also be automatically assigned a value of undefined.

**5.0.4 number** 
  - The number primitive helps us work with values in the numeric domain.
You can define negative and positive values, decimals (more commonly known as
floating-point numbers.) 
  - There is even a negative and positive Infinity value.
  - This makes more sense if you have some background in math.
NaN is technically a non-numeric value a statement can evaluate to. It’s available
directly from the Number.NaN But literally, it is exactly what it says it is: neither
"number" primitive nor Number() object. (It could be a "string", for example.)
Using typeof operator on a numeric value will produce "number" (It helps to note
that the return value is in string format.)
```javascript
typeof -1;
typeof 5;
typeof 7;

let number = new number(7);//undefined
typeof number;//object
typeof number.valueOf();//number
```
  - This example shows distinction between primitive literal value (-1, 5, 7, etc.) and
the Number object. Once instantiated, the value is no longer exactly a literal but
an object of that type.
To get ”number” type from the object use typeof on the valueOf method as
seen in the previous example typeof number.```valueOf();```

**5.0.5 bigint**
  - BigInt was added in EcmaScript10 and wasn’t available until Summer 2019.
  - In the past the maximum value of a number created using a number literal or the
Number() constructor was stored in Number.MAX SAFE INTEGER and was equal
to 9007199254740991.
  - A bigint type allows you to specify numbers greater than Number.MAX SAFE INTEGER.
```javascript
const limit = Number.MAX_SAFE_INTEGER;
limit+1;
limit+2;
const small = 1n;
const large = 1752500000129229n;
const integer = BigInt(1752500000129229);
const big = BigInt('1752500000129229');
big + 1;
```

**5.0.6 typeof**
 - Difference between numeric types:
```javascript
typeof 10;//number
typeof 10n;//bigint
```
 - Equality operators can be used between the two types
```javascript
10n === BigInt(10);//true
10n == 10;//true
```
- Math operators only work within their own type

**5.0.7 string**
  - The string value is defined using any of the available quote characters: double
quotes, single quotes, and back-tick quotes (Located on tilde key.) You can nest
double quotes inside single quotes, and the other way around.
  - Running typeof on a string value returns "string":
  - You can also use String constructor function to build an object of string type:
 ```javascript
 typeof "text"; //string
typeof "JavaScript book";//string
typeof "price"+250;//string

let text = new Text("hello.");//undefined
typeof text;//object
typeof text.valueOf();//string
 ```
  - Note that the first typeof returns "object", because at this point the object is
instantiated (this is different from the primitive’s literal value which is still just a
"string" primitive). To get the value of the instantiated object use valueOf()
method and use typeof string.valueOf() to determine the object’s type.

**5.0.8 Template Strings**
  - Strings defined using the backtick quotes have special function.
  - You can use them to create Template Strings (also known as Template Literals)
to embed dynamic variable values inside the string:
 ```javascript
  let apple = 10;
let name =  `There are ${apple}, apples in the basket`;
console.log(name);
let firstName = "John";
let lastName = "Doe";
let text = `Welcome ${firstName}, ${lastName}!`;
console.log(text);
 ```
  - The back-tick cannot be used to define an object-literal property name (You still
have to use either single or double quotes.)

**Creative Use Case**
  - Template strings can be used to solve the problem of forming a message that has
proper language form, based on a dynamic number. One of the classic cases is
forming an alert message sentence.
```javascript
for (let alerts =0;alerts<4;alerts++){
    let one = (alerts==1);
    let is = one ? "is" : "are";
    let s = one == 1 ? "" : "s";
    let message = `There ${is} ${alerts} alert${s}`;
    console.log(message);
}
```
  - Whenever there is only 1 alert, the trailing "s" in the word "alerts" must be
removed. But we don’t want to create a second string just to cover one case.
Instead, we can calculate it dynamically. We also need to decide which verb should
be used ("is" or "are") based on the number of alerts.

```console
VM126:6 There are 0 alerts
VM126:6 There is 1 alert
VM126:6 There are 2 alerts
VM126:6 There are 3 alerts
```
  - Here the **ternary operator** consisting of ? and : is used.
You can think of ternary operator as an inline **if**-statement. 
  - It doesn’t need {}
brackets because it doesn’t support multiple statements:
 ```javascript
 let is = one ? "is" : "are";
 ```
 - Question mark can be interpreted as "if-then" or as "if the previous statement
evaluates to true" and the colon : can be interpreted as "else".

**5.0.9 Symbol**
  - The Symbol primitive provides a way to define a completely unique key.
Symbol doesn’t have a constructor and cannot be initialized using new keyword:
Instead, just an assignment to Symbol will create a new symbol with a unique ID:
  - The ID, however, is not the used-defined string "sym", it is created internally.
  - This is demonstrated in the following example.
  - At first it might be surprising that the following statement evaluates to false:
Whenever you call Symbol(’sym’) a unique symbol is created. The comparison
is made between two logically distinct IDs and therefore evaluates to false.
Symbols can be used to define private object properties. This is not the same
as regular (public) object properties. However, both public and private properties
created with symbols can live on the same object:
```javascript
let sym = new Symbol('sym'); // type error
let sym = Symbol('sym');//symbol created
Symbol('sys') === Symbol('sys') //flase

let sym1 = Symbol('unique');
let bol = Symbol('dictinct');
let one = Symbol('only-one');
let obj = {property:"regular property",[sym1]:1,[bol]:2};
obj[one]=3;//add the property
console.log(obj);
//hide properties
```
  - Here we created an object obj, using object literal syntax, and assigned one of
its properties property to a string, while second property was defined using the
[sym] symbol created on the first line. [sym] was assigned value of 1. Second
symbol property [bol] was added in the same way and assigned value of 2.
Third object symbol property [one] was added directly to the object via obj[one].
Printing the object shows both private and public properties:
- Private (symbol-based) properties are hidden from Object.entries, Object.keys
and other iterators (for example for...in loop):

```javascript
for (let prop in obj)
console.log(prop+ ":" +obj[prop]);//property: regular property
console.log(Object.entries(obj));//(2) ["property","regular property"]
console.log(JSON.stringify(obj));//{"property":"regular property"}
console.log(Object.getOwnPropertySymbols(obj));//0: Symbol(unique)
//1: Symbol(dictinct)
//2: Symbol(only-one)
//length: 3
```
  - In addition symbol properties are also hidden from JSON.

  - Why would we want to hide symbol-based properties from JSON stringify?
  - Actually it makes sense. What if our object needs to have private properties that
are only relevant to how that object works, and not what data it represents? These
private properties can be used for miscellaneous counters or temporary storage.
  - The idea behind private methods or properties is to keep them hidden from the
outside world. They are only needed for internal implementation. Private implementation is rarely important when it comes to marshalling objects.
  - But symbols can be exposed via Object.getOwnPropertySymbols method:
  - Note that you probably shouldn’t use Object.getOwnPropertySymbols to expose properties that are intended to be private. Debugging should be the only use
case for this function.
  - You can use symbols to separate your private and public properties. This is
like separating ”goats from the sheep” because even though they provide similar functionality, symbols will not be taken into account when used in iterators or
  - console.log function.
Symbols can be used whenever you need unique IDs. Hence, they can also be used
to create constants in enumerable lists of IDs:
```javascript
const seasons={
    Winter:Symbol('Winter'),
    Spring:Symbol('Spring'),
    Summer:Symbol('Summer'),
    Autumn:Symbol('Autumn')
};
```
**Global Symbol Registry**
  - As we saw earlier Symbol("string") === Symbol("string") is false because
two completely unique symbols are created.
  - But there is a way to create string keys that can overwrite symbols created using
the same name. There is a global registry for symbols, that can be accessed using
methods Symbol.for and Symbol.keyFor.

```javascript
let sym = Symbol.for('age');
let bol = Symbol.for('age');
let obj = {};
obj[sym]= 20; 
obj[bol]=25; //25
console.log(obj[sym]); //25 tide eachother by key 'age'

```
  - The private symbolic object property obj[sym] outputs the value of 25 (which
was originally assigned to obj[bol]) when it was defined, because both variables
sym and bol are tied to the same key "age" in global symbol registry.
  - In other words the definitions share the same key.

**Constructors And Instances**
  - There is a distinction between constructors and instances. The constructor
function is the definition of a custom object type. The instance is the object that
was instantiated from that constructor function using the new operator.
  - Let’s create a custom Pancake constructor, containing one object property number
and one method bake() which will increase pancake number by 1 when called:
```javascript
let Pancake = function (){
    //create object property
    this.number = 0;
    //create object method
    this.bake = function() {
        console.log("Baking the pancake...");
        //Increase number of pancake baked:
        this.number++;
        
    };
}
```
 - Note that properties and methods are attached to the object via this keyword
The constructor is only a design of the object type. In order to start using it, we
have to instantiate it. When we do that, an instance of the object is created in
computer memory:
```javascript
let pancake = new Pancake();
```
 - Let’s bake 3 pancakes by using bake() method which increments pancake counter:
```javascript
pancake.bake();
pancake.bake();
pancake.bake();
```
  - 3 pancakes successfully baked! Let’s take a look at pancake.number now:
 ```javascript
 console.log(pancake.number);
 ```
 - You can look up the constructor function’s type. The constructor function Pancake
is an object of type Function. This is true of all custom objects. It makes sense
because the function itself is the constructor:
```javascript
console.log(Pancake.constructor);//function Function(){}
```
  - But, if you output constructor via the instantiated object, it will show you the
entire function body in string format:

```javascript
console.log(Pancake.constructor);//function Function(){}
//ƒ (){
    //create object property
    //this.number = 0;
    //create object method
    //this.bake = function() {
        //console.log("Baking the pancake...");
        //Increase number of pancake baked:…

/*let body="cosole.log('Hello from f() function!')";
let f = new function(body);
f();*/
```
  - You can actually create a brand new function by supplying the body in string
format to Function constructor:
```javascript
let body="cosole.log('Hello from f() function!')";
let f = new function(body);
f();
```
  - This tells us that Function is the constructor for creating JavaScript functions.
But when we created our own Pancake function, Pancake became the constructor
of our custom class that we could also initialize using the new keyword.

**5.0.10 Executing Methods On Primitive Types**
**Parenthesis And Object Property Access**
  - The parenthesis operator gives you control over which statement should evaluate
first. That’s its primary purpose.
  - For example statement 5 * 10 + 2 is not the same as 5 * (10 + 2).
  - But sometimes it is used to access a member method or property. Which is
demonstrated in the next source code listing.
You can execute methods directly on the literal values of primitive types. Which
automatically converts them to objects, so that the method can be executed.
  - In some cases – like with the primitives of type "number" – we must first wrap
the literal value in parenthesis, or you’ll freeze your program.
```javascript
//1.toString();//This will freeze
(1).toString(); //"1"
"hello".toUpperCase(); //"HELLO"
("hello").toUpperCase(); 
new Number(1).toString();//"1"
```
  - A literal is just a literal value. By accessing its properties, it turns into a reference
to the object instance so you can execute object methods on that value.

**Chaining Methods**
  - Because in JavaScript functions can return this keyword, or any other value,
including functions, it’s possible to chain multiple methods using the dot operator.

```javascript
"hello".toUpperCase().substr(1,4);//"ELLO"
```

# **Chapter 6**
**Type Coercion Madness**
  - When learning JavaScript from scratch you may be puzzled by some decisions
made by the language when it comes to evaluating statements.
  - For example, what will happen if we sporadically add up different types of values
and stitch them together using the + operator?

```javascript
console.log(null+{}+true+[5]);
```
```console
null[object Object]true5
```
  - A string? This might seem confusing. After all, not a single value in this statement
is a string! So how did that happen?
  - *Answer:* When + operator encounters objects of incompatible type, it will attempt
to coerce those objects to their values in string format. In this case, leaving us
with a new statement: "null[object Object]" + true + [] + [5].
  - Furthermore, when + operator encounters a string at least on one side of the
operator, it will try to coerce the other side to string and perform string addition.
  - Calling .toString on true results in "true". Calling .toString on empty array
brackets [] when the other side of operator is also a string evaluates it to "" which
is why it appears missing from the result. And finally adding [5] to a string calls
[5].toString which results in "5".

**6.0.1 Examples of Type Coercion**
 - Here are some classic examples of type coercion

```javascript
let a = true + 1; //2
let b = true + true ; //2
let c = true + false; // 1+0 = 1
let d = "Hello" + " " + "there"; //Hello there
let e = "username" + 113215 ; //username113215
let f = 1 / "string";// NaN (not a number)
let g = Nan === Nan ; // false
let h = [1]+[2]; // "12"
let i = Infinity; // Infinity
let j = [] + []; //""
let k = [] + {}; // [object object]
```
  - JavaScript will try to come up with best value available if you supply meaningless
combinations of types to some of its operators.
After all, what would it mean to ”add” an object literal {} to an array []? Exactly
  - it doesn’t make any sense. But by evaluating to object [] at least we don’t
break the code in that one little odd case where it may happen.
  - This safety mechanism will prevent the program from breaking. In reality, however,
these types of cases will almost never happen. We can treat majority of these cases
as examples – not something you should be actually trying to do in code.

**Type Coercion In Constructors**
  - Coercion also occurs when we provide an initialization value to a type constructor:
  - In the last two cases we supplied an array literal {} and an object literal [] to
Boolean constructor. What does this mean? Not much, but the point is that at
least it evaluates to true in this odd case.
  - This is just a safety net to prevent bugs.
 ```javascript
 let a = Boolean(true); //true
let b = Boolean([]); //false
let c = Boolean({});//false
let d  = Boolean(false); // false
let e = Boolean(Nan); // false
let f = Boolean(null); // false
let g = Boolean(undefined); // false
let h = Boolean(''); // false
let i = Boolean(0); // false
let h = Boolean(-0); // false
 ```
  - Meaningless values still evaluate to either true or false, because these are the
only values available for boolean types.
Other built-in data type constructors behave in the same way. JavaScript will try
to coerce to an ideal value specific to that type.

**Type Coercion**
 - Coercion is the process of converting a value from one type into another. For
example, number to string, object to string, string to number (if the entire string
consists of numeric characters) and so on...
 - But when values are used together with different operators not all cases are
straightforward to the untrained eye.
 - To someone new to the language, the following logic might seem obscure:
```javascript
[] = []; //false
```
 - Let’s say that it is false because two instances of [] are not the same, because
JavaScript == operator tests objects by reference and not by value.
```javascript
let a = []; 
a == a ; //true
```
 - But this statement evaluates to true because variable a points to the same instance
of the array literal. They refer to the same location in memory.
 - But what about cases like this? Even though you would never write code like this
in production environment, it calls for understanding of type coercion:
```javascript
[] == ![]; //true
```
  - JavaScript will often coerce different types of values to either strings or numbers.
The Boolean type is no exception:
```javascript
true + false; //1
```
  - The above statement is the same as 1 + 0. And here’s the absolute classic:
```javascript
NaN == NaN;//false
```
 - These types of cases might appear bizarre at first, but as your knowledge of types
and operators deepens it will start to make a lot more sense.
 - Let’s start simple. The unary plus and minus operators force the value to a number.
If the value is not a number, NaN is generated:
```javascript
const s = "text";
console.log(-s); //NaN 
```
 - Here unary minus (-) struggles to convert the string "text" to a number. What
does -"text" mean anyway? So it returns NaN because ”text” is not a number.
 - Here is the same logic demonstrated using the Number type function:
```javascript
Number("text"); //NaN ("text" is not a numeric string)
Number("1"); //1 ("1" is numeric string)
```
  - But when unary minus (-) is applied to a number, it produces expected value:

```javascript
const s = 1;
console.log(-s); //-1
const t = 1;
console.log(+t); //1
```
  - This rule is specific to the unary operator.

**Number And String Arithmetics**
  - Naturally the arithmetic + operator requires two values.
```javascript
5+5; //10
```
 - If both values are integers, arithmetic operation is performed. If one of them is
a string then coercion happens and string addition is invoked.
 - If the type of the two values provided to the arithmetic + operator is different, this
conflict must be resolved. JavaScript will use type coercion to change one of
the values before evaluating the entire statement to a more meaningful result.
  - What will happen if left value is a string and right value is a number?
 ```javascript
 "1"+1;//"11"
 ```
  - Here + is treated as a string addition operator. The right value is converted to
"1" via String(1) and then the statement is evaluated as follows:
```javascript
"1"+"1"; //"11"
```
 - In JavaScript there are actually three + operators: unary, arithmetic and string.
 - Here JavaScript treats + not as the unary addition operator, but as the arithmetic
addition operator instead. But... when it sees that one of the values is a string, it
invokes the string addition operator. It makes no difference whether the string is
on the left or right side. The statement still evaluates to a string
```javascript
l + "ol"; //"lol"
```
 - Operators follow specific associativity rules. Like + and most other operators, the
arithmetic addition operator (+) is evaluated from left to right:
```javascript
1+1; //2
```
 - But the assignment operator is evaluated in right to left order:
```javascript
let n = 2; //undefined
```
 - Note that in example above, while N is assigned value of 2, the statement itself
evaluates to undefined.
```javascript
n;//2
```

**6.0.2 Adding Multiple Values**
  - Often you will encounter statements tied together by multiple operators. What
should the following statement evaluate to?
```javascript
1+1+1+1+2+""; //"6"
```
 - First, all of the purely numeric values will be combined, ending up with the sum
of 5 on the left hand side and "" on the right hand side
```javascript
5+"";
```
 - But this is still not enough to produce the final result. Adding a numeric value to a
string value will coerce the numeric value to a string and then add them together:
 - Finally we arrive at "5" in string format.
When adding numbers and strings, numeric values always take precedence. This
seems to be a trend in JavaScript. In the next example we we will compare numbers
to strings using the equality operator. JavaScript chooses to convert strings to
numbers first, instead of numbers to strings.

**6.0.3 Operator Precedence**
  - Some operators take precedence over others. What this means is that multiplication will be evaluated before addition.
  - Let’s take this statement for example:
```javascript
1+1+1+2*"";//3
```
 - Several things will happen here.
The string "" will coerce to 0 and 2 * 0 will evaluate to 0.
```javascript
1+1+1+2*"";
1+1+1+2*0;
1+1+1+0;
3+0;//3
```

**6.0.4 String To Number Comparison**
 - When it comes to equality operator == numeric strings are evaluated to numbers
in the same way the Number(string) function evaluates to numbers (or NaN).
 - According to EcmaScript specification, coercion between a string and a numeric
value on both sides of the == operator can be visualized as follows.

**Comparing Numeric String To Number**

```javascript
1 == "1"; //true
"1" == 1; //true
```

**Comparing Non-Numeric String To Number**
  - If the string does not contain a numeric value, it will evaluate to NaN and therefore
further evaluating to false:
```javascript
1 == "a"; //fab nlse
```
**Other Comparisons**
  - Other comparisons between different types (boolean to string, boolean to number, etc) follow similar rules. As you continue writing JavaScript code, you will
eventually develop intuition for them and it will become second nature.
  - The operator precedence and associativity table on the next page might help you
when things get tough.

**6.0.5 Operator Precedence & Associativity Table**
  - There are roughly 20 operator precedence levels. Parenthesis () overrides the
natural order. Red values are first in associativity order: for example, subtraction
operator subtracts blue from red. Assignment operators follow right to left order.
  - Consider an expression describable by the representation below. Note that both OP1 and OP2 are fill-in-the-blanks for OPerators.
  ```javascript
  a OP1 b OP2 c
  ```
    - If OP1 and OP2 have different precedence levels (see the table below), the operator with the highest precedence goes first and associativity does not matter. Observe how multiplication has higher precedence than addition and executed first, even though addition is written first in the code.
```javascript
console.log(3 + 10 * 2);   // logs 23
console.log(3 + (10 * 2)); // logs 23 because parentheses here are superfluous
console.log((3 + 10) * 2); // logs 26 because the parentheses change the order

```
 - **The mathematical operation of * * raising a quantity to a power.**
```javascript
console.log(3 + 4 * 5); // 3 + 20
// expected output: 23

console.log(4 * 3 ** 2); // 4 * 9
// expected output: 36

let a;
let b;

console.log(a = b = 5);
// expected output: 5
```

  - Associativity flows in either left-to-right or right-to-left direction: it determines
the order of the operation, usually for operators that require more than one value

**6.0.6 L-value and R-value**
  - In many computer languages values on the left and right side of the operator are
referred to as L-value and R-value. In EcmaScript spec they are often referred
to as x and y values.
**Assignment Operator**
  - The assignment operator takes the R-value and transfers it over to L-value, which
is usually a variable identifier name.
**Arithmetic Addition Operator**
But the arithmetic addition operator takes the L-value and adds R-value to it.
**6.0.7 null vs undefined**
  - The null primitive is not an object (although some may believe it is,) – so it
doesn’t have a built in constructor, like some of the other types. Luckily, we can
(and should) use its literal value: null.
Think of null as a unique type for explicitly assigning a ”nothing” or ”empty”
value to a variable. This way it doesn’t end up undefined.
  - If you don’t assign a variable to null, its value will be undefined by default:
```javascript
 let bike;
  console.log(bike);//undefined
```
  - To same effect, you can also explicitly assign variable to undefined:
  ```javascriptmd file code format
  let bike=undefined;
  console.log(bike);//undefined

  ```
  - But that’s something we should avoid. If the value is unknown at the time of
variable definition it is always best to use null instead of undefined.
  - The null keyword is used to assign a temporary default value to a variable before
it’s populated with actual object data at a later time in your program.

**Initialize or Update**
  - In a real-case scenario the null value can help us determine whether the data needs
to be initialized for the first time, or existing data merely needs to be updated.
We’ll take a look at a practical example in the next source code listing.
59
  - Let’s take a look at this scenario:
 ```javascript
 let bike = null;
class Motorcycle{
    constructor(make,model,year){
       this.make = make;
       this.model = model;
       this.year = year;
       this.features = null;
    }
    getFeatures(){
        if(this.features == null){
            this.features = {/* get features from database */}
        } else {
            this.features = {/* get features from database */}
        }
    }
}
bike = new Motorcycle("kawasaki","z900RS CSFE",2019);
bike.getFeatures();
 ```
 - Here we assigned null to bike. Later at some point in code, the variable was
instantiated with a real object. At no point in our program bike was undefined,
even before it was initialized for the first time.
 - Inside the object itself, the this.features property was also assigned to null.
 - Maybe at a later time, we can download feature list from a database. Until then,
we can be sure that feature object was not yet populated.
 - This gives us a distinction between two classic cases: downloading data for the first
time (if this.features == null) or updating existing data (that has already
been downloaded at some point in the past.)

**7.0.1 Scope**
  - Scope is simply the area enclosed by {} brackets. But be careful not to confuse it
with the identical empty object-literal syntax.
  - There are 3 unique scope types:
  - The global scope, block scope and function scope. Each expects different things
and has unique rules when it comes to variable definitions.
  - Event callback functions follow the same rules as function scope, they are just
used in a slightly different context. Loops can also have their own block-scope.

**7.1 Variable Definitions**
**Case-Sensitivity**
  - Variables are case-sensitive. This means a and A are two different variables:
```javascript
let a = 1;
let A = "hello";

console.log(a); //1
console.log(A); //hello
```
**Definitions**
 - Variables can be defined using var, let or const keywords.
Of course, if you tried to refer to a variable that wasn’t defined anywhere, you
would generate a ReferenceError error ”variable name is not defined”:
```javascript
console.log(apple);//ReferenceError: apple is not defined
{

}
```

  - Let’s use this setup to explore variable definitions using var keyword and hoisting.
  - Prior to let and const the traditional model allowed only var definitions:

  - Let’s use this setup to explore variable definitions using var keyword and hoisting.

  - Prior to let and const the traditional model allowed only var definitions
```javascript
var apple = 1;
{
  console.log(apple);//1
}
```
 - Here apple is defined in global scope. But it can also be accessed from an inner
block-scope. Anything (even a function definition) defined in global scope becomes
available anywhere in your program. The value propagates into all inner scopes.
 - When a variable is defined in global scope using var keyword, it also automatically
becomes available as a property on window object.

**Hoisting**
  - If apple was defined using var keyword inside a block-scope, it would be hoisted
back to global scope! Hoisting simply means ”raised” or ”placed on top of”.
  - Hoisting is limited to variables defined using var keyword and function name defined using function keyword.
  - Variables defined using let and const are not hoisted and their use remains limited
only to the scope in which they were defined.
  - As an exception, variables defined var keyword inside function-level scope are not
hoisted. Commonly, when we talk about hoisting block-scope is implied.
  - We will talk more about hoisting in just a moment!
  - Likewise, variables defined in global scope will propagate to pretty much every
other scope defined in global context, including block-level scope, for-loop scope,
function-level scope, and event callback functions created using setTimeout,
setInterval or addEventListener functions.
```javascript
console.log(apple); 
{
  var apple=1;
}
```
  - Variable apple is hoisted to global scope. But the value of the hoisted variable is
now undefined – not 1. Only its name definition was hoisted.
  - Hoisting is like a safety feature. You should not rely on it when writing code. You
may not retain the value of a hoisted variable in global scope, but you will still
save your program from generating an error and halting execution flow.
 - Thankfully, hoisting in JavaScript is automatic. When writing your program more
than half of the time, you won’t even need to think about it.

**Function Name Hoisting**
 - Hoisting also applies to function names. But variable hoisting always takes precedence. We’ll see how that works in this section.
 - You can call a function in your code, as long as it is defined at some point later:

**Function Name Hoisting**
  - Hoisting also applies to function names. But variable hoisting always takes precedence. We’ll see how that works in this section.
  - You can call a function in your code, as long as it is defined at some point later:
  ```javascript
  fun();
  function fun(){
    console.log("Hello from fun() function.");
  }

  ```
   -Note that the function was defined after it was called. This is legal in JavaScript.
  - Just make sure you understand that it happened because of function name hoisting
  - It goes without saying if the function was already defined prior to being called,
there’d be no hoisting but everything would still work as planned. Statements inside
a function’s body are executed when the function is called by its name. Nameless
functions can still be assigned as values themselves. (See next example.)
```javascript
function fun(){
  console.log("Hello from fun() function 1.");
  }
  //The code above is the same as:
  var fun = function(){
    console.log("Hello from fun() function 2.");
  }
```
 - It is possible to assign an anonymous function expression to a variable name.
It’s important to note, however, that anonymous functions that were assigned to
variable names are not hoisted unlike named functions.
 - This valid JavaScript code will not produce a function redefinition error.   
 - The
function will be simply overwritten by second definition.
 - Even though fun() was a function, when we created a new variable fun and
assigned another function to it, we rewired the name of the original function.
 - Having said this, what do you think will happen if we call fun() at this point?
 ```javascript
 fun();
 ```
```javascript
"Hello from fun() function 2."
```
 - You might think that the following code will produce a redefinition error:

```javascript
function fun(){
  console.log("Hello from fun() function 1.");
  }
  //The code above is the same as:
  var fun = function(){
    console.log("Hello from fun() function 2.");
  }

```
  - However, this is still perfectly valid code – no error is generated. Whenever you
have two function defined using function keyword and they happen to share the
same name, the function that was defined last will take precedence.
  - In this case if you call fun(); the console will output the second message:
```javascript
"Hello from fun() function 2."
```
  - This actually makes sense.
In following scenario variable name will take precedence over function definitions
even if it was defined prior to the second function definition with the same name:
```javascript
 var fun = function(){
    console.log("Hello from fun() function 2.");
  }

function fun(){
  console.log("Hello from fun() function 1.");
  }
  //The code above is the same as:
 
```
  - And now let’s call
  
  
   fun() to see what happens in this case:
 ```javascript
 fun();
 ```
 But this time the output is:
```javascript
 "Hello from fun() function 1."
```
 - You can see the order in which JavaScript hoists variables and functions. Functions
are hoisted first. Then variables.
**Defining Variables Inside Function Scope**
 - At this point you might want to know that variables defined inside a function will
be limited only to the scope of that function. Trying to access them outside of
the function will result in a reference error:
```javascript
//define a variable inside a block scope?
function fun()
{
var apple=1;
}
console.log(apple);//ReferanceError: apple is not defined
```

**Simple scope accessibility rules:**
 - Here var is defined in Global Scope, but its value propagates into the
block scope as well. What actually happens is, when block scope 1 cannot find
var definition in within its own brackets
  - Defining variables inside function scope is basically one way street
ordeal. Nothing can leave the confines of a function into its parent scope.
  - Functions enable closure pattern, because their variables are concealed from global
scope, but can still be accessed from other function scopes within them:
  - Nothing can get out of function scope into its outer scope. This
enables the closure pattern. We’ll take a look at it in just a moment!
  - The idea is to protect variables from the global scope but still be able to call the
function from it. We’ll take a look at this in greater detail in just a moment

**7.1.1 Variable Types**
 - JavaScript is a dynamically-typed language.
 - The type of the variable (defined using var or let keyword) can be assigned and
changed at any time during the run-time of your application, after it was already
compiled by browser’s JavaScript engine.
 - The keywords var, let and const do not determine the variable’s type. Instead,
they determine how the variable can be used: can it be used outside of the scope
in which defined? Can it be re-assigned to another value during run-time? For
example, var and let can, but const can’t.
**var ES5** 
  - The var keyword is still with us from original specification. You should probably
start using let and const instead. For the most part it is still available but only
to support legacy code.

**let ES6**
  - let defines a variable but limits its use to the scope in which it was defined.

**const ES6**
  - const is the same as let but you can’t re-assign it to a new value once defined.

**7.1.2 Scope Visibility Differences**
**No Difference In Global Scope**
 - When variables are defined in global scope there is no differences between var, let
and const in terms of scope visibility.
- They all propagate into inner block-level, function-level and event callback scopes:
 - Keywords let and const limit variable to the scope in which they were defined:
 - Variables defined using let and const are not hoisted. Only var is.

 **In Function Scope**
  - However, when it comes to functions, all variable types, including var remain
limited to their scope:
  - You cannot access variables outside of the function scope in which they were
defined regardless of which keyword was used.

**Closures**
  - A function closure is a function trapped inside another function:
  - Calling add() increments counter. This is not possible using other scope patterns.
  - add() returns an anonymous function which increments
the counter variable that was defined in an outer scope.
  - Let’s try to use that pattern to create our own closure:
 ```javascript
 var plus = (function(){
    var counter = 0;
    return function(){
        counter +=1;
        return counter;
    }
})();
plus();
 ```
  - The plus() function is defined by an anonymous function that executes itself.

**Why Are We Doing This?**
  - Inside the scope of plus, another anonymous function is created – it increments a
private variable counter and sends the result back into global scope as a function’s
return value.
  - Take away: Global Scope cannot directly access nor modify the counter variable
at any time. Only the code inside the closure allows its inner function to modify
the variable, still, without the variable leaking into Global Scope. . .
  - The whole point is that Global Scope does not need to know or understand how
the code inside plus() works. It only cares about receiving the result of plus()
operation so it can pass it to other functions, etc.
  - So why did we even bother explaining them? Beside that closures are one of the
top-asked questions on JavaScript interviews?
  - Closures are similar to the idea of encapsulation – one of the key principles of
Object Oriented Programming, where you hide the inner workings of a function or
a method from the environment from which it was called.
  - This idea of making some variables private is key to understanding many other
programming concepts.
  - If you think about it, this is exactly why let was added to JavaScript. It provides
automatic privacy for variables defined in block-level scope. Variable privacy is a
fundamental feature of many programming languages in general.

**In Block-level Local Scope**
  - The let and const keywords conceal variable visibility to scope in which they were
defined and its inner scopes.
 - Scope visibility differences surface when you start defining variables inside local
block-level scope or function-level scope.

**In Classes**
  - The class scope is simply a placeholder. Trying to define variables directly in class
scope will produce an error:
```javascript
class cat { 
  let property = 20; //"Unexpexted token" Error
  this.property = 2;
  }
```
  - Here are the proper places for defining local variables and properties. Note, in
class methods, let (or var or const) only create a local variable to that scope.
Therefore, it cannot be accessed outside of the method in which it was defined.
```javascript
 class cat {
        constructor(){
            let property = 1; //Ok: local variable 
            this.something = 2;//Ok: object property
        }
        mehtod(){
            console.log(this.property); //undefined
            console.log(this.something);//1
        }
    }
```
  - In classes variables are defined inside its constructor function or its methods:  

**7.1.3 const**
  - The const keyword is distinct from let and var.
  - It requires assignment on definition:
```javascript
let a;
console.log(a);
const b;//Uncaught SyntaxError: Missing initializer in const declaration
```
  - This makes sense because value of const cannot be reassigned.
```javascript
const speed_of_light = 186000;
speed_of_light = 1; //VM1126:2 Uncaught TypeError: Assignment to constant variable.
    at <anonymous>:2:16

```
  - It’s still possible to change values of a more complex data structure such as Array
or objects, even if variable was defined using const. Let’s take a look!

**7.1.4 const and Arrays**
 - Changing a value in the const array is still allowed:
```javascript
const A = [];
A[0] = 5; //ok
A = [2]; //Uncaught SyntaxError: Identifier 'A' has already been declared
```
  - You just can’t assign any new objects to the original variable name again.

**7.1.5 const and Object Literals**
  - Similar to arrays, when it comes to object literals, const only makes the definition
constant. But it doesn’t mean you can’t change values of the properties assigned
to a variable that was defined with const:
```javascript
// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};

// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson";
console.dir(car);
//IT WILL CREATE ERROR
const car = {type:"Fiat", model:"500", color:"white"};

car = {type:"Volvo", model:"EX60", color:"red"};    // ERROR
```

**Conclusion**
  - In case of a more complex data structure (object or array) you can think of const
as something that does not allow you to reassign it to a new object again. The
variable is locked to the original object, but you can still change the value of its
properties (or indexes, in case of an array.)
  - If the value of a variable was defined with const and a single primitive (string,
number, boolean,) such as speed of light, PI, etc, it cannot be changed.

**7.1.6 Dos and Dont’s**
  - Do not use var unless for some reason you want to hoist the variable name.
(These cases are rare and usually don’t comply with good software design.)
  - Do use let and const instead of var, wherever possible. Variable hoisting (variables defined using var) can be the cause of unpredictable bugs, because only the
variable name is hoisted, the value becomes undefined.
  - Do use const to define constants such as PI, speed of light, tax rate, etc.
 values that you know shouldn’t change during the lifetime of your application.

# **Chapter 8**
## **Operators**
**8.0.1 Arithmetic**
```console
+ Additon 
- Subraction
* Multiplication
/ Division
% Modulus
++ Increment
-- Decrement
```

  - The arithmetic operators are pretty basic. They do exactly what you expect.
  - The modulus operator returns the number of times one number fits into the other.
Here, 4 fits into 10 only 2 times – it is also often used to determine the remainder.
  - You can create statements without assigning the value to a variable name. It is
possible to type them directly into your browser’s developer console for practice:
 - That works in Chrome console. But in your source code, evaluating simple statements is meaningless:

```javascript
1+1; //2
1-2; //-1
8/2; //4
5*3; //15
```
 - More often, you will perform operations directly on variable names:
```javascript
let variable = 1; // undefined
variable + 2; //3
variable - 1; //0
variable / 2; //0.5
variable * 5; //5
variable * variable; //1
variable++; //1
variable++; //2
variable++; //3
variable--; //4
console.log(variable);
```
**8.0.2 Assignment**
```javascript
= Assignment //x=1;
+= Addition //x+=2;
-= Subraction //x-=1;
*= Multiplication //x*=2;
/= Division //x/=2;
%= Modulus //x%=1;

```

  - Assignment operators assign a value to a variable. There are several assignment
operators that can also combine assignment with one of the arithmetic operations.

**8.0.3 String**
  - Strings can be assigned to variable names or each other using the + operator which
we earlier saw used as arithmetic addition. But when one or both of the values on
either side of + operator are strings, it is treated as a string addition operator.
```javascript
x="a"; //a
x +="b"; //'ab'
'x'+'y'; //'xy'
console.log(x);
```
  - In this context the += operator can   be thought of as string concatenation operator.

**8.0.4 Comparison**
```javascript
1 == 1 ;//true
'1' == 1 ; //true Equality
'1' == '1' ; //true
1 === 1 ; //true
'1' === 1 ; //flase Equality of value and type
'1' === '1' ; //true
1 != 1 ; //false
1 != 2 ; //true Equality
2 > 1 ; //true
5 < 7 ; //true
2 >= 1; //true
2 <= 1; //flase
```
  - Triple equality operator checks for value and type.

**8.0.5 Logical**
```javascript
(5<1 && 3>2)//false AND both must be satisfied
1==1 || 2==2//true OR any one satisfies 
!true //false NOT EQUAL TO
!(1 == 2) // true

```
 - Logical operators are used to determine logic between the values of expressions or
variables.


**8.0.6 Bitwise**
  - &	AND	= Sets each bit to 1 if both bits are 1
  - |	OR =	Sets each bit to 1 if one of two bits is 1
  - ^	XOR =	Sets each bit to 1 if only one of two bits is 1
  - ~	NOT =	Inverts all the bits
  - <<	Zero = fill left shift	Shifts left by pushing zeros in from the right and let the leftmost bits fall off
  - ```>>```	Signed right shift =	Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
  - ```>>>```	Zero fill right = shift	Shifts right by pushing zeros in from the left, and let the rightmost bits fall off
 ```javascript
 5 & 1	// 1 =	0101 & 0001	- 0001
  5 | 1	// 5 =	0101 | 0001	- 0101
  ~ 5	// 10	= ~0101	- 1010
  5 << 1	// 10	= 0101 - << 1	- 1010
  5 ^ 1	// 4 =	0101 ^ 0001	- 0100
  5 >> 1 //	2	= 0101 >> 1	- 0010
  5 >>> 1	// 2= 0101 >>> 1 - 0010
 ```
   - In binary number system decimal numbers have an equivalent represented by a
series of 0’s and 1’s. For example 5 is 0101 and 1 is 0001. Bitwise operators work
on those bits, rather than number’s decimal values.
  - We won’t go into great detail about how they work, but you can easily look them
up online. They have unique properties: for example: the << operator is the
same as multiplying a whole number by 2 and >> operator is the same as dividing
a whole number by 2. They are sometimes used as performance optimizations
because they are faster than * and / operators in terms of processor cycles.

**8.0.7 typeof**
  - The typeof operator is used to check the type of a value. It will often evaluate
to either primitive type, object or function. The value produced by the typeof
operator is always string format:
```javascript
typeof 10;//number
typeof 10n;//bigint
typeof 'text';//string
typeof NaN;//number
typeof true;//boolean
typeof [];//object
typeof {};//object
typeof Object; //function
typeof new Object();//object
typeof null;//object

```
  - NaN (Not a Number) evaluates to ’number’. This is just one of many
JavaScript quirks. However, they are not bugs and usually start to make more
sense as your knowledge of JavaScript deepens.
  - NaN lives natively on Number.NaN – it is considered to be a primitive value.
  - NaN is the symbol usually produced in the context of a numeric operation. One
such example is trying to instantiate a number object by passing a string value to
its constructor: new Number(”str”) in which case NaN would be returned.
**8.0.8 Ternary (?:)**
 - The ternary operator has the form of: statement?statement:statement;
Statements can be expressions or a single value:
```javascript
var satement = 45;
let result = 45;
result = satement ? "pass" : "fail";
console.log(result);
```
  - The ternary operator is like an inline if-statement. It does not support {} brackets
or multiple statements.
**8.0.9 delete**
  - The delete keyword can be used to delete an object property:
 ```javascript
let bird = {name:"raven",speed:"30mpg"};
console.log(bird);//{name:"raven",speed:"30mpg"};
delete bird.speed;
console.log(bird);//{name:"raven",speed:"30mpg"};
 ```
   - You cannot use delete to remove stand-alone variables. Even though, if you try
to do that, no error will be generated (unless you are in strict mode.)
**8.0.10 in**
 - The in operator can be used to check if a property name exists in an object:
```javascript
 "c" in {"a": 1, "b":2,"c":3};//true
1 in {"a": 1, "b":2,"c":3};//false
```
  - The in operator, when used together with arrays, will check if an index exists.
Note, it is ignorant of actual value (in either arrays or objects.)
```javascript
0 in["a","b","c"];//true
1 in["a","b","c"];//true
2 in["a","b","c"];//true
3 in["a","b","c"];//false
```
  - You can check for properties on built-in data types. The length property is native
to all arrays:
```javascript
"length" in [];  //true
"length" in["a","b","c"];//true
```
  - The ”length” property does not exist natively on an object unless it’s added explicitly:
```javascript
"length" in {};//false
"length" in {"length":1}//true
```
Check for presence of constructor or prototype property on an object constructor
function:
```javascript
"constructor" in Object;//true
"prototype" in Object;//true
"length" in object; //truer
```


**Chapter 9**
**...rest and ...spread**
**9.0.1 Rest Properties**
 - The ...rest syntax can help you refer to a larger number of items by extracting
them from a single function parameter name. The single ...rest parameter is
assumed to contain one or more arguments passed to the function:
  - Using ...rest properties to break down a larger number of arguments
and passing them to higher-order function Array.map()
  - We can further shorten code by moving console output to a separate print function:
 ```javascript
 let print = item => console.log(item);
 let f = (...item) => item.map(print);

 ```
 Call the f() function with an arbitrary number of arguments:
```javascript
f(1, 2, 3, 4, 3);
```
 - The function takes rest parameters: you can specify as many as you need.
Console output:

```console
1
VM214:2 2
VM214:2 3
VM214:2 4
VM214:2 3
```
 - After arrow functions were introduced in EcmaScript 6, to further shorten code
some started to name their variables using a single character:
```javascript
let f = (i...)=>i.map(v=>console.log(v));
```
  - We just used multiple language features: an arrow function, ...rest, and .map()
to abstract our code to something that looks like a math equation without sacrificing original functionality. It definitely looks cleaner than a for-loop!
  - This might make your code even shorter, but it’s probably harder to understand.
Remember, if you are working on a team, another person might be reading your
code. Sometimes that person will be you in the future.

**9.0.2 Spread Properties**
  - You can think of spread as an opposite of rest.
  - It can help you extract parts from an object.
  
  **9.0.3 ...rest and ...spread**
 - It’s tempting to call ...rest or ...spread syntax operators. And you will often hear
people refer to them as such. But in fact it is only syntax. An operator is often
thought of as something that modifies a value. Rest and spread assign values.
  - If we box them into the category of operators, perhaps we could say they would be
similar to the equality operator =. Rest and spread simply abstract it for working
with multiple assignments.
 - The rest syntax is called rest parameters, in the context of using it as a parameter
name in a function definition, where it simply means: ”the rest of arguments”.
Sometimes it is referred to as rest elements, because it assumes multiple values.
  - Both rest and spread syntax takes on the form of ...name. So what’s the
difference?
  - ...spread operator – expand iterables into one or more arguments.
  - ...rest parameter – collect all remaining parameters (”the rest of”) into an array.

**...rest**
  - Let’s say we have a simple sum() function:
  - This limits us to two arguments.
The ...rest parameters can gather an unknown number of arguments passed to
the function and store them in an array (named args in this example):
```javascript
function sum(...args){
 console.log(args);
 
 }
 sum(1,2,3,4);

```
  - It is similar to the built-in arguments array-like object. But there is a difference.
As the name suggests, rest can capture ”the rest of” parameters.
  - Keep in mind, ...rest must be either the only arguments token, or the last one on
the list. It cannot be the first argument of many:
`function sum(...args, b, c){}//error`
  - The ...rest parameters cannot appear as the leading parameter name when
followed by more parameters. You can think of it as ”the rest of” arguments when
used in this context.
`function sum(b, ...args, c){}//error`
 - Likeiwise ...rest cannot appear in the middle of an argument list. In
context of multiple function parameters, it is always the last one on the list.
 - If you don’t follow this rule, the following error will be generated in console:
 `function sum(a, b, c...args){}//correct`
```javascript
//Quirk: if you pass an array, it will register as an array:
sum([1,2,3]);//array(3)
//But you can flatter an array using spread syntax
sum(...[1,2,3]); //

```
  - In this case the three dots in ...[1,2,3] is actually ...spread. You can see from
this example that ...spread is like a reverse of ...rest: it unpacks values from an
array (or an object, as we will see later.)
  - Contrary to ...rest, ...spread is allowed to be used anywhere on a list.
  - But ...rest and ...spread can sometimes overlap:
  ```javascript
  function print(a, ...args){
    console.log(a);
    console.log(args);
  }
  print(...[1,2,3],4,5); //here it is ...spread
  //a=1
  // args =[2,3,4,5]
  ```
  - Here, first ...spread forms a complete list of arguments: 1, 2, 3, 4, 5 and
that’s what’s passed into the print function.
  - Inside the function, a equals 1, and [2, 3, 4, 5] is ”the rest of” arguments.
Here’s another example:
```javascript
function print(a,b,c, ...args)
{
    console.log(a);
    console.log(b);
    console.log(c);
    console.log(args);
}
print(...[1,2,3],4,5);
```
**Creating a sum() function with ...rest arguments**
  - Our first sum function using ...rest parameters might look like this
```javascript
  function sum(...args){
    let sum = 0;
    for (let temp of args)
    sum +=temp;
    return sum;
}
let add = sum(1,2,3,4,5);
console.log(add);
  
```
  - But because ...args produces an array, which makes it an iterable, we can use a
reducer to perform the sum operation:
```javascript
  function sum(...args){
    return args.reduce((k, j)=>k+j,0)
}
let add=sum(1,2,3,4,5,20);
console.log(add);

```
  - But ...rest parameters also work in arrow functions and we can further shorten
the function to following form:
```javascript
let sum = (...args)=>args.reduce((k,j)=>k+j,0);
sum(1,2,3,4,5,20);
console.log(sum);
```
  - Some people think while this format is shorter, it’s harder to read. But that’s the
trade off you get with functional programming style. People with background in
math find this format elegant. Traditional programmers might not.
**Flattening arrays with ...spread**
  - Luna would be a nice name for a female cat with silvery fur that resembles the
```javascript
moon’s surface.
let subscribed =["netflix","amazon"];
const ott = [...subscribed,"disney","zeetv"];
console.dir(ott);
```
**Using ...spread outside of arrays,objects or function parameters**
You can’t use ...spread syntax to assign values to variables.
```javascript
let a = ...[1,2,3]; //error Uncaught SyntaxError: Unexpected token '...'
```
  - Are you disappointed? Don’t be. You will love Destructuring Assignment.

**9.1 Destructuring Assignment**
  - Destructuring assignment can be used to extract multiple items from arrays and
objects and assign them to variables:
```javascript
[a,b] = [10,20];
console.log(a,b);//10 20
```
  - The above code is the same as:
```javascript
 var a = 10;
 var b = 20;
```

  - When var, let or const are not specified, var is assumed:
 ```javascript
 [a] = [1];
  console.log(window.a);// 1
 ```
   - As expected let definitions are not available as a property on window object:
 ```javascript
 let  [a] = [1];
  console.log(window.a);// undefined
 ```
  - It is possible to destructure into ...rest array:
  ```javascript
  [a,b,...rest] = [30,40,50,60,70];
console.log(a,b);
console.log(...rest);

  ```

    - Destructuring is often used to extract object properties to a matching name:
 ```javascript
let {oranges} = {orangeS :1 };
console.log(oranges);
 ```
   - The order doesn’t matter – as long as there is property grapes the value will be
assigned to the variable with the same name on the receiving end:
```javascript
let fruitBasket={apples:1,oranges:2,mangoes:3};
let {apples, mangoes} = fruitBasket;
console.log(apples+mangoes);
```
  - Extract from multiple values. Grab apples and oranges and count them:
  - Destructuring is not implicitly   recursive, second-level objects are not scanned:
    
```javascript
let {oranges} = {apple:1,inner:{orange:2}};
console.log(oranges);//undefined

```
  - But it’s possible to extract directly from object’s inner properties:
```javascript
  let deep = {
    basket:{
        fruit:{
            name: "orange",
            shape: "round",
            weight: 0.2
        }
    }
}
let {name, shape, weight} = deep.basket.fruit;
console.log(name);
console.log(shape);
console.log(weight);
```
  - If variable is not found in object, you will end up with undefined. For example, if
we attempt to destructure to property name that doesn’t exist in the object:
```javascript
let {apples}={oranges:1};
console.log(apples);//undefined
```
  - It is possible to destructure and rename at the same time:
```javascript
 let {automobile:car}={automobile:"Tesle"};
  console.log(car);//Tesla
```

**Merging objects with ...spread**
  - You can use ...spread syntax to easily merge two or more objects:
 ```javascript
 let a = {p:1,q:2,m:()=>{}};
 let b = {r:4,s:5,n:()=>{}};
 let c = {...a,...b};
 ```
   - What are the contents of object c?
  ```javascript
  console.log(c);
  ```
  Console output;
 ```console
 {p: 1, q: 2, r: 4, s: 5, m: ƒ, …}
m: ()=>{}
n: ()=>{}
p: 1
q: 2
r: 4
s: 5
[[Prototype]]: Object
 ```
   - The great thing is that it’s not just a shallow copy.
...spread copies nested properties too:
```javascript
let a = {nest:{nest:{eggs:10}}};
let b = {eggs:5};
let c = {...a,...b};
console.log(c);
```
Console output:
```console
{nest: {…}, eggs: 5}
eggs: 5
nest:
nest: {eggs: 10}
[[Prototype]]: Object
[[Prototype]]: Object
```
**Merging arrays with ...spread**
  - The same can be done with arrays:
 ```javascript
 let a = [1,2];
 let b = [3,4];
 let c = [...a,...b];
 console.log(c);
 ```
# **Chapter 10**
## **Closure**
  - Closure Introduction
There are many different ways to explain a closure. The explanations in this
chapter should not be taken for the holy grail of closures. But it is my hope that
interpretation presented in this book will be enough to deepen your understanding.
  - Feel free to play around with the examples shown here on codepen.io and see
how they work. Eventually it should sink in.
In C, and many other languages, when a function call exits, memory allocated for
that function is wiped out as part of automatic memory management on the stack.
  - But in JavaScript, variables and functions defined inside that function still remain
in memory, even after the function is called.
  - Retaining a link to variables or methods defined inside the function, after it has
already been executed, is part of how a closure works.
  - JavaScript is an ever-evolving language.
  - When closures came around, there were no classes or private variables in JavaScript.
  - It can be said that until EcmaScript 6, closures could be used to (roughly) simulate
something similar to what is known as object’s method privacy.
  - Closures are part of traditional programming style in JavaScript. They are a prime
candidate for interview questions.    Having said this, JavaScript Grammar cannot
be complete without a discussion on closures.
**What Is Closure?**
  - A closure enables you to keep a reference to all local function variables, in the
state they were found after the function exited.
  - Closures are difficult to understand, knowing nothing about scope rules and how
execution context delegates control flow in JavaScript. But I think this task can
be simplified if we start simple and take a look at a few practical examples.
  - To understand closures, we need to – at the very least – understand the following
construct. Primarily it is enabled by the idea that in JavaScript you can define a
function inside another function. Technically, that’s what a closure is.

```javascript
function global(){
    function inner(){
        console.log("inner");
    }
    inner();//Call inner
}
global();//"inner'

```
  - In the following example, global function sendMail defines an anonymous function
and assigns it to variable send. This variable is visible only from the scope of
sendEmail function, but not from global scope:
```javascript
function sendEmail(from,sub,message){
    let msg = `"${sub}">"${message}" received from "${from}"`;
    let send =function () {console.log(msg)}
    send();
}
sendEmail('Pravin','re:subject','Good news');

```
  - In JavaScript, inner functions have access to variables defined in the
scope of the function in which they are defined.
  - When we call sendEmail it will create and call send function. It is not possible
to call send() directly from global scope.
  - Console Output:
```console
  "re:subject">"Good news" received from "Pravin"
```
 - We can expose a reference to private methods (inner functions) by returning them
from the function. The following example is exactly the same as one above, except
here instead of calling the send method we return a refernce to it on line 004:
```javascript
function sendEmail(from,sub,message){
    let msg = `"${sub}">"${message}" received from "${from}"`;
    let send =function () {console.log(msg)}
    return send;
}
let ref = sendEmail('Pravin','re:subject','Good news');
ref();
```
  - Instead of calling send(), let’s return it. This way a reference to this
private method can be created in global scope.
  - Now we can call send() by reference directly from global scope.
  - Even after sendEmail function was called, msg and send variables remained in
memory. In languages like C, they would be removed from the automatic memory
  - on the stack, and we wouldn’t be able to access them. But not in JavaScript.
  - Let’s take a look at another example. First we defined print, set, increase and
decrease variables as global placeholders. 
```javascript
let print,set, increase, decrease;
function manager(){
    console.log("manager();");
    let number = 15;
    print = function(){console.log(number)}
    set = function(value) {number = value}
    increase = function() {number++}
    decrease = function() {number--}
}

```

  - In order to assign anonymous function names to global function variables, we need
to run manager() at least once.

```javascript
manager();//undefined
print();//15
for(let i = 0; i<200 ; i++) increase();
print();// 215
decrease();
print();//214
set(755);//755
let old_print = print;
manager();
print();//15
old_print();//755
```
   - The set(755) function resets the value of number to 755.
**Explanation**
  - After calling manager() for the first time. The function executed and all global
references were linked to their respective anonymous functions. This created our
first closure. Now, let’s try to use the global methods to see what happens.
  - We then calleBeautiful Closure
It can be assumed that closures are used in Functional Programming for similar
reasons to why private methods are used in Object Oriented Programming. They
provide a method API to an object in the form of a function.
What if we could advance this idea and create a closure that looked beautiful and
returned several methods rather than just one?d some methods: increase(), decrease() and set() to modify
the value of number variable defined inside manager function. At each step we
printed out the value using the print() method, to confirm it actually changed.
**Beautiful Closure**
  - It can be assumed that closures are used in Functional Programming for similar
reasons to why private methods are used in Object Oriented Programming. They
provide a method API to an object in the form of a function.
  - What if we could advance this idea and create a closure that looked beautiful and
returned several methods rather than just one?
let get = null; //placeholder for global getter function
```javascript
function closure(){
    this.inc = 0
    get = () => this.inc;//getter
    function increase() {this.inc++;}
    function decrease() {this.inc--;}
    function set(v) {this.inc = v;}
    function reset() {this.inc=0;}
    function del(){
        delete this.inc;//become undefined
        this.inc = null;
        console.log("this.inc deleted");

    }
    function readd(){
        if(!this.inc)
         this.inc = "re-added";
    }
    return [increase,decrease,set(15),reset,del,readd];
}


```
  - The del method will completely remove inc property from the object and readd will
re-add the property back. For simplicity of the explanation there is no safeguarding
against errors. But naturally, if the inc property was deleted, and an attempt to
call any of the methods was detected, a reference error would be generated.
  - Initialize closure:
 ```javascript
 let f = closure();
console.log(f)
 ```
   - Variable f now points to an array of exposed methods. We can bring them into
global scope by assigning them to unique function names:
```javascript
let inc = f[0];
let dec = f[1];
let set = f[2];
let res = f[3];
let del = f[4];
let add = f[5];
```
  - We can now call them to modify the hidden inc property:

```javascript
inc();//1
inc();//2
inc();//3
dec();//2
get();//2
set(7);//7
get();//7
res(0);//0
get();//0
```
- Finally we can delete the property itself using del method:
```javascript
//Delete property
del(0);//null
get();
```
  - Calling other functions at this point would produce a reference error, so let’s re-add
the inc property back to the object:
```javascript
//read property inc
add();
get();//"re-added"
```
 - Reset the inc property to 0 and increment it by 1:
```javascript
res();
 inc();
 get();
```
**Closing Words**
  - Whenever a function is declared inside another function, a closure is created.
  - When a function containing another function is called, a new execution context
is created, holding a fresh copy of all local variables. You can create a reference
to them in global scope, by linking to variable names defined in global scope, or
returning the closure from the outer function using return keyword.
  - A closure enables you to keep a reference to all local function variables, in the
state they were found after the function exited.
 - **Note:** new Function() constructor does not create a closure, because objects
created with new keyword also creates a stand-alone context.

**10.0.1 Arity**
  - Arity is the number of arguments a function takes.
  - You can access function’s arity via Function.length property:
```javascript
function f(a,b,c){}
let arity = f.length;
console.log(arity);
```
**10.0.2 Currying**
  - In JavaScript functions are expressions. This also means a function can return
another function. In the previous section we looked at the closure pattern. Currying
is a pattern that immediately evaluates and returns another function expression.
  - A curried function can be constructed by chaining closures by defining and immediately returning all inner functions at the same time.
  - Here is an example of a curried function:
  ```javascript
  let planets = function(a){
    return function(b){
    return 'favorite planets are ' + a + ' and ' +b;
    }

    };
    let favoritePlanet = planets('jupiter');
    let fav1 = favoritePlanet('Earth');
    console.log(fav1);
    let fav2 = favoritePlanet('Mars');
    console.log(fav2);
    let fav3 = favoritePlanet('Saturn');
    console.log(fav3);

  ```

  - Function planets returns another anonymous function. So when it is assigned
to favoritePlanets with one argument ”Jupiter”, it can be called again with a
secondary argument.
  - Here is the result of the 3 curried functions from example above:
```console
favorite planets are jupiter and Earth
favorite planets are jupiter and Mars
favorite planets are jupiter and Saturn
```
  - The inner function can be invoked immediately after the first call:
  ```javascript
    let p = planets('Earth')('Mars');
    console.log(p);
  ```
  And the result is:
  ```console
  favorite plnaets are Earth and Mars
  ```
    - Currying is originally considered to be part of functional programming style.
  - It is not a surprise then, that this older currying syntax can be rewritten into this
far more elegant arrow function format:
```javascript
let planets = (a) => (b) => 'favorite planets are ' + a + ' and ' +b;
let fav1=planets ("venus")("Mercury");
console.log(fav1);
```
And the outcome is:
```console
favorite planets are venus and Mercury
```

# **Chapter 11**
## **Loops**
 - Loops are fundamental to working with lists. The primary purpose of a loop is
to iterate over one or a set of multiple statements. Iterating is commonplace in
software development – it means to repeat an action a multiple number of times.
  - Working with loops introduces the idea of iterators. Some built-in types are
iterable. Iterables that can be passed to a for...of loops instead of using traditional
for-loop. You can say that an iterable object abstracts away the index values of
a list and helps you focus on solving the problem.
  - Array is an iterable. Object is not (objects are enumerable).
  - An iterable type guarantees the order of items in the set. This is why arrays have
an index for each item. Enumerable types do not guarantee the order in which
properties will appear when iterated.
**11.0.1 Types of loops in JavaScript**
  - There are different ways to iterate in JavaScript. Starting from classic while and
for- loops to leaning more toward functional programming style iterators: using
array’s higher-order methods. 
  - Common iterators are for, for...of, for...in, while
and Array.forEach. 
  - Some Array methods are assumed to be iterators: .values,
.keys, .map, .every, .some, .filter, .reduce and a few others. They are called
higher-order functions, because they take another function as an argument.
**Incrementing And Reducing**
  - Loops are often used for walking through a large list of objects and updating their
properties. Loops can be used for filtering out objects and reducing the list to
something more meaningful.
  - They can also be used for reducing a set of values to a single value:
```javascript
  let miles = [50,6,9,20,15,30];
// Add up all numbers using a for loop
let a = 0;
for(let i=0; i<5;i++)
   a += miles[i];
console.log(a);//99
```
  - You can implement a reducer to the same effect:
 ```javascript
 let miles = [50,6,9,20,15,30];
const R =(accumulator,value) => accumulator + value;
const result = miles.reduce(R);
console.log(result);
 ```
 **Generating HTML Elements Dynamically**
  - Create a number of HTML elements dynamically to populate the UI view:
```javascript
 for(let i=0;i<10;i++){
    i = 1;
    let element = document.createElement('div');
    element.innerHTML = 'element' + i;
    document.appendChild(element);
}
```
  - This code will add 10 div elements to the document.
  - It is possible to use appendChild method to create nested elements.


**Render lists**
  - Loops are often used together with render lists. Rendering is simply the act of
displaying something on the screen. In software development, there are plenty of
times when you need to display a list of items.

**Dynamically sorted tables**
  - Building an entire table dynamically can help you sort values by column using an
Array.entries and Array.sort methods.
  - In some cases you will have to write your own sorting function, if your table columns
are stored in an object as properties and not array items. That however, may or
may not be a good idea, depending on the data set.
**Note**
  - You cannot easily make a decision about exactly how to deal with lists, until some
sort of data layout is defined. So, choosing which type of loop to use will be often
determined by other decisions made and the layout of your custom data structures.
**11.1 for loops**
  - For loop syntax comes in three syntactic flavors:
```javascript
//For-loop with an empyt body
for(initializer; condition; increment);
//Iterate over a single statement
for(initializer; condition; increment) single_statement;
//Iterate over multiple statements
for(initializer; condition; increment){
  multiple;
  statements;
}
```
  - For loops require 3 statements separated by two semicolons, which can be any
legal JavaScript statement, a function call, or even an empty statement.
  - You’ll often use the following pattern in basic implementations: 1) initialize
counter 2) test condition and 3) increment or decrement counter.
**11.1.1 0-index based counter**
  - Initializing the for-loop counter with a 0-index based value is a good idea, because
most lists (like arrays) are 0-index based, where first item is located at array[0]
and not array[1]. This might take some time to get used to
**11.1.2 The Infinite for Loop**
  - A for loop can be defined without any of the default statements. But by doing
this you will create an infinite for-loop that will freeze your program:
```javascript
for(;;)
 console.log("hi");//Infinite foe loop *strictly don't do it.*
```
  - You probably don’t really want to do this, unless for some reason it becomes
necessary. A while loop should probably be used in this case.
**811.1.3 Multiple Statements**
  - Multiple statements can be separated by comma. In the following example the
inc() function is used to increment value of global variable counter. Note the
combination of the two statements: i++, inc():
```javascript
let counter = 0;
function inc(){counter++;console.log(counter)}
for(let i =0;i<10;i++,inc());
;
```
  - This body-less for loop progresses the counter 10 times. The actual value is
incremented inside the inc() function. This is just an example of executing multiple
statements, we should definitely avoid using global variables in these types of cases.

**Incrementing Numbers**
  - At their basic, loops can be used to increment numbers.
```javascript
  let counter = 0;
   for(let i = 0; i < 10 ; i++)
        counter++;
        console.log(counter);
```

**for loops and let scope.**
  - Bracket-less for-loop syntax is not good friends with the let keyword. The following
code will generate an error:
```javascript
for(var i=0;i<10;i++) let x = i;
```
  - A let variable cannot be defined without scope brackets. All variables defined using
let keyword require their own local scope. This is fixed by:
```javascript
for(var i=0;i<10;i++) { let x = i; }
```
**Nested for Loops**
  - Because a for loop is a JavaScript statement in itself it can be used as the iterable
statement of another for loop. This hierarchical for loop is often used for working
with 2-dimensional grids:
```javascript
for(let y=0;y<2;y++)
    for (let x=0;x<2;x++)
              console.log(x, y);
```
  - Console output (all combinations between x / y):
  
```console
  0 0
1 0
0 1
1 1

```


**Loop’s Length**

  - The condition statement will usually check if counter has reached a limit and if
so, the loop will terminate:

  - You can add brackets if you need to execute multiple statements:
```javascript
for(let i=0;i<3;i++){
    let loop = "loop";
    console.log(loop);
}
```
Console output:
```console
loop
loop
loop
```
**Skipping Steps**
  - You can skip an iteration step by using continue keyword
 ```javascript
 for(let i=0;i<3;i++){
    if(i==1)
    continue;
    console.log(i);
  }
 ```
 Console output:
```console
0
2
```
  - The continue keyword tells code flow to go to the next step without executing any
next statements in this for-loop’s scope during the current iteration step.
 **Breaking Early**
  - You can break out of a for loop by using break keyword
```javascript
 for(let i = 0;i<2;i++){
    console.log("loop");
    break;
}
```
  - Note the condition statement was skipped here. The loop will break by an explicit
command from the statement itself.
In this case the for loop will print ”loop.” to the console only once. The break
  - keyword simply exits the loop whenever it’s encountered. But it can also be
conditional (see next example.)
**Custom Breaking Condition**
  - None of the 3 statements separated by ;; in a for loop are required. It’s perfectly
legal to move the conditional test into the for loop’s body, instead of testing for
it between the parenthesis.
  - This example skips the middle statement, where we would usually create a conditional test for the counter, and replaces it by its own condition inside the loop
where it breaks out of the loop if i is greater than 1:
```javascript
for(let i = 0;;i++){
    console.log("loop, i = "+i);
    if(i>1)
    break;
}
```
  - If not for the if statement inside the for loop, it would continue indefinitely because
there are not other conditions stopping it from running.
Console output:
```console
loop, i = 0
loop, i = 1
loop, i = 2 
```
  - The word ”loop.” is printed 3 times. The condition i is greater than 1 might
deceive us into thinking that the text will be printed 2 times at most. But it’s printed 3 times! That’s because counting started with 0 and not 1, and at its
upper limit the condition evaluates to 2 and not 1.
**Breaking To Label**
  - In JavaScript, a statement can be labeled when a label name: is prepended to a
statement. Because a for loop is a statement you can label for loops.
  - Let’s try to increment value of c inside the inner loop. By choosing whether to
break the loop and jump to inner or mark label we change the pattern in which
the for loops will work:
1. This example produces 11 when breaking to mark: label.
```javascript
let c = 0;
mark: for(let i=0; i<5;i++)
    inner: for(let j=0; j<5;j++){
        c++;
        if(i==2)
        break mark;
    }
    console.log(c);//11
```
2. This example produces 21 when breaking to inner: label.
```javascript
let c = 0;
mark: for(let i=0; i<5;i++)
    inner: for(let j=0; j<5;j++){
        c++;
        if(i==2)
        break inner;
    }
    console.log(c);//21

```
  - The two examples are logically different based on which label the execution flow
of the inner for loop is transferred to.
**Breaking from a labeled block scope**
  - While we’re on the subject, you can use break keyword to break out of regular non
for-loop block scope as long as it’s labeled:
```javascript
block:{
    console.log("before");
    break block;
    console.log("after");
}

```
Console output:
```console
"before"

```
  - Execution flow never reaches ”after”.
  
  **11.2 for...of Loop**
  - Using indexed iterators, such as the for loop, can become a hassle when dealing
with arrays or object properties. Especially when their number is not known.
  - for...of loops to the rescue!
  - We’ll start with a slightly advanced example where we will use a for...of loop
together with a generator, and then discover some of the other, simpler use-cases.

**11.2.1 for...of and Generators**
  - Sometimes you might want to use a for loop with a generator – a special type of
function with star * character appended to the function* keyword.
  - When a generator function is called, the multiple yield statements inside it do not
execute at the same time, as you would normally expect. Only the first one does.
  - To execute yield statements 2 and 3, you have to call the generator function
again (two more times). Internally, the yield statement counter is incremented
automatically every time you call the generator function.
  - Generator executes a yield statement asynchronously, even though the code inside
the generator function has linear appearance. This is done on purpose - it makes
code more readable compared to alternatives (XMLHttpRequest, Ajax, etc).
```javascript
function* generator(){
    yield 1;
    yield 2;
    yield 3;
}
for(let value of generator())
  console.log(value)

```
  - The code above is equivalent to calling generator manually 3 times (When you
want to increment generator manually just make sure that you first assign it to
another variable.):

```javascript
let gen = generator();

console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);

```
  - Here’s the console output in either case:
```console
1
2
3
```
  - Generators are one-time use functions. You should not attempt to reuse a generator function more than once as if it were a regular function (after the last yield
statement has been executed.)11.2.2 **for...of and Strings**
  - Strings are iterable.
You can walk each character of a string using a for...of loop:

```javascript
let string="text";
for(let value of string)
   console.log(value); 
```
Console:
```console
t
e
x
t
```
**11.2.3 for...of and Arrays**
  - Let’s say we have an array:
 ```javascript
 let array = [0,1,2];
 ```
   - We can iterate through it without having to create index variables. Once the end
of the array is reached the loop will end automatically:
```javascript
const array = [1,2,3,4];
for(let value of array)
  console.log(value)
```
Console:
```console
1
2
3
4
```
**11.2.4 for...of and Objects**
  - It would be nice to have the ability to iterate over an object’s properties using
for...of loop, right?
```javascript
let object = {a:1,b:2,c:3};
for(let value of object)
  console.log(value)//Object is not iteratable
  
```
  - But for...of loops work only with iterable values. An object is not an iterable. (It
has enumerable properties.) One solution is to convert the object to an iterable
first before using it in a for...of loop.
**11.2.5 for...of loops and objects converted to iterables**
  - As a remedy you can first convert an object to an iterable using some of the built-in
Object methods: .keys, .values or .entries:
```javascript
let enumerable={property:1,method:()=>{}};
for (let key of Object.keys(enumerable))
  console.log(key);//property method

for (let value of Object.values(enumerable))
  console.log(value);//1 [Function: method]

for (let entry of Object.entries(enumerable))
  console.log(entry);//[ 'property', 1 ] [ 'method', [Function: method] ]
```
  - This can also be achievable by using a for...in loop instead, without having to use
any of the Object conversion methods.
We’ll take a look at that in the following section.
**11.3 for...in Loops**
  - The for...of loops (in previous section) only accept iterables. Unless the object is
first converted to an iterable, a for...of loop won’t be of any help.
  - for...in loops work with enumerable object properties. It’s a much more elegant
solution for iterating through Object properties.
  - When you have an object at hand you should probably use a for...in loop.
 ```javascript
 let object = {a:1,b:2,c:5,method:()=>{}};
for (let value in object)
   console.log(value, object[value]);
   
/*Console
a 1
b 2
c 5
method [Function: method]*/
 ```
   - A for...in loop will iterate only enumerable object properties. Not all object
properties are enumerable, even if they exist on the object. All non-enumerable
properties will be skipped by for...in iterator.
  - You won’t see constructor and prototype properties in an output from the
for...in loop. Although they exist on an object they are not considered to be
enumerable.

**11.4 While Loops**
  - A while loop will iterate for an indefinite number of times until the specified
condition (there is only one) evaluates to false. At which point your loop will stop
and execution flow will resume.
```javascript
while (condition){
  /*do something until condition is false*/
}
```
  - Once condition evaluates to false the while loop will break automatically:
```javascript
 let c = 0;
while (c++ <= 5)
console.log(c);

```
Console:
```console
1
2
3
4
5
6
```
  - A secondary condition can be tested within the loop. This makes it possible to
break from the loop earlier if needed:
```javascript
while(condition_1){
  if(condition_2)
     break;
}
```
**11.4.1 While and continue**
  - The continue keyword can be used to skip steps:
  let c = 0;
```javascript
while (c++ < 1000){
 if (c > 1)
     continue;
     console.log(c)
}
```
  - Console output:
```console
1
```
  - Just keep in mind this is just an example. In reality, this would be considered bad
code, because the if statement is still executed 1000 times. The console prints 1
only when c == 0. If you need an early exist, use break instead.

# **Chapter 12**
## **Arrays**
  - Many of the Array.* methods are iterators. Instead of passing your array into a
for or a while loop you should use built-in Array methods instead. Arrays usually
already have methods offering cleaner syntax for anything you would write yourself
to solve the same problem. So why re-invent the wheel?
  - Array methods are attached to Array.prototype property. This means you can
execute them directly from array object like array.forEach() or directly from
array’s literal value like: [1,2,3].forEach();
**12.0.1 Array.prototype.sort()**
  - Previous (pre-ES10) implementation of V8 used an unstable quick sort algorithm
for arrays containing more than 10 items.
  - A stable sorting algorithm is when two objects with equal keys appear in the same
order in the sorted output as they appear in the unsorted input. But this is no
longer the case. ES10 offers a stable array sort:

```javascript
var fruit = [
    {name:"Apple", count:13,},
    {name:"Pear", count:12,},
    {name:"Banana", count:12,},
    {name:"Strawberry", count:11,},
    {name:"Cherry", count:11,},
    {name:"Blackberry", count:10,},
    {name:"Pineapple", count:10,}

];
```

Console Output:
```javascript
//create our own criteria function:
let mySort=(a,b)=>a.count - b.count;
//Perform stable ES10 sort:
let sorted = fruit.sort(mySort);
console.log(sorted);
```
Console Output:

```console
[
  { name: 'Blackberry', count: 10 },
  { name: 'Pineapple', count: 10 },
  { name: 'Strawberry', count: 11 },
  { name: 'Cherry', count: 11 },
  { name: 'Pear', count: 12 },
  { name: 'Banana', count: 12 },
  { name: 'Apple', count: 13 }
]
```
**12.0.2 Array.forEach**
  - The forEach method will execute a function for every item in the array.
  - Each iteration step receives 3 arguments value, index, object.
It’s similar to a for-loop but it looks cleaner:
```javascript
let fruit = ['pear',
'banana',
'orange',
'apple',
'cherry'];
let print = function(item,index,object){
    console.log(item);
}
fruit.forEach(print);
```
  - Starting from ES6 it can be suggested to use arrow functions together with Array
methods. The code will be easier to read and maintain when building large scale
applications. Let’s take a look at how we can make syntax cleaner:
  - Because in JavaScript functions are also expressions, you can pass the function
directly into the forEach method:
```javascript
let print = function(item,index,object){
    console.log(item,index,object);
}
fruit.forEach(print);

```
  - But you might want to use an arrow function here: () => {}
 ```javascript
 fruit.forEach((item,index,object)=>{
console.log(item,index,object);});

 ```
   - The console output from both of the cases above:
 ```console
  pear 0 [ 'pear', 'banana', 'orange', 'apple', 'cherry' ]
banana 1 [ 'pear', 'banana', 'orange', 'apple', 'cherry' ]
orange 2 [ 'pear', 'banana', 'orange', 'apple', 'cherry' ]
apple 3 [ 'pear', 'banana', 'orange', 'apple', 'cherry' ]
cherry 4 [ 'pear', 'banana', 'orange', 'apple', 'cherry' ]
 ```
   - If you can get away with one argument and return statement you can use this slim
form:
```javascript
fruit.forEach(item=>console.log(item));
```
  - As long as you have only one single statement you can remove brackets.
```console
  pear
banana
orange
apple
cherry
```
**12.0.3 Array.every**
  - Return value: boolean
  - Not to be confused with ”execute for every item” logic of forEach. In many cases
method every will actually not run on every item in the array when at least one
item doesn’t evaluate to true based on specified condition.
  - The method every will return true if the value of every single item in the array
satisfies the condition specified in its function argument:
  - The result is true because none of the numbers in the array are greater than or
equal to 10. Let’s take at the same function with a different value set. If 10 or a
greater number was present in the array the result would be false:
  - Here one of the numbers is 256. Which can be translated to ”not every value
in the array is ¡ 10”. Hence, false is returned. It’s important to note that once
  - Array.every method encounters 256 the condition function will not execute on the
remaining items. Just a single failed test will cause false.
  - Array.every does not modify the original array. The value inside the function is a
copy, not a reference to the value in the original array
```javascript
const isBelowThreshold = (currentValue) => currentValue < 40;

const array1 = [1, 30, 39, 29, 10, 13];

console.log(array1.every(isBelowThreshold));

// expected output: true
```
**12.0.4 Array.some**
  - Return value: boolean
Similar to Array.every except it stops looping whenever it encounters a value that
evaluates to true (and not false like in Array.every) Let’s compare:
```javascript
let number = [0,10,2,3,4,5,6,7];
let condition = value => value < 10;
let some = number.some(condition);
let every = number.every(condition);
console.log(some);
console.log(every);
```
  - Here some returns true because it checks first value: 0 for ¡ 10 and immediately
returns true without having to check the rest of the values.
  - The every method returns false on the same data set. That’s because when it
reaches the second item whose value is 10, the ¡ 10 test fails.
  - Note: Try not to think of some as an ”opposite” of every. In some cases they
return the same result on the same data set.

**12.0.5 Array.filter**
  - Return value: new array consisting only of items that passed a condition.

```javascript
 let number = [0,10,2,3,4,5,6,7]
let condition = value => value < 10;
let filtered = number.filter(condition);
console.log(filtered);
console.log(number);

```
  - The new filtered array contains all original items except 10. Because it did not pass the ¡ 10 test. In a real-world scenario the condition can be much more complex
and involve larger objects sets.
**12.0.6 Array.map**
  - Return value: a copy of the original array with modified values (if any.)

```javascript
let number = [24,24,2,4,56,85,63];
let condition = number.map(value => value + 1);
console.log(condition);
```
  - Array.map is like Array.forEach but it returns a copy of the modified array. Note
that original array is still unchanged.
**12.0.7 Array.reduce**
  - Return value: accumulator
  - Reducers are similar to other methods. Yet they are unique because they have an
accumulator value. The accumulator value must be initialized. There are different
types of reducers. In this first example we’ll take at a simple case.
  - As values are iterated this accumulator adds all numbers into a single value:
Like any other Array method that works with iterables, a reducer has access to
the value it is currently iterating (currentValue).
  - This reducer added up all the numbers into the single accumulator value and
returned it: 1 + 2 + 4 = 7.
  - How to understand reducers in more complex, practical situations?
When developing software in the real world you won’t be using reducers to count
numbers. This can be done with a simple for loop. You will encounter plenty of
situations where a set of data should be ”reduced” only to the set of important
values based on some criteria.
```javascript
const array1 = [1, 2, 3, 4];
const reducer = (previousValue, currentValue) => previousValue + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15

```
**Array.reduce or Array.filter?**
  - There is a reason why Array object has a number of different methods that at
first sight appear to do the same things.
  - When it comes to Array methods, always try to to choose a proper tool for the
task. Don’t use reduce just because you want to use reduce – figure out if a
particular method was purposed to produces a more efficient logic.
  - It is written, somewhere, that reduce is the father of filter and map. Anything
you can do with filter and map can be done with reduce.
  - However, reduce provides a more elegant solution to adding up numbers than a
for-loop or other Array methods.
**Reducers And Updating Object Properties In A Database**
  - After an API action – update or delete an item, for example – you may want
to update the application view. But why update all objects everywhere, when you
can ”reduce” which object properties should be affected, without having to copy
entire lists of object – even the ones that weren’t affected by the API call?

**12.0.8 Practical Reducer Ideas**
  - Narrowing down on object properties
Let’s say your car listing management application has a button that updates the
price of a particular vehicle. The user sets a new price and clicks on the button.
An action is dispatched to update the vehicle in the database.
  - Then the callback function returns containing the object with all properties for
that vehicle ID (price, make, model, year). But, we only need to update the price.
  - A reducer can make sure to narrow down on (or ”hand pick”) only the vehicle
price property, not the entire set of properties on the object. The object is then
sent back to the database and application view is updated.

**Counting weekends**
  - Imagine a task where you had to implement a function that, given month would
return number of weekends, working days and holidays there are in that month. A
month could be represented by the number of days in it.
  - It’s important to keep the input values the same type as the return value of a
reducer. This is one of the main characteristics of a reducer: to reduce a set (not
necessarily by filtering, although it is a possibility.)
  - Function Purity
Reducers are often used in code written following Functional Programming style
principles. One of which is function purity. The following Dos and Dont’s
describe some of properties of a pure function.

**12.0.9 Dos and Dont’s**
  - Even though these are not absolute requirements, these ideas might be helpful for
avoiding anti-pattern code. Only use reduce() when the result has the same type
as the items and the reducer is associative: 
```javascript
[1,2,3,4,5].reduce((a,b)=>a+b, 0);
```
  - Do use it for summing up some numbers.
  - Do use it for multiplying some numbers.
  - Do use it for updating state in React.
  - Do not use it for building new lists or objects from scratch.
  - Do not use it for just about anything else (use a loop).
  - Do not use it to mutate (change original values of) its arguments.
  - Do not use it perform side effects, like API calls and routing transitions.
 - Do not use it to call non-pure functions, e.g. Date.now() or Math.random().

**12.0.10 Array.flat()**

  - Flattening a multi-dimensional array:
```javascript
  let multi = [1,2,3,[4,5,6,[7,8,9,[10,11,12]]]];
multi.flat();//(7) [1, 2, 3, 4, 5, 6, Array(4)]
multi.flat().flat();//(10) [1, 2, 3, 4, 5, 6, 7, 8, 9, Array(3)]
multi.flat().flat().flat();//12) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multi.flat(Infinity);//(12) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

**12.0.11 Array.flatMap()**

```javascript
let array = [1,2,3,4,5];
array.map(x=>x*2);
```
  - Becomes;
```console
(5) [2, 4, 6, 8, 10]
0: 2
1: 4
2: 6
3: 8
4: 10
length: 5
```
Now flatten the map:
```javascript
let array = [1,2,3,4,5];
console.log(array.flatMap(x=>x*2));
//[ 2, 4, 6, 8, 10 ]
```
**12.0.12 String.prototype.matchAll()**
Matching multiple patterns in a string is a common problem when writing software.
Use cases include extracting name and email addresses at the same time from an
email header, scanning for presence of unique patterns, etc.
In the past, to match multiple items we used String.match with a regular expression and /g (”global”) flag or RegExp.exec and/or RegExp.test with /g.
First, let’s take a look at how the older spec worked.
String.match with string argument only returns the first match:
```javascript
let string = "hello";
let matches = string.match("l");
console.log(matches[0]);
```
  - The result is a single "l" (note: the match is stored in matches[0], not matches.)
  - Only "l" is returned from a search for "l" in the word "hello".
  - The same goes for using string.match with a regex argument. Let’s locate the "l"
character in the string "hello" using the regular expression /l/:
```javascript
let string = "hello";
let matches = string.match("l");
console.log(matches[0]);
```
**Adding /g to the mix**
  - String.match with a regex and the /g flag does return multiple matches:

```javascript
let string = "hello";
let ret = string.match(/l/g);
console.log(ret);
// ['l', 'l']
//0: "l"
//1: "l"
//length: 2

```
  - Great... we’ve got our multiple matches using < ES10. It worked all along. So
why bother with a completely new matchAll method? Well, before we can answer
this question in more detail, let’s take a look at capture groups. If nothing else,
you might learn something new about regular expressions.

**Regular Expression Capture Groups**
  - Capturing groups in regex is simply extracting a pattern from () parenthesis.
  - You can capture groups with /regex/.exec(string) and with string.match.
Regular capture group is created by wrapping a pattern in (pattern).
  - But to create groups property on resulting object it is: (?<name>pattern).
  - To create a group name: prepend ?<name> inside brackets. The resulting object
will have a new property groups.name attached (see code below.)
This is the string we will take as the specimen for our experiment:
```javascript
const string = 'black*raven lime*parrot white*seagull';
const regex = /(?<color>.*?)\*(?<bird>[a-z0-9]+)/g;
while (match = regex.exec(string))
{
    let value = match[0];
    let index = match.index;
    let input = match.input;
    console.log(`${value} at ${index} with '${input}`);
    console.log(match.groups.color);
    console.log(match.groups.bird);

}
```
  - Note: match.groups.color & match.groups.bird are created
from adding ?<color> and ?<bird> to the () match in the regex string.

  - regex.exec method needs to be called multiple times to walk the entire set of
the search results. During each iteration when .exec is called, the next result is
revealed (exec doesn’t return all matches right away.) Hence, while loop

Console Output:
```console
lack*raven at 0 with 'black*raven lime*parrot white*seagull
black
raven
 lime*parrot at 11 with 'black*raven lime*parrot white*seagull
 lime
parrot
 white*seagull at 23 with 'black*raven lime*parrot white*seagull
 white
seagull
```
**But there is the quirk:**
 - If you remove /g from this regex, you will create an infinite loop cycling on the
first result forever. This has been a huge pain in the past. Imagine receiving a
regex from some database where you are unsure of whether it has /g at the end
or not. You’d have to check for it first, which would require additional code.
  - And now, we have enough background to answer the question:

**Good reasons to use .matchAll()**
1. It can be more elegant when using with capture groups. A capture group is
simply the part of regular expression with ( ) that extracts a pattern.
2. It returns an iterator instead of array. Iterators on their own are useful.
3. An iterator can be converted to an array using spread operator (...)
4. It avoids regular expressions with /g flag... useful when an unknown regular
expression is retrieved from database or outside source and used together with the
archaic RegEx object.
5. Regular expressions created using RegEx object cannot be chained using the
dot (.) operator.
6. Advanced: RegEx object changes internal .lastIndex property that tracks last matching position. This can wreck havoc in complex cases.
**How does .matchAll() work?**
  - Let’s try to match all instances of letter e and l in the word hello. Because an
iterator is returned we can walk it with a for...of loop:
```javascript
let iterator = "hello".matchAll(/[el]/);
for (const match of iterator)
  console.log(match);
```
  - Note that .matchAll method does not require /g flag.
 ```console
 [ 'e', index: 1, input: 'hello', groups: undefined ]
[ 'l', index: 2, input: 'hello', groups: undefined ]
[ 'l', index: 3, input: 'hello', groups: undefined ]
 ```
 **Capture Groups example with .matchAll()**
  - .matchAll returns an iterator so we can walk it with for...of loop.
  
```javascript 
const string = 'black*raven lime*parrot white*seagull';
const regex = /(?<color>.*?)\*(?<bird>[a-z0-9]+)/g;
while (match = regex.exec(string))
{
    let value = match[0];
    let index = match.index;
    let input = match.input;
    console.log(`${value} at ${index} with '${input}`);
    console.log(match.groups.color);
    console.log(match.groups.bird);

}
```
  - Console Output:

```console
lack*raven at 0 with 'black*raven lime*parrot white*seagull
black
raven
 lime*parrot at 11 with 'black*raven lime*parrot white*seagull
 lime
parrot
 white*seagull at 23 with 'black*raven lime*parrot white*seagull
 white
```

  - Perhaps aesthetically it is very similar to the original regex.exec while loop implementation. But as stated earlier this is the better way for the reasons mentioned
above. And removing /g won’t cause an infinite loop.

**12.0.13 Dos and Dont’s**
  - Do use string.matchAll instead of regex.exec & string.match with /g flag.

**12.0.14 Comparing Two Objects**
  - It makes sense to compare two literal numeric values such as 1 === 1 or literal
boolean values true === false, but what does it mean to compare two objects?
Furthermore == and === operators won’t help because they compare by reference
and not by value: [] and [] may be equal by value but they are different arrays:
```javascript
[] === [];//false by value
let x = [];
x===x;//true only by referance
```
  - We’ll have to write our own function! One way of thinking about comparing
objects is comparing the number, type and value of all of their properties.
  - Following naming convention of strcmp: a function that compares strings in many
languages, we can write a custom function objcmp that compares two objects:
```javascript
export default function objcmp(a,b){
    //Copy properties into a and b
    let A = Object.getOwnPropertyNames(a);
    let B = Object.getOwnPropertyNames(b);
     
    //Return early if number of properties is not equal
    if(A.length != B.length)
    return false;

    //Return early if number of properties on both objects
    for(let i = 0; i<A.length;i++)
    {
        let propName = A[i];
        //properties must equal by value *and type
        if(a[propName] !== b[propName])
        return false;
    }
    //objects are equal
    return true

}
objcmp();

```
  - The function objcmp takes two arguments: a and b, representing the two objects
we want to compare.
  - This is a non-recursive, shallow copy algorithm. In other words, we are only comparing first-class properties attached directly to the object. Properties attached to
properties are not compared. In many cases this is enough.
  - But there is another, much greater problem. In its current form the function
assumes that properties cannot point to either an array or object. Two common
data structures that are very likely to be part of an arbitrary object.
  - Even if we’re not doing a deep comparison, the function will fail if any of the
properties point to either an object or an array, regardless of whether their length
and actual values are the same:

```javascript
let a = {prop:[1,2], obj:{}};
let b = {prop:[1,2], obj:{}};
objcmp(a,b);
```
  - Our algorithm failed on [1,2] === [1,2] comparison. So how do we deal with
this situation? First, we can write our own is array function. Because array is
the only object in JavaScript with length property and at least 3 higher-order
functions: filter, reduce and map, we can say that if these methods exist on an
object, then it must be an array, with roughly 99% certainty:
```javascript
function isArray(value){
    return typeof value.reduce == "function" &&
    typeof value.filter == "function" &&
    typeof value.map == "function" &&
    typeof value.length == "number" ;


}
//Test the function 
console.log(isArray(1));//false
console.log(isArray("string"));//false
console.log(isArray({a:1}));//false
console.log(isArray(true));//false
console.log(isArray([]));//true
console.log(isArray([1,2,3,4,5]));//true
```
**12.0.15 Writing arrcmp**
  - Let’s write our own arrcmp function based on the assumption the array equality
means that each value at each corresponding index in both arrays match:

```javascript
let a = [1,2];
let b = [1,2];
let c = [5,5];
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
 console.log(arrcmp(a,b));//true
 console.log(arrcmp(b,b));//true
 console.log(arrcmp(a,b));//false
```

 - There is no built in function for comparing arrays in JavaScript. There is probably
a good reason for it. How data is mapped to an array largely depends on overall
design of the data in your application.
  - After all, what exactly does it mean for two arrays to be equal? The data layout
can be different from project to project. So is the nature of what you’re trying
to accomplish, by storing data in arrays. For this reason an array does not always
guarantee integrity between its values and indexes they are stored at.
Without a concrete project, we can only assume that it does.

**12.0.16 Improving objcmp**

  - Now that we have is array and arr cmp let’s add two special case comparisons to
the objcmp function: one for arrays using our new function, and one for objects
using recursion. This deepens our algorithm and makes it less prone to bugs.
We will call objcmp from itself (line 025) if one of the object properties checks
out to be an object literal itself:
```javascript
let a = [1,2];
let b = [1,2];
let c = [5,5];
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
console.log(objcmp(a,b))//true
console.log(objcmp({a:{b:12}},{a:{b:12}}));//true
console.log(objcmp({a:{b:12}},{a:{b:13}}));//false
console.log(objcmp({a:function(){}},{a:function(){}}));//false
```
  - A test for whether
property points to an array or an object literal was added. If the property is neither,
primitive value is tested as usual.

**12.0.17 Testing objcmp on a more complex object**
 - Let’s try it out in action!
```javascript
 console.log(objcmp(a,b))//true
console.log(objcmp({a:{b:12}},{a:{b:12}}));//true
console.log(objcmp({a:{b:12}},{a:{b:13}}));//false
console.log(objcmp({a:function(){}},{a:function(){}}));//false

```
  - Our object comparison function now works as expected. It’s not perfect but at
least it won’t get stuck in large majority of cases. In fact, it even checks object
properties recursively, which is a bit more of a deeper search than before.
  - Possible Improvements: You can further improve this function by checking for
arrays of objects, instead of just arrays of values.
As you can see, this is exactly why a native function for a deep search doesn’t exist.
  - It really depends on your data implementation. Who says your arrays will contain
objects or that any object property will ever point to another object? Without
this knowledge, it’s difficult to create a common-case algorithm without risking
creating an anti-pattern (when your code does more than it needs to.)

**Chapter Review**
  - Trying to solve one problem (compare two objects) led to discovery of another
problem we also needed to solve first (compare two arrays.) This is not something
we predicted at the time we thought of writing objcmp.
  - JavaScript already provides Array.isArray method – so why reinvent the wheel?
  - Taking initiative to solve any problem is what makes the distinction between a
hobbyist coder and a software developer. The skill of thinking for yourself to solve
problems, instead of using existing libraries, helps you train yourself for.
  - Writing your own code is always a good idea. If you can’t write an is array
function yourself, chances are you won’t have the practice and training to write
an important function later, one that doesn’t exist but is crucial to success of a
real-life project, facing much more complex problems.
  - This might cause you not only reputation among your peers, but the job itself.
  - Most interviews at software companies don’t test only for knowledge, they want
to see your problem-solving approach. Perhaps, it’s a good idea to develop it!

# **13.1 Functions**

  - In JavaScript there are two types of functions: the standard function that can be
defined using function keyword and an arrow function ()=>{} added later in ES6.
  - Regular functions can be called. But they can also act as object constructors,
when used together with new operator in order to create an instance of an object.
  - Note that since EcmaScript >= 6 you can use class keyword to the same effect.
  - Inside a function, the this keyword can point either to the context from which the
function was called. But it can also point to an instance of the created object, if
that function was used as an object constructor.
  - Functions have an array-like arguments object inside their scope, which holds the
length of parameters and values that were passed to the function, even if parameter
names were not present in function definition.
  - An arrow function can be called. But it cannot be used to instantiate objects.
  - Arrow functions are often used with functional programming style. Like regular
functions, they can be used to define object methods. They are also often used
as event callback functions. Inside the scope of an arrow function this keyword
points to whatever this equals to outside of its own scope.
  - Arrow functions do not have the array-like arguments inside their scope. 
 

**13.1.1 Function Anatomy**
  - The function definition consists of the function keyword followed by its name
(shown as update, in the following example) parenthesis containinga list of parameter names (a,b,c) and the function body enclosed in brackets:
```javascript
let num = 7;
let arr = [1,2];
let obj = {net:11};

function update(a,b,c,d = 'hi'){
return a,b,c,d;

}
const res=update(num,arr,obj);
console.log(res);
```
  - The return keyword is optional. But function will return anyway once all statements in its body are done executing, even if return keyword is not specified.
  - The this keyword inside an ES5 style function points to the context from which the
function was executed. Very often it is the global window object. If the function
is used to instantiate an object using new keyword then this keyword will point
to object instance that was instantiated using function.
  - The arguments is an array-like object that contains 0-index list of arguments that
were passed into the function, even if parameter names were not specified in the
function’s definition.
**13.1.2 Anonymous Functions**
  - Nameless or anonymous functions can be defined by using the same syntax but
skipping the function name.
  - Anonymous functions are often used as event callbacks, where we usually don’t
need to know what the names are – we simply want to execute them at a specific
time after an event has finished doing its work:
```javascript
setTimeout(function(){
    console.log("print something in 1 second.");
    console.log(arguments);
},1000);
```
  - Anonymous function used as a 
  setTimeout event callback.
 ```javascript
 document.addEventListner("click",function(){
   console.log("Document was clicked.");
   console.log(arguments);

 });
 ```
   - Anonymous function used to intercept a mouse click event.

**13.1.3 Assigning Functions To Variables**
  - Anonymous functions can be assigned to a variable, making them named functions
again. By doing this you can separate the function definition from its use in an
event-based method:
```javascript
let print = function(){
    console.log("Print something in 1 second.");
    console.log(arguments);
}
let clicked = function(){
    console.log("Document was clicked");
    console.log(arguments);
}
//call anonymous named functions
print();
clicked();
```
 - ”anonymous” functions that were assigned to a variable name become
named functions.
  - You can also pass them to the event functions just by their name:
```javascript
//cleaner code
 setTimeout(print,1000);
clicked();
document.addEventListener('click', clicked);
```
  - This often makes your code look cleaner. Note that different event functions
generate their own arguments, regardless of whether your anonymous function
defines parameters to catch them – they will be passed into the function:
```javascript
let clicked = function(event){
  console.log(event, event.target);
}
```
**Function Parameters**
  - Function parameters are optional. But in many cases you will find yourself defining
some. You can use default function parameters to pass things like primitives, arrays
and objects into a function. Anything that evaluates to a single value will do it:
```javascript
function fun(text, number, array, object, func, misc){
    console.log(text);
    console.log(number);
    console.log(array);
    console.log(object);
    console.log(func);
    console.log(misc);
    //Call the function by its parameter name
    func();
}

```
  - You can pass the name of another function. This way you can call that function
at some point later inside another function.
  - Let’s pass some arguments into function’s parameters:
```javascript
 function volleyball(){return "volleyball"};
fun("text",125,[1,2,3],{count:1},volleyball, volleyball());
```
  - Note that we’re passing the function name Volleyball and the result: Volleyball()
(which will evaluate to string value ”Volleyball.”) into the last two parameters of
the function Fun(); to get the following console output:

```console
text
125
[ 1, 2, 3 ]
{ count: 1 }
[Function: volleyball]
volleyball
```

  - That’s a useful variety of primitives and objects!
  - The last value is generated by ca-lling function Volleyball, which was passed into
parameter func. This means we can simply call it by calling func() instead of
Volleyball(), since func is its name inside the function.

**Checking For Types**
  - JavaScript is a dynamically-typed language. The type of a variable is determined
by its value. The variable definition simply assumes the type. This sometimes can
be the cause of subtle bugs.
  - For example, even though JavaScript provides a number of different object types
to work with, it doesn’t really provide an automatic safeguard that makes sure the
arguments passed into the function were what you expect them to be.
  - What if in the previous example, we passed an array or an object into func
parameter? The function expects it to be a function. We wouldn’t be able to
call func() if func wasn’t a function.
  - Let’s narrow down on the problem:

```javascript
function fun(func){
    console.log(func());//call the function by it's parameters name

}
var array = [];
var f = function() {return true}
fun(array);//pass array instead of function

```
  - But we cannot call an array. Hence, console output:
```console
 Uncaught TypeError: func is not a function
    at fun (<anonymous>:2:17)
    at <anonymous>:7:1

```
  - This is a problem if it happens in production code.

**Safeguarding Function Parameters**
  - The solution is to safeguard the value by checking its type. JavaScript has a
built-in directive typeof that we can use before calling the function: 

```javascript
function fun(func){
    //Call the function but only if it is a function:
    if(typeof func == "function")
      console.log(func());
      else
      console.log("Its not a function");
}
var array = [];
var f = function () {}
fun(array);//pass array instead of function
```
 - The function Fun(array) was called. The function expects a function name as
an argument but an array was sent.   - The typeof test failed and nothing happened
but at least our program didn’t break.
- You can do the same with other types if it becomes imperative that a particular
value must be in absolute compliance with a particular type.

**13.2 Origin of this keyword**

  - The this keyword was borrowed from C++. In its original design this keyword
was meant to point to an instance of an object in class definitions.
  - That’s it! There shouldn’t be much more to it.
  - But it seems like original designer of JavaScript language decided to use this
keyword to provide one extra feature: carrying a link to execution context, which
shouldn’t really be part of computer language feature design, but rather kept away
to its internal implementation:

  - You can’t avoid dealing with context in any programming language. But wiring
context into this keyword was a mistake and created duality and much confusion.
  - Later arrow functions were invented to deal with some of the side effects of this
odd-ball use-case for this keyword. And that is our next subject!


# **Chapter 14**

## **Higher-order Functions**

**14.0.1 Theory**

  - Higher-order functions may sound complicated but they are actually simpler than
their regular (first-order) functions that you’ve already been dealing with all along.
Higher-order functions, as the name suggests, is something that exists at a higher
level of thinking. That’s what abstraction is. If you want to become even better
at software development, abstraction is a very important concept to understand.
  - You can think of abstraction as the quality of dealing with ideas rather than gritty
details. Once you get a good grasp on it, abstraction will become your best friend.

**Abstraction**
  - When you are driving a car and you push the break pedal, you don’t think about
weight distribution, the brake caliper containing pistons that push the brake pads
against the disc, or how power assistance mode augments the pressure you are
placing on the pedal. You simply want the car to stop. That’s what you expect
to happen. You see? You’ve already been using abstract thinking – it’s natural.
  - How does this hold up in the context of writing software applications? In the
following section, we will write our own higher-order function map that will walk
through each item in an array, and apply a function to it. If our map function was
the car brake system from previous example, it would be the brake pedal.  
- It will be
responsible for controlling the brake calipers and pistons – a mechanism designed
to take care of the low-level details by making them abstract. So when we call map function, we don’t have to think of all the gritty details. We simply want
something to happen and have the expected result returned from the function.
  -That’s great, but before using the function we actually have to design its content
and determine how we want those gritty details to work.
  - JavaScript already supports several higher-order functions that do just that. But
before using them, we will write our own. If anything, this will help us deepen our
understanding not only of high-order functions but of abstraction in general.

**Writing your first higher-order function**
  - Not all problems can be solved with built-in JavaScript methods. Working on
custom software, you will be faced with situations where you would have to write
your own functions of this kind, or functions that require thinking in abstract terms
in order to produce the most efficient solution.

**The first-order function that applies an action**
  - The actual action happens not in map, but in the function passed to map as one
of its parameters. This means the map function doesn’t have one single purpose.
  - It is whatever the function passed into it does. And that can be anything.
  - We’ll create the map function and pass a first-order function into it, whose single
purpose will be to increment a numeric value by 1. Just like in the car brakes
example, the user of our map function should not be concerned about how the
internal for-loop iterates through all items. We just want to give it a task. In
order to do that, we will pass another function into the higher-order map function.
  - **Important:** What actually makes the function abstract is the fact that the higherorder function itself does not need to know exactly what it’s doing. It is simply
a logical scaffold to perform an action on a set of values. Much like a for-loop.
  - In fact, a for-loop is at its core. But when the function is actually being used, it
is of no concern. You can think of this as abstracting the for-loop (it becomes
assumed.)
  - They are actually often used together with first-order functions. Try not to think
of a higher-order function as a specific feature. They can behave as a for-loop.
  - But they can also be used as a way to instantiate an event – in which case a
first-order function would be used together with it as a callback function. They
are not limited to a single purpose. They enable a few different logical patterns that cannot be created using first-order functions alone.
  - For example Array.map iterates through a set of values and applies a modification.
  - The Array.reduce ”reduces” a set of values to a single value.
Event-based setTimeout is a higher-order function, and so is addEventListener.
**14.0.2 Definition**
  - A higher-order function is a function that either takes a function as one of its
parameters or returns a function (or both.)

**14.0.3 Abstract**

  - Here is one way of visually thinking about the pattern of a high-order function. It
exists as a higher level thinking.

**14.0.4 Iterators**
 - The Array.map method is one of the most common higher-order functions.  It
takes a function to run on every item in the array. Then it returns a modified copy
of the original array:
 - Here is a rather abstract way of thinking about the problem: ”Add 1 to each item
in the array.” Simple logic which is defined in add one function.
The Array.map method does not expose its loop implementation. The idea is not
to make the iterator merely more efficient either (although, that would help) but
hide it completely. We are only concerned with supplying a first-order function to
the map method. Internally, it will run the function on each value in the array.
 - This is a very powerful technique that can apply to many problems. But the
greatest advantage of using a higher-order function is that it abstracts problem
solving. It helps us focus on the key: running the function on each individual item
in the array, while abstracting away the for-loop (or while loop).
 - Let’s create the function that will modify the values. The body of the function
depends on what type of modifications you’re looking to apply to each array item.
 - We will create a first-order function called add one, which simply adds 1 to the
value. This is just a helper function that will work together with a higher-order
function (first-order and higher-order functions are often used together.)
```javascript
function addOne(value){return value + 1;}

```
 -For a function to qualify as a higher-order function it either needs to take a function
as one of its parameters, or return a function. As long as one of those conditions
is met we are creating a higher-order function.
 - The map function will take an array to work on. It will return a copy of that array
with each item modified by the add one function we have written earlier, which
will be passed as the second parameter.
 - Let’s write our own version of map which will be similar to what Array.map does:

```javascript
function maap(num, f){
    for (let index = 0; index < num.length; index++) {
        const original = num[index];
        let modify = f(original);
        copy[index] = modify;
        
    }
    return copy;
}
```

**Line-by-line explanation of map() function**
  - The function map takes two parameters: an arbitrary array of values and the
function which we want to apply to each item in the array.
```javascript
function map(array, f){}
```
 - First, copy array was created and assigned to an empty array literal: []. This array
will store a modified copy of the original array that was passed into the function.
```javascript
let copy = [];
```
  - Then a for-loop iterates through the array we received as first parameter. This
is the part we want to make abstract. When using the function we won’t even
have to think about the for-loop

```javascript
for (let index = 0; index < num.length; index++) {
```
  - Inside the loop, let’s copy the value at current index in the original array to a
temporary variable original.

```javascript
let original = num[index];
```

 - Now let’s pass the value in original variable to the first-order function that was
passed to this function:
```javascript
let modify = f(original);
```
  - The f function will do the magic (in our example, add 1 to the original value, but
it can be anything) and return the modified value. So let’s copy the modified value
into our copy array which is a placeholder for the entire modified array.
```javascript
copy[index] = modify;
        
```
 - Finally, a copy of the modified array is returned:

 ```javascript
 return copy
 ```
 - Once all items have been copied and processed by add one function, they will be
stored in copy array which will then be used as the return value of the function.
  - Side note: The reduce method – which is also a higher-order function – uses
something known as an accumulator. The accumulator in Array.reduce serves
a similar purpose as the copy array in this example. In reduce, however, the
accumulator is not an array – it is a single value that cumulatively gathers together
all items from the array and combines them into a single return value. That’s why
reducers are a better solution when you need to combine values.

**Calling our custom map function**
To see how it all works, first, let’s define an initial set of values to work with:

```javascript
let array=[0,1,2];
```
Let’s try out our map function in action:
```javascript
array = map(array,add_one);
```
  - Here add one is the function from earlier in this chapter. It simply adds 1 to the
value that was passed to it and returns it.
  - The result? The original array [0,1,2] is now [1,2,3]. All items in the array
were incremented by 1.
  - We’ve just written our own map method that internally does exactly the same
thing as the built-in method Array.map. This operation is so common that it was
added as a native method on the Array object.

**Calling Array.map function**
  - Yes, we can do exactly the same thing using a built-in Array method map. It does
exactly (or relatively) the same thing:
```javascript
array.map(addOne);
```
 - Sounds easy. We could have used this method from the very start. But by writing
our own map method we now actually understand how it works internally.
 - This will help us understand many other higher-order functions that implement
iteration over a list of items, such as filter, every, reduce, etc. They all use
similar internal code, with just a few slight differences.
**What happened to the for-loop?**
 - As you can see Array.map implements a for-loop internally. This isn’t the issue of
providing a more efficient for-loop, but rather, hiding it from our sight completely.
 - All we have to do is supply a function to the Array.map method. By hiding the
iteration steps, we are left only with writing the actual function that compares,
adds or filters each value individually.
 - This helps you to focus on solving the problem, instead of writing and re-writing
a lot of repetitive code. But it also makes your code look cleaner.

**14.0.5 Dos and Dont’s**
 - Often beginners use one method instead of another to accomplish relatively the
same thing. While it ”still works,” this choice shouldn’t be taken lightly.
 - Do use a high-order method for solving the problems it was intended to solve.
Understanding the differences between map, filter, reduce matters. This isn’t
about just the syntax differences, but writing efficient code and avoiding antipatterns. Try to find a proper method for the given task.
 - Do not use filter if you can get away with using reduce to accomplish the same
action with more efficiency. Different high-order functions are designed to deal
with problems specific to their implementation.

# **Chapter 15**
## **Arrow Functions**

 - Arrow functions do not have array-like arguments object. They also cannot be
used as constructors. The this keyword points to the same value this points to in
the scope just outside of the arrow function.

```javascript
let fun_1 = ()=> {};
```

**Arguments**
  - You can pass arguments to an arrow function via parameters.

```javascript
let x = (arg1, arg2) => {console.log(arg1,arg2);};
x(1,2);//1,2

```  
**Returning From An Arrow Function**
  - Arrow functions are primarily designed as expressions, so you might want to spend
extra time on learning how they return values

```javascript
let boomerang = a => "returns";
let karma = a => {return "returns";}
//let prayer = a => {return random()>=0.5};
let time = a => {"won't return";}
console.log(boomerang(1));//"returns"
console.log(karma(1));//"returns"
console.log(time(1));//[undefined]
//]
 let a = [1];
 console.log(a.map(boomerang));//"returns"
 console.log(a.map(karma));//"returns"
 console.log(a.map(time));//[undefined]
   console.log(x);
   console.log(y);
 console.log(z);
prayer("Make me understand JavaScript")
```
  - Takeaway: time arrow function is the only function that does not return a value
at all. Be careful not to use this syntax with higher-order functions.

**Similarities Between ES-style Functions**
 - There are some similarities between arrows and classic functions. Most of the time
you can use arrow functions as a replacement to standard ES5 functions without
a hitch!
Let’s try this example to get started with our discussion about arrow functions.
I defined two classic ES5 functions classic one and classic two, followed by
definition of arrow – an ES6-style arrow function:

```javascript
function classic_one(){
    console.log("classic function one.");
    console.log(this);
}
var classic_two = function(){
    console.log("classic function two.");
    console.log(this);
}
let arrow = ()=>{
    console.log("arrow function");
    console.log(this);
}
```
 - I added console.log(this); statement to the scope of each function, simply
to see the outcome.
Let’s call all 3 functions i

```javascript
//call the first function
classic_one();
//call the second function
classic_two();
//call third function
arrow();
```
Console output:


```console
VM10:2 classic function one.
> Window
VM10:6 classic function two.
> Window
VM10:10 arrow function
> Window
```
 - When defined in global scope, it only seems like there is no difference between
classic and arrow functions, in terms of this binding.

**No this binding**
  - Arrow functions do not bind this keyword. They look it up from whatever this
equals in the outer scope, just like any other variable. Hence, you can say arrow
functions have a ”transparent” scope.

**No arguments object**

  - The arguments object does not exist in arrow function scope, you will get a
reference error if you try to access it:

```javascript
let a = ()=>{
  console.log(arguments);//undefined

}
```
 - Just as a reminder here, the arguments object does exist on classic ES5 functions:
```javascript
function f(){
   console.log(arguments);
 }
```

**No Constructor**
  - ES5-style functions are object constructors. You can create and call a function
but you can also use same function as an object constructor – together with new
operator – to instantiate an object.  The function itself becomes class definition.
 - For this reason you would often hear it said that in JavaScript all functions are
objects. After ES6 specification introduced arrow functions to the language this
statement is no longer true. Arrow functions cannot be used as object constructors.
 - Therefore, arrow functions cannot be used to instantiate objects. They work best
as event callbacks or function expressions in methods such as Array.filter,
 - Array.map, Array.reduce and so on... In other words, they are more proper in
context of Functional Programming style.
 - Thankfully, modern JavaScript is rarely written using ES5-style functions masquerading as object constructors. It’s probably a good idea to start defining your
classes using class keyword anyway, instead of using function constructors.

**When classic and arrow functions are used as event callbacks**
There is a difference between classic ES5 functions and arrows, when they are used
as event callbacks.
Here is an example of an arrow function that outputs a string and this property
to console in the event of a click on the document:
```javascript

let arrow = (event) =>{
    console.log("Hello, I am an arrow funciton");
    console.log(this);
}
document.addEventListener("click", arrow);
```
 - And here is the same exact event using classic ES5 function syntax:

```javascript
function classic(event){
    console.log("Hello, I am a classic ES5 function");
    console.log(this);
}
document.addEventListener("click",classic);
```
**So what’s the difference?**
 - Here is console output after clicking on document in each case:
 Hello, I am an arrow funciton
```console
Hello, I am arrow function 
3 Window
8 Hello, I am a classic ES5 function
9 #document
```
 - Inside the arrow function’s scope this property points to Window object.
  - In classic ES5 function this property points to the target element that was clicked.
  - What happens here is that arrow function took the Window context with it, instead
of giving you the object that refers to the clicked element.

**Inherited this Context**
  - But wait, how did the arrow function inherit Window context in the first place? Is
that because it was defined in global scope (same as the object of type Window)?
  - Not exactly.
  - The arrow function inherits the lexical scope based on where it was used, not
where it was defined. Here it so happens that the arrow function was both defined
and called in global scope context (Window object.)
  - To truly understand this, let’s draw another example, where I will attach arrow
function B() to a click event.
But this time, I will execute addEventListener function from another class called
  - Classic instead of Window like in the previous example.
  - Remember that when you use new operator, you execute the function as though
it was an object constructor. This means that every statement inside it will be
executed from the context of its own instantiated object: object, not window.
```javascript
function classic(){
    let b = () => {
        console.log("Hello, I am arrow functionB()");
        console.log(this);
    }
    document.addEventListener("click",b);
}
let object = new classic();
```
 - A new context is created when using new operator to instantiate an object. Anything called from within that object will have its own context.
 - After running this code and clicking on document, we get following console output:
```console
Hello, I am an arrow funciton
[object classic]
```
 - The object instance delimited by [] brackets is of type Classic. And that’s exactly
what happens here.
 - Event was attached from context of Classic constructor and not from the context
of global scope object Window like in the previous examples.
 - The event has literally ”taken the context it was executed from” with it into its
own scope via the this property.
 - This type of context chaining is common to JavaScript programming. We’ll see
it once again when we explore prototype-based inheritance in more depth later in
the book. The idea of execution context may start to become more clear by now.

# **Chapter 16**
 
 **Creating HTML Elements Dynamically**

 - JavaScript creates a unique object for each HTML tag currently present in your
*.html document. They are automatically included to DOM (Document Object
Model) in your application once the page is loaded into browser. But what if we
want to add new elements without having to touch the HTML file?
 - Creating and appending another element to an existing element will dynamically
insert it into the DOM and instantly display it on the screen as if it were directly
typed into the HTML source code.
 - However, this element is not typed directly into your HTML document using HTML
tag syntax. Instead, it is created dynamically by your application.
The method createElement natively exists on the document object. It can be
used to create a new element:

```javascript
let E = document.createElement("div");
let E1 = document.createElement("span");
let E2 = document.createElement("p");
let E3 = document.createElement("img");
let E4 = document.createElement("input");

```

 - At this point none of the created elements are attached to DOM yet.

**16.0.1 Setting CSS Style**

  - So far we created an empty element without dimensions, background color or
border. At this point all of its CSS properties are set to defaults. We can assign
a value to any standard CSS property via style property.

```javascript
let div = document.createElement("div");
//set ID of the element
div.setAttribute("id","element");
//set class attribute of the element
div.setAttribute("class","box");

div.style.position = "absolute";
div.style.display = "block";
div.style.width = "100px";//px is requried
div.style.height = "100px";//px is requried
div.style.top = 0; //px is not required
div.style.left = 0;//px is not required
div.style.zIndex = 1000; // z-index of > zIndex
div.style.borderStyle = "solid";
div.style.borderColor = "gray";
div.style.borderWidth = "1px";
div.style.backgroundColor = "white";
div.style.color = "black"; 

```

 - In CSS dash (-) is a legal property name character. But in JavaScript it is always
interpreted as the minus sign. Using it as part of a JavaScript identifier name will
cause an error. For this reason, single-word CSS property names remain the same
– style.position and style.display for example. Multi-word property names are
changed to camel-case format, where the second word is capitalized. For example
z-index becomes .zIndex, and border-style becomes .borderStyle.

**16.0.2 Adding Elements To DOM with .appendChild method**

  - Method element. appendChild(object ) inserts an element object into DOM.
  - Here element can be any other element that currently exists in the DOM.
  - This method exists on all DOM element objects, including document.body.

**document.body**
 - Insert the element into the body tag using appendChild method:

```javascript
document.body.appendChild(div);
```
 - Although very common the body tag is not the only place you can add the newly
created element.

**getElementById**
  - Insert element into another element by id:
```javascript
document.getElementById("id-1").appendChild(div);
```

**querySelector**
 - Insert element to any element selected using a valid CSS selector:

```javascript
 //Insert element into another element with id = "id-1"
let selector = "#parent .inner .target";
document.querySelector(selector).appendChild(div);
```

**16.0.3 Writing A Function To Create Elements**
  - Writing your own functions is fun. And sometimes necessary. In this section we will
write our own function that makes it easy to create HTML elements dynamically.
Before writing the function body, let’s take a closer look at its parameters.

**Function Parameters**
  - To accommodate for most cases, we don’t need to include all CSS properties, just
ones that have most impact on element’s visual appearance

```javascript
let element = (id,type,l,t,w,h,z,r,b)=>{};
```
 - Most of the parameters are optional. If you skip them, either default values will
be used – defined using const keyword inside the function body (see next page)
– or not assigned (if you pass null, for example.)
 - Last parameters on the argument list: r and b (right and bottom) will override
standard placement in top and left corner of the parent element.
 - Using this function we can create basic HTML elements with one line of code:

```javascript
let a = element("id-1","static",0,0,100,25,"unset");
let b = element("id-2","relative",0,0,50,25,1);
let c = element("id-3","absolute",10,10,50,25,20);
```

**Function Body**
  - Let’s take a look at the body of the element-creation function:

 ```javascript
 //create a generic HTML element
let element =(id,type,l,t,w,h,z,r,b,value,color)=>{
    //default-used to replace missing arguments
    const position=0;
    const size=10;
    const Z=1;

    //create a <div> element dynamically
    let div=document.createElement("div");
    //inner html
    div.innerHTML=value;
    //set ID of the element
    div.setAttribute("id",id);
    //set abosolute behavior
    div.style.position=type;
    div.style.display="block";
    div.style.color = color;
    if(r)//if right is provided,reposition element
        div.style.right=r?r:position+"px";
    else
        div.style.left=l?l:position+"px";

    if(b)//if bottom is provided,reposition element
        div.style.bottom=b?b:position+"px";
    else
        div.style.left=t?t:position+"px";

    div.style.width=w?w:size+"px";
    div.style.height=h?h:size+"px";
    div.style.zIndex=z?z:Z;
    
    //return the element object we just created
    return div;
};
document.body.appendChild(element("id1","button",10,10,200,10,10,10,10,"created by function","blue"));
 ```
  - Place this function into separate file common-styles.js

 -  create HTML file to run the javascript.

```html
<html>
    <head>
        <title>example</title>
        <script src="functionBody.js" defer></script>
    </head>
    <body>
        <h2>Example for create element using function</h2>
    </body>
</html>

```

 - Creating UI elements often requires pixel-perfect precision. This function will create a position:absolute element (unless otherwise specified) with default size
of 10px in each direction, unless replacement values are supplied via its arguments:
w and h parameters.
 - As a quick reminder here is the behavior of HTML elements with position set
to absolute based on point of attachment.
 - Note that the element can be attached to the logical coordinate position within
the parent. For example top:0; right:0 attaches the element to the upper right
corner of the parent.
 - The direction in which the attached element will move, when its coordinates are
provided using negative values are displayed in the following diagram.

**Importing And Using element() Function**
 - Let’s import the function we created above into our project.
To import a module type attribute on script tag must be set to "module".

```javascript
<html>
  <head>
    <title>use element</title>
    <script type = "module">
    import {absolute} from "./functionBody.js";
    let a = absolute("id-1",0,0,100,50,1);
    let b = absolute("id-2",null,null,25,25,1,10,5);
    b.addElement(a);
    document.body.addElement(a);
    </script>
</head>
<body></body>
</html>

```

 - We can now create an HTML element using just one line of code.
 - In this example we created two elements A and B. Then we nested element B in
element A, and attached element A to the body container.


**16.0.4 Creating objects using function constructors**
 - Let’s create a function called Season:
```javascript
 function season(name){
    this.name = name;
    this.getName = function(){
        return this.name;
    }
}

```
 - To instantiate four seasons:
 let winter = new season("winter");
let summer = new season("summer");
let spring = new season("spring");
let autumn = new season("autumn");
```javascript
let winter = new season("winter");
let summer = new season("summer");
let spring = new season("spring");
let autumn = new season("autumn");
 
```
 - We just created 4 instances of the same type:
```javascript
 console.log(winter.getName());
console.log(summer.getName());
console.log(spring.getName());
console.log(autumn.getName());
```
 - This creates a problem, because function getName is copied 4 times in memory,
but its body contains exactly the same code.
 - In JavaScript programs Objects and Arrays are created all the time. Imagine if
you instantiated 10000 or even 100000 objects of a particular type, each storing a
copy of the same exact method.
 - This is rather wasteful. Could we somehow have a single getName function?
 - The answer is yes. For example, native function .toString() you may have used
before as Array.toString() or Number.toString() exists in memory at a single
location, but it can be called on all built-in objects! How does JavaScript do it?


# **Chapter 17**

**Prototype**

 - When a function is defined two things happen: the function object is created,
because functions are objects. Then, a completely separate prototype object is
created. The prototype property of the defined function will point to it.
 - Let’s say we defined a new function Human:

```javascript
 function Human(name){}
```
 - You can verify that prototype object is created at the same time:
```javascript
typeof Human.prototype;//"object"
```
 - Human.prototype will point to the prototype object. This object has another
property called constructor, which points back to the Human function:
 - Human is a constructor function, used to create objects of type Human. Its
prototype property points to a separate entity in memory: prototype object.
 - There is one separate prototype object per each unique object type (class).
Some will argue that there are no classes in JavaScript. But technically, Human
is a unique object type, and basically that’s what a class is.
 - If you come from C++ background, you can probably refer to Human as a class.
 - A class is an abstract representation of an object. It’s what determines its type.
 - Note, prototype property is not available on an instance of an object, only on the
constructor function. On an instance, you can still access prototype via proto ,
but should probably use static method Object.getPrototypeOf(instance) which
returns the same prototype object as proto (in fact proto () is a getter.)

**17.0.2 Prototype on Object Literal**
 - To draw a simple example, let’s create an object literal:

```javascript
 let literals = {
    prop:123,
    meth: function(){}
};
```
 - Internally it is wired into prototype as an object of type Object, even though it
wasn’t created using the new operator.
```javascript
literals.__proto__;  //object{}
literals.__proto__.constructor; //ƒ Object() { [native code] }
literals.constructor; //ƒ Object() { [native code] }
```
  - When literal was created, literal. proto was wired to point to Object.prototype:

   - Object.prototype was already created internally by JavaScript. Whenever a new
object type is defined, a secondary object to serve as its prototype is created.

**17.0.3 Prototype Link**

 - When an object is instantiated using new keyword, the constructor function executes to build the instance of that object.

```javascript
let instance = new Object();
instance.prop = 123;
instance.meth = function(){};
//instance={prop: 123, meth: ƒ}
```
 - In this case Object constructor function is executed and we get a constructed
link, that looks like this:

 - The .prototype property points to a separate object: the built-in prototype object.
 - In this case it’s Object.prototype. It is similar to Human.prototype from the
earlier example: in this case we just don’t control how Object was created, because,
 - Object is a preexisting built-in type.

**17.0.4 Prototype Chain**
 - It can be argued that Array is a child of its parent type Object.
 Object.prototype is Object, but not because Object is inherited from Object.
 - This is simply because the prototype itself is just an object: they co-exist.
 - You can think of this as Object’s prototype being null, because it’s the top-level
object on the prototype chain. In other words Object does not have an abstract
prototype. Object does have a ”ghost” prototype object just like any other type.
 
 **17.0.5 Method look-up**
 - When you call Array.toString() what actually happens is, JavaScript will first
look for method toString on the prototype of Array object. But it does not find
it there.
 - Next, JavaScript decides to look for toString method on the prototype
property of Array’s parent class: Object.
 - It finally finds Object.prototype.toString() and executes it.
 
**17.0.6 Array methods**
 - In previous section we’ve taken a look at prototype chain and how .toString
method is found by traversing the prototype chain. But .toString is available on
all objects that stem from the Object type (which is most built-in types.)
 - The same is true for Number, String and Boolean built-in types. You can call
toString method on each one of them, and yet it exists only in one place in
memory on Object.prototype property.
 - Methods native to Array type should exist on Array.prototype object.
 - It is obvious that there isn’t much use in having higher-order functions like .map,
.filter and .reduce attached to  
 - Number or Boolean types.
The fact is, every single Array method already exists on Array.prototype:
   ```javascript
   [1, 2, 3]
   3
   1
   0: 1
   1: 2
   2: 3
   length: 3
   [[Prototype]]: Array(0)
   at: ƒ at()
   concat: ƒ concat()
   constructor: ƒ Array()
   copyWithin: ƒ copyWithin()
   entries: ƒ entries()
   every: ƒ every()
   fill: ƒ fill()
   filter: ƒ filter()
   find: ƒ find()
   findIndex: ƒ findIndex()
   flat: ƒ flat()
   flatMap: ƒ flatMap()
   forEach: ƒ forEach()
   includes: ƒ includes()
   indexOf: ƒ indexOf()
   join: ƒ join()
   keys: ƒ keys()
   lastIndexOf: ƒ lastIndexOf()
   length: 0
   map: ƒ map()
   pop: ƒ pop()
   push: ƒ push()
   reduce: ƒ reduce()
   reduceRight: ƒ reduceRight()
   reverse: ƒ reverse()
   shift: ƒ shift()
   slice: ƒ slice()
   some: ƒ some()
   sort: ƒ sort()
   splice: ƒ splice()
   toLocaleString: ƒ toLocaleString()
   toString: ƒ toString()
   unshift: ƒ unshift()
   values: ƒ values()
   Symbol(Symbol.iterator): ƒ values()
   Symbol(Symbol.unscopables): {copyWithin: true, entries: true, fill: true, find: true, findIndex: true, …}
   [[Prototype]]: Object
   constructor: ƒ Object()
   hasOwnProperty: ƒ hasOwnProperty()
   isPrototypeOf: ƒ isPrototypeOf()
   propertyIsEnumerable: ƒ propertyIsEnumerable()
   toLocaleString: ƒ toLocaleString()
   toString: ƒ toString()
   valueOf: ƒ valueOf()
   __defineGetter__: ƒ __defineGetter__()
   __defineSetter__: ƒ __defineSetter__()
   __lookupGetter__: ƒ __lookupGetter__()
   __lookupSetter__: ƒ __lookupSetter__()
   get __proto__: ƒ __proto__()
   set __proto__: ƒ __proto__()
   1,2,3
   1
   2
   30mpg
   ```
   - Looks like our favorite methods .map, .filter and .reduce live on
   Array.prototype object.

  - If you want to extend functionality of the Array method specifically, attach a
method to Array.prototype.my method.

**17.1.1 Extending Your Own Objects**
 - Number’s and Array’s parent is Object. This is great, but what if we want to
extend our own object from another object?
 - As we saw from the preceding diagrams proto getter is part of internal prototype implementation. It’s crucial for establishing the link, but we shouldn’t mess
with it directly. For the same reason.
 - JavaScript is a dynamically typed language, so you can try to create some object
constructors and rewire the proto property on their prototype object to the
”parent”, but this is often considered to be a hack. In practical coding situation,
you will actually never need to do anything like this. There is literally no software
you would possibly be writing that modifies the internal function of prototype.
 - After EcmaScript 6 you are encouraged to create and extend classes using class
and extends keywords and let JavaScript worry about prototype links.

**17.1.2 constructor property**
 - The constructor property of Object class points to Function:
 - The constructor property of Function class points to Function:
 - This creates a circular dependency around the Function class:
 - Function.constructor is Function (circular.) But Object.constructor is also Function. This can imply that a class is constructed using a function. Yet, Function
itself is a class. This is circular dependency.

**17.1.3 Function**
 - Function is the constructor of all object types.

**17.2 Prototype In Practice**
 - Understanding how prototype works is a gradual process. It might be a difficult
task, considering JavaScript language has evolved over the years. To get a better
idea of how it all works, we’ll start from the very beginning.
 - We’ve already covered the theory behind prototype in the previous section of this
chapter. In this section we will finally arrive at prototype in terms of how fits into
the big picture when it comes to actually writing code.
 - This section is a thorough walk-through that demonstrate different ways of working
with objects. And what’s a better place to start than the object literal?

**17.2.1 Object Literal**
 - In this example cat object was defined using a simple object literal syntax. In
some ways, under the hood JavaScript wires up all the prototype linking.
 - Throughout the following sections of this chapter we will gradually update this
example and build on it to finally arrive at how prototype can be useful to you as
a JavaScript programmer.

```javascript
let cat = {};
cat.name = "Felix";
cat.hunger = 0;
cat.energy = 1;
cat.sate = "idle";
```
 - We named our cat specimen Felix, gave him 0 level of hunger and 1 unit of energy.
Currently Felix is in idle state. Just where we want him to be!

```javascript
//Sleep to restore energy
cat.sleep = function(amount){
    this.state = "sleeping";
    console.log(`${this.name} is ${this.state}.`);
    this.energy += 1;
    this.hunger += 1;
    }

//wake up
cat.wakeup = function(){
    this.state = "idle";
    console.log(`${this.name} woke up`);
}

//Eat until hunger is quenched
cat.eat = function(amount){
    this.state="eating";
    console.log(`${this.name} is ${this.state} ${amount} unit(s) of food.`);
    if(this.hunger -= amount <=0)
       this.energy += amount;
    else 
       this.wakeup();
}

//Wandering depletes energy
//If necessary, sleep for 5 hours to restore energy
cat.wander = function(){
    this.state = "wandering";
    console.log(`${this.name} is ${this.state}.`);
    if(--this.energy<1)
     this.sleep(5);
}

cat.sleep();
cat.wakeup();
cat.eat(5);
cat.wander();
```

 - Methods sleep, wakeup, eat and wander were added directly to the instance
of the cat object. 
 - Each method has basic implementation that either restores or
depletes cats energy.

**817.2.2 Using Function Constructor**
 - Even after some sleep Felix feels a bit of melancholy. He needs a friend.
 - But instead of creating a new object literal, we can place the same code inside a
function called Cat to represent a global Cat class: 

```javascript
console.log(typeof Object.prototype); 
function cat(name, hunger, energy, state){
    let cat = {};
    cat.name = name;
    cat.hunger = hunger;
    cat.energy = energy;
    cat.state = state;
cat.sleep = function(){
    this.state = "sleeping";
    console.log(`${this.name} is ${this.state}`);
    this.energy += 1;
    this.hunger += 1;
}

cat.wakeup = function (){
    this.state = "idle";
    console.log(`${this.name} woke up. `);
}
cat.eat = function (){}
cat.wander = function (){}
 return cat;
}
```
 - Note that all that was done here is we moved the exact same code we wrote in the
previous section into a function and returned the object using the return keyword.
 - The methods implementation remained the same too. I simply used the comment
markers /* implement */ to avoid repeating the same code again

```javascript
let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();
let tom = cat("tom",5,1,"sleeping");
tom.sleep();
```

**17.2.3 Prototype**
 - Branching out from previous example, we see a problem.
 - All of the methods of Felix and Luna take twice as much space in memory. This
is because we are still creating two object literals for each cat.
 - And this is the problem prototype tries to solve.
Why don’t we take all of our methods and place them at a single location in
memory instead?

```javascript
const prototype = {
    sleep(amount){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    },
    wakeup(amount){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    },
    eat(amount){

    },
    wander(amount){

    }

}
```
 - Now all of our neatly packaged methods share a single place in memory.
 - Let’s go back to our Cat class implementation, and wire the methods from the
above prototype object directly into each method on the object:

```javascript
function cat(name, hunger, energy, state){
    let cat = {};
    cat.name = name;
    cat.hunger = hunger;
    cat.energy = energy;
    cat.state = state;

    cat.sleep = prototype.sleep;
    cat.wakeup = prototype.wakeup;
    return cat;
}

let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();

```

 - Before we see how JavaScript does this, let’s take a look at something else.

**17.2.4 Creating objects using Object.create**
 - In JavaScript we can also create objects using Object.create method, which takes
a clean slate object as one of its arguments:

```javascript
const cat = {
    name: "Tom",
    state: "idle",
    hunger: 1,
}
const kitten = Object.create(cat);
kitten.name = "Loki";
kitten.state = "sleeping";
```

 - Now let’s take a look at kitten:

```javascript
console.log(kitten);
```
 - Mysteriously, object kitten has only two methods – it is missing hunger property.

```cosole
{ name: 'Loki', state: 'sleeping' }
```

 - To explain this, let’s see what will happen if we actually try to output it:
```javascript
console.log(kitten.hunger);//1
```
 - This behavior is unique to objects created via Object.create method. When we
try to get kitten.hunger, JavaScript will look at kitten.hunger, but will not find
it there (because it wasn’t created directly on the instance of the kitten object.)
 - Then what happens is JavaScript will look at .hunger property in cat object.
 - Because kitten was created via Object.create(cat), kitten considers cat to be
its parent so it looks there.
 - Finally it finds it on cat.hunger and returns 1 in console. Again, property hunger
is stored only once in memory

**17.2.5 Back To The Future**
 - Let’s rewind a bit and go back to the earlier example from section called Using
 - Function Constructor fully equipped with new knowledge about Object.create.

```javascript
const prototype = {
    sleep(amount){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    },
    wakeup(amount){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    },
    eat(amount){

    },
    wander(amount){

    }

}

function cat(name, hunger, energy, state){
    let cat = {};
    cat.name = name;
    cat.hunger = hunger;
    cat.energy = energy;
    cat.state = state;

    cat.sleep = prototype.sleep;
    cat.wakeup = prototype.wakeup;
    return cat;
}
```
 - Let’s delete the part where we wired our own prototype object into the methods
of Cat class, and instead pass them into the native Object.create method which
will now reside inside our Cat function (source code listing above.)
 - Now we can create felix and luna via this new Cat function as follows:

```javascript
let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();
```
 - Now we get the ideal syntax, and sleep() is defined only once in memory. No
matter how many felixes or lunas you create, we’re no longer wasting memory
on their methods, because they are defined only once.

**17.2.6 Constructor Function**
 - Let’s recall that each Object has a prototype property pointing to its ghost prototype object:

```javascript
console.log(typeof Object.prototype);//"object"
```
 - So now what we can do is attach all Cat methods directly to its built-in prototype
property instead of our own ”prototype” object we created earlier:

```javascript
function cat(name, hunger, energy, state){
    let Cat = Object.create(cat.prototype);
    Cat.name = name;
    Cat.hunger = hunger;
    Cat.energy = energy;
    Cat.state = state;

    return Cat;
}

 cat.prototype.sleep = function (){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    };
    cat.prototype.wakeup=function(){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    };
    cat.prototype.eat=function(){};
    cat.prototype.wander=function(){};

let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();
```
 - In this scenario, JavaScript will look for .sleep on luna object, and will not find
it there. It will then look for .sleep method on Cat.prototype. It finds it there
and the method is invoked.

```javascript
let tom = cat("sam",5,1,"sleeping");
tom.wakeup();
tom.sleep();
```
 - The same happens here, .wakeup method is executed on Cat.prototype.wakeup,
not on the instance itself.
 - Therefore the main purpose of prototype is to serve as a special look up object,
which will be shared across all instances of objects instantiated with its constructor
function while preserving memory.

**17.2.7 Along came new operator**
 - We can wipe out everything we learned up to this point and replace it all with
new operator – which will automatically do every single thing we’ve just explored
in the previous sections of this chapter!
```javascript
function cat(name, hunger, energy, state){
    let Cat = Object.create(cat.prototype);
    Cat.name = name;
    Cat.hunger = hunger;
    Cat.energy = energy;
    Cat.state = state;

    return Cat;
}
```
 - Let’s remove Object.create and return cat from our class definition.
 - In JavaScript functions defined with function keyword are hoisted. This means
we can add methods to Cat.prototype before Cat is defined:

```javascript

    cat.prototype.sleep = function (){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    };
    cat.prototype.wakeup=function(){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    };
    cat.prototype.eat=function(){};
    cat.prototype.wander=function(){};

``` 

Followed by Cat definition:

```javascript
function cat(name, hunger, energy, state){
    Cat.name = name;
    Cat.hunger = hunger;
    Cat.energy = energy;
    Cat.state = state;
}

```

 - Now we can instantiate sam as follows:
```javascript
 let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();

```

**17.2.8 The class keyword**
 - Everything we’ve just explored about prototype was converging toward the class
keyword added in EcmaScript 6.
 - How prototype works is a common subject during JavaScript interviews. But in
production environment, you will never (spelling is correct) have to touch it at all
in your entire career as a front-end software engineer.

```javascript
class cat{
    constructor(name, hunger, energy, state){
        this.name = name;
        this.hunger = hunger;
        this.energy = energy;
        this.state = state;
    }
    sleep(amount){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    }
    wakeup(amount){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    }
    eat(amount){
    }
    wander(amount){
    }
}
```

 - Use class and new keywords. Let JavaScript worry about prototype:

```javascript
 let sam = new cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();
let tom = new cat("tom",5,1,"sleeping");
tom.wakeup();
tom.sleep();
```
 - In the next section we will take this concept further to design an entire application using OOP: Polymorphism with examples via Inheritance and Object
Composition and just a bit of Functional Programming style.

# **Chapter 18**

**Object Oriented Programming**

 - In this chapter we will exemplify OOP by building a cooking range with stove.
 - The best example of Object Oriented Programming would be based on many
different types of objects. We will define a class for each abstract type: Fridge,Ingredient, Vessel, Range, Burner, and Oven.
 - We will take a look at two key OOP principles: inheritance and polymorphism
in the sense of how it actually relates to JavaScript code.

**JavaScript Classes**
 - In JavaScript, classes are the special type of functions. We can define the class just like function declarations and function expressions.

 - The JavaScript class contains various class members within a body including methods or constructor. The class is executed in strict mode. So, the code containing the silent error or mistake throws an error.

 - The class syntax contains two components:

    - Class declarations
    - Class expressions

[Refer from this](https://www.javatpoint.com/javascript-oops-classes)

**Class Declarations**
  - A class can be defined by using a class declaration. A class keyword is used to declare a class with any particular name. According to JavaScript naming conventions, the name of the class always starts with an uppercase letter.

**Class expressions**
 - Another way to define a class is by using a class expression. Here, it is not mandatory to assign the name of the class. So, the class expression can be named or unnamed. The class expression allows us to fetch the class name. However, this will not be possible with class declaration.
```javascript
var emp = class {  
  constructor(id, name) {  
    this.id = id;  
    this.name = name;  
  }  
  console.log(emp.name);
```

**JavaScript Encapsulation**
 - The JavaScript Encapsulation is a process of binding the data (i.e. variables) with the functions acting on that data. It allows us to control the data and validate it. To achieve an encapsulation in JavaScript: -

    - Use var keyword to make data members private.
    - Use setter methods to set the data and getter methods to get that data.
 - The encapsulation allows us to handle an object using the following properties:

    - Read/Write - Here, we use setter methods to write the data and getter methods read that data.

    - Read Only - In this case, we use getter methods only.

```javascript
//Allows us to control data and variable
//Allows to handle an object read/write
class Student  
  {  
    constructor()  
    {  
       var name;  
       var marks;  
    }  
        getName()  
        {  
          return this.name;  
        }  
      setName(name)  
      {  
        this.name=name;  
      }  
        
      getMarks()  
      {  
        return this.marks;  
      }  
    setMarks(marks)  
    {  
        if(marks<0||marks>100)  
        {  
          console.log("Invalid Marks");  
        }  
      else  
        {  
          this.marks=marks;  
        }  
    }  
    }  
    var stud=new Student();  
     stud.setName("Praveen");  
     stud.setMarks(90);//alert() invokes  
     console.log(stud.getName()+" "+stud.getMarks());  

```

**JavaScript Inheritance**
 - The JavaScript inheritance is a mechanism that allows us to create new classes on the basis of already existing classes. It provides flexibility to the child class to reuse the methods and variables of a parent class.

 - The JavaScript extends keyword is used to create a child class on the basis of a parent class. It facilitates child class to acquire all the properties and behavior of its parent class.

**Points to remember**
 - It maintains an IS-A relationship.
 - The extends keyword is used in class expressions or class declarations.
 - Using extends keyword, we can acquire all the properties and behavior of the inbuilt object as well as custom classes.
 - We can also use a prototype-based approach to achieve inheritance.

```javascript
 class Bike  
{  
  constructor()  
  {  
    this.company="Honda";  
  }  
}  
class Vehicle extends Bike {  
  constructor(name,price) {  
   super();  
    this.name=name;  
    this.price=price;  
  }   
}  
var v1 = new Vehicle("Shine","70000");  
console.log(v1.company+" "+v1.name+" "+v1.price);  
const v2 = new Vehicle("Trigger", "90000") ;
console.log(v2.company+" "+v2.name+" "+v2.price);
```

**JavaScript Polymorphism**
 - The polymorphism is a core concept of an object-oriented paradigm that provides a way to perform a single action in different forms. It provides an ability to call the same method on different JavaScript objects. As JavaScript is not a type-safe language, we can pass any type of data members with the methods.

```javascript
 class A  
  {  
     display()  
    {  
      console.log("A is invoked");  
    }  
  }  
class B extends A  
  {  
    display()  
    {  
      super.display();//invoke both method 
      console.log("B is invoked");  
    }  
  }  
  
// var a=[new A(), new B()]  
// a.forEach(function(msg)  
// {  
// msg.display();  
// });  
var b = new B();
b.display();

```

**JavaScript Abstraction**
 - An abstraction is a way of hiding the implementation details and showing only the functionality to the users. In other words, it ignores the irrelevant details and shows only the required one.

**Points to remember**
 - We cannot create an instance of Abstract Class.
 - It reduces the duplication of code.

```javascript
class Car{
    constructor(color,cost,milage){
        this.color = color;
        this.cost = cost;
        this.milage = milage;
        //this.nextYearPrice = 20000; //data is not hiding here
        }
        getdetails(){
            console.log(this.color);
            console.log(this.cost);
            console.log(this.milage);
        }
        getNextYearPrice(){
            let nextYearPrice = 20000;//hide the price of next year
            console.log(this.cost+nextYearPrice);
        }
}

let swift = new Car("red",800000,"25");
swift.getdetails();
swift.getNextYearPrice();
```

# **Chapter 19**

## **Events**

 - Events are functions executed at the time when a specific action occurs. For example, if user clicks on a UI button or any other HTML element, browser dispatches
an ”onclick” event associated with HTML element that was clicked.
 - There are two types of events: browser events and synthetic events.

**19.0.1 Browser Events**
 - Built-in browser events are already pre-determined and executed by the browser
when an action occurs. You don’t need to create them yourself, only to intercept
them – if you wish something else to happen after they occur.
 - When browser window changes size, a resize event is automatically dispatched.
 - This might be a good place to adjust your UI layout to the new area.
 - Mouse events are also an example of built-in browser events. When a mouse
is moving onmousemove event is dispatched, continuously re-calculating mouse
position and exposing them via event.clientX and event.clientY property names.
 - When the mouse button is pressed down onmousedown event is dispatched and
when it is released onmouseup event will occur. You can intercept these events
and supply a callback function that contains commands you want to be executed
after the event occurs. This is incredibly useful for implementing custom UI experience: for example, display a custom menu when a mouse button is clicked.

**19.0.2 Synthetic Events**
 - Built-in browser events are nice, but to truly understand how they work, we’ll start
with synthetic events. This will give us a good idea of how events are created and
dispatched in JavaScript.

**Event Object**
 - You can create and dispatch your own events using Event object. Events created
in this way are called synthetic events because they are not generated by the
browser itself, but rather by your program. Let’s create a synthetic event just to
see how events work in JavaScript at their basic level
```javascript
//create event detail payload
let info = {
    detail: {position: [125,210],info:"map location"}
};
```
 - Now, let’s create our new custom ”pin” event:

```javascript
let eventPin = new CustomEvent("pin", info);

```
 - This callback function will be triggered when the event is dispatched
```javascript
let callback = function(event){
    console.log(event);
}
```
 - Finally, start listening for the ”pin” event:

```javascript
document.addEventListener("pin", callback);
```
 - The custom event is dispatched in exactly the same way as a regular event, by
calling the dispatchEvent method.
 - Whenever someone clicked a mouse button on the map area, you can dispatch the
”pin” event using the dispatchEvent method:

```javascript
document.dispatchEvent(eventPin);
```

**Event Capture And Event Bubbling**
 - The last parameter useCapture is set to false to disable event capture mode.
 - Basically when it’s set to true it means the parent element will be notified of the
event first, and only then the element that was actually clicked. If it is set to false,
”event bubbling” will be used, which means the opposite: first, the clicked element will be notified of the event, and then the event will be dispatched progressively
to all of its parents.
 - The story goes way back to implementation in the Netscape Navigator browser
and initial versions of Internet Explorer.
 - Long story short, Netscape wanted to enforce event capture. And Internet Explorer wanted to enforce event bubbling. The final consensus was to use both.
 - Since that time addEventListener function will actually listen to both capture
and bubbling. But the last parameter useCapture allows the programmer to make
a choice for which event propagation method should take precedence:
 - In modern browsers, the useCapture parameter defaults to false if it’s not specified,
but older browsers require this flag to be set manually. So in modern JavaScript
it is usually explicitly set to false but only for backwards-compatibility.

**dispatchEvent**
 - Once addEventListener function is executed, the browser will be continuously
listening for the ”start” event to occur. But the callback remains dormant until
event is actually dispatched using the dispatchEvent method:

```javascript
document.dispatchEvent(startEvent);
```
 - The dispatchEvent method actually triggers our custom ”start” event. It usually
takes one argument: the variable pointing to the actual event object created earlier.

**removeEventListener**
 - Event listeners take memory and can affect performance of your program if there
are too many listeners running at the same time. If we no longer need to listen
for the event it’s a good idea to call removeEventListener method.
 - Let’s say we started to listen for ”click” event on document:

```javascript
document.addEventListener("click", callback);
```
 - To remove this event listener we must also provide the same callback function that
was originally passed to the addEventListener method above
```javascript
document.removeEventListener("click", callback);
```
 - Anonymous functions cannot be used to remove event listeners, so the following
call will not remove the event listener:
```javascript
document.removeEventListener("click", function(){});
```

 - Whenever you use an anonymous function expression, it will occupy a new location
in memory. This means removeEventListener will not be able to locate it among
already existing callbacks.
 - The original callback function name is required because it is located at a unique
location in memory. That’s what essentially lets removeEventListener method
know exactly which listener to unbind.
 - Note removeEventListener(”click”) will not remove ”all click events”. Again,
you must specify original function name that was used to attach the event as the
second argument of removeEventListener to successfully unbind the event.

**CustomEvent Object**
 - Events can carry additional data, specifying details of the event. For example, if a
mouse is clicked, we need to know the X and Y location of the mouse pointer at
that time. If browser was resized, we need to know the size of the new client area.
 - In order to add detail to the event the CustomEvent object should be used.
 - But first, let’s create the payload object. This object must have a property named
detail which will store additional information about our custom event – indicating
that a pin was placed on a map with position and an info label:
```javascript

//create event detail payload
let info = {
    detail: {position: [125,210],info:"map location"}
};
```
 - Now, let’s create our new custom ”pin” event:
```javascript
let eventPin = new CustomEvent("pin", info);
```
 - This callback function will be triggered when the event is dispatched:

```javascript
let callback = function(event){
    console.log(event);
}
```
 - Finally, start listening for the ”pin” event:

```javascript
document.addEventListener("pin", callback);
```
 - The custom event is dispatched in exactly the same way as a regular event, by
calling the dispatchEvent method.
 - Whenever someone clicked a mouse button on the map area, you can dispatch the
”pin” event using the dispatchEvent method:

```javascript
document.dispatchEvent(eventPin);
```

**19.0.3 Event Anatomy**
  - Let’s take a look at the CustomEvent in console. Important parts were highlighted:

     ```console
     CustomEvent {isTrusted: false, detail: {…}, type: 'pin', target: document, currentTarget: document, …}
   bubbles: false
   cancelBubble: false
   cancelable: false
   composed: false
   currentTarget: null
   defaultPrevented: false
   detail: {position: Array(2), info: 'map location'}		//CustomEvent.detail
   eventPhase: 0
   isTrusted: false
   path: (2) [document, Window]     			  // propatagion path
   returnValue: true
   srcElement: document
   target: document					// target element
   timeStamp: 1317
   type: "pin"						//custom event name
   [[Prototype]]: CustomEvent
   true

     ```



**Final Words**
 - Event objects are abstract. Each event usually carries details that are relevant to
event type. So when designing your own events, think about what type of data it
should provide. This is usually specific to the purpose of your program.

**19.0.4 setTimeout**
 - You can time events using setTimeout function.
Create callback:

```javascript
 let callback = function(){
     console.log("event!")};
```
 - Execute the callback 1 second (1000 milliseconds) after setTimeout is called:
```javascript
setTimeout(callback, 1000);
```
 - Let’s try something else:

```javascript
 let callback = function(){
    console.log("do something");
}
```
 - Execute callback 1 second in the future:
```javascript
 let timer = setTimeout(callback, 1000);
```
 - Resetting the timeout using clearTimeout function will cancel the event and
prevent it from occurring in the future:

```javascript
clearTimeout(timer);
timer = null;
```

**19.0.5 setInterval**
 - The setInterval function works exactly like setTimeout, except it will continue
executing the callback function for an indefinite number of times at a time interval
specified as its second argument:
```javascript

let a = 0;
let callback = function(){
    if(a<=5){
     console.log(a);
    a++;
    }
    else{
        clearInterval(interval);
    }
  }
let interval = setInterval(callback, 1000);
```
 - *Note: To stop the events, you can use clearInterval function:*

**819.0.6 Intercepting Browser Events**
 - Many built-in events already have callback functions attached to global window
object. This means you can override them by providing your own version:

```javascript
window.onload = funciton(event){ }
window.onresize = funciton(event){ }
window.focus = funciton(event){ }
window.onmousemove = funciton(event){ }
window.onmouseover = funciton(event){ }
window.onmouseout = funciton(event){ }

```

 - The events will still take place, but the function you attach to their name will be
executed in addition to the built-in code.
 - But window object is not the only place where events can be overwritten. For
example, it is possible to attach events directly to HTML elements. And if the
selected element supports a particular event type, it will be overwritten:

```javascript
document.getElementById("id").onclick = fucntion(event){
    console.log(event);
}
```

**19.0.7 Display Mouse Position**
 - To display where the mouse pointer is located within an element, or relative to
the entire page, you can intercept the onmousemove event and output mouse
position coordinates 1attached to event argument:
```javascript
window.onmousemove = function(event){
    let mouseX = event.pageX;
    let mouseY = event.pageY;
    let localX = event.clienntX;
    let localY = event.clienntY;
    console.log(localX,mouseX,localY,mouseY);
    }
```

 - In the console we will observe similar output to:

```console
 8 218
 84  113
 21  320
```
 - The click event, and many others, can be overwritten as follows:

```javascript
  window.onclick = function(event){
        let mouseX = event.pageX;
        let mouseY = event.pageY;
        let localX = event.clienntX;
        let localY = event.clienntY;
        console.log(localX,mouseX,localY,mouseY);
        }
```


**19.0.8 Universal Mouse Event Class**
 - I can’t count how many times I had to write mouse code all over again every time
a new project required custom UI functionality. While simply intercepting common
mouse movement and click events is enough to track when buttons are clicked,
common UI projects require calculations not provided by built-in mouse events.
 - Custom modules you might want to write require knowing things like: ”Is the user
currently dragging an object with a mouse?” If you are working on a slider UI, you
will most definitely need to answer the question: ”What is the distance between
last mouse click and current mouse position?”
 - In this section we will write a reusable Mouse class that will put an end on ever
having to write mouse code again in your future JavaScript projects: just export
 - Mouse class from mouse.js file, and you’re ready to go.

```javascript
export class Mouse{
    constructor(){
        this.current = {x:0, y:0};
        this.memory = {x:0, y:0};
        this.diffrence = {x:0, y:0};
        this.dragging = false;
        document.body.addEventListener("mousedown",()=>{
            if(this.deagging == false){
                this.dragging = true;
                this.memory.x = this.current.x;
                this.memory.y = this.current.y;
                this.inverse.x = this.memory.x;
                this.enverse.y = this.memory.y;
            }
        });
        document.body.addEventListener("mouseup",()=>{
            this.dragging = false;
            this.current.x = 0;
            this.current.y = 0;
            this.memory.x = 0;
            this.memory.y = 0;
            this.diffrence.x = 0;
            this.diffrence.y = 0;
            this.inverse.x = 0;
            this.inverse.y = 0;
                    });
        document.body.addEventListener("mousemove",(event)=>{
            this.current.x=event.pageX;
            this.current.y = event.pageY;
            if(this.dragging){
                this.diffrence.x=this.current.x - this.memory.x;
                this.diffrence.y=this.current.x - this.memory.y;
                if(this.current.x<this.memory.x)
                  this.inverse.x = this.current.x;
                if(this.current.y<this.memory.y)
                  this.inverse.y = this.current.y;
                }

        });
        
    }

}
```

**Including And Using Mouse Class**
 - Just store this code in mouse.js and every time you need to work with mouse
coordinates, instantiate the Mouse class as shown in the next code sample:

```html
<html>
    <head>
        <title>Custom UI Project</title>
        <script type="module">
            import { Mouse } from "./mouse.js";
            let mouse = new Mouse();

            mouse.current.x;
            mouse.current.y;

            mouse.memory.x;
            mouse.memory.y;

            mouse.diffrence.x;
            mouse.diffrence.y;

            mouse.inverse.x;
            mouse.inverse.y;

            mouse.dragging;
        </script>
    </head>
    <body>
        
    </body>
</html>
```

**Mouse Class Explained**
 - From now on, all coordinates we might need are automatically calculated and available on the instance of the Mouse class.

 - The mouse.memory property holds the position where the mouse was clicked last
time. If user is still holding the mouse button down, which is tracked by the boolean
mouse.dragging variable, then mouse.difference property will contain distance
between the previous click and where the mouse pointer is currently located.
 - This is useful for tracking distance of a custom scrollbar, or similar slider UIs. If
the mouse is hovering over the slider handle area and user clicks the mouse button,
and the mouse button remains pressed down, then the slider should move the same
amount of distance specified in difference.x or difference.y property, depending
on whether the slider is horizontal or vertical.
 - When mouse button is released, all properties are reset to 0 again.
 - A bit more can be said about mouse.difference property when it’s negative. If
the mouse is used to ”draw” a rectangle on the screen, but the vector cast from
previous click location is negative, then mouse.inverse property will contain the
upper left corner of the rectangle.  
- If the distance vector is positive, then the upper
left corner will be naturally stored in mouse.memory.



# **Chapter 20**

**Network Requests**
 - Applications dealing with back-end code often communicate via HTTP requests.
 - In this section we will explore several different methods.
One of the first and simplest ways of initiating an HTTP request is by creating an
instance of the XMLHttpRequest object:

```javascript
const Http = new XMLHttpReauest();
```
 - This object has methods open and send. But before calling them, we need to
define an endpoint URL. In this example, let’s simply download the source code
of jQuery library from a CDN location. But it can be any other type of file:

```javascript
const url = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js";
```
 - Now we can call the URL with either ”GET” or ”POST” method:

```javascript
Http.open("GET", url);
Http.send();
```
 - To get the actual value returned from the URL endpoint, we need to listen to
”state change” event which will be executed soon as the content is returned:

```javascript
//http request response callback
Http.onreadystatechange = function(event){
    console.log(Http.respondText);
}

```

 - You can create an HTTP request to fetch almost any type of data. It doesn’t
have to be jQuery library. Usually an API you are connecting to will pack the
return value into a JSON object containing a list of items, ready for parsing by
your application and displaying in the UI view.
This is usually done in production code as shown in next example:


```javascript
const Http = new XMLHttpRequest();
const url = "object.js";

Http.onreadystatechange =  function(){
    //check for successful request status:
    if(this.readyState == 4 && this.status == 200){
       //Read content in json forma
       let json = JSON.parse(Http.responseText);

       //Extract properties from object 
       let id = json.id;
       let name = json.name;

       //Update application view with received data
       let userId = document.getElementById("id");
       if(userId) userId.innerHTML = id;

       let userName = document.getElementById("name");
       if (userName) userName.innerHTML = name;

    }

};

Http.open("GET", url);
Http.send();
```

 - Here are the contents of object.js file – it is simply an object represented by JSON
notation. Notice [] brackets:

```json
[{"id":10, "name":"pravin"}]
```
 - When an HTTP request is executed using open and send methods, the onreadystatechange event will actually be fired 4 times, each with state changing from 1 to
2 to 3 and finally to 4. We are only concerned with final stage 4, at which point
the request will be considered completed and return 200 status.
 - It is important to check for this.status == 200. Because this is the only place
where we can be sure that the event completed successfully.
Next, we retrieve contents of object.js file, which is the JSON object shown
above, in string format. But we need to convert it to an actual JavaScript object.
 - This is done via JSON.parse method.
We then store individual properties json.id and json.name in variables id and
name respectively.
 - Finally, the id and name are displayed in the UI of the app. This could be two div
containers prepared to store this data.
 - If multiple JSON objects are received, you should probably convert them to an
array (using Object.entries method) and iterate through them using .forEach,
.map or other higher-order functions.
 - In this case object.js could include multiple objects separated by comma:

```json
[
    {
        "id":7,
        "name":"dhoni"
    },
    {
        "id":10,
        "name":"sachin"
    },
    {
        "id":18,
        "name":"kohli"
    }
]
```


**What are APIs?**
 - Application Programming Interfaces (APIs) are constructs made available in programming languages to allow developers to create complex functionality more easily. They abstract more complex code away from you, providing some easier syntax to use in its place.
 - As a real-world example, think about the electricity supply in your house, apartment, or other dwellings. If you want to use an appliance in your house, you plug it into a plug socket and it works. You don't try to wire it directly into the power supply — to do so would be really inefficient and, if you are not an electrician, difficult and dangerous to attempt.


**APIs in client-side JavaScript**
 - Client-side JavaScript, in particular, has many APIs available to it — these are not part of the JavaScript language itself, rather they are built on top of the core JavaScript language, providing you with extra superpowers to use in your JavaScript code. They generally fall into two categories:

 **Browser APIs** are built into your web browser and are able to expose data from the browser and surrounding computer environment and do useful complex things with it. For example, the Web Audio API provides JavaScript constructs for manipulating audio in the browser — taking an audio track, altering its volume, applying effects to it, etc. In the background, the browser is actually using some complex lower-level code (e.g. C++ or Rust) to do the actual audio processing. But again, this complexity is abstracted away from you by the API.

**Third-party APIs** are not built into the browser by default, and you generally have to retrieve their code and information from somewhere on the Web. For example, the Twitter API allows you to do things like displaying your latest tweets on your website. It provides a special set of constructs you can use to query the Twitter service and return specific information.

**20.0.1 Callback Hell**
 - Callbacks are functions that return after an event is executed. This way we can
write in our custom code, wrap up loading animations, and do clean up.
 - For a long time, before EcmaScript 6, callbacks were extensively used as a tool to
execute asynchronous calls. As applications grew more complex, multiple callbacks
were chained up together because each call relied on completion of a previous task:

**Sailor API**
 - You can’t build a boat until you fetch some wood. You can’t sail the ocean
until the boat is built. You can’t discover an island until you can sail the ocean.
Certainly, you can’t dig for treasure without exploring an island!
 - Let’s take a look at how imaginary Sailor API could be used to achieve a series of
actions that depend on each other.

```javascript
SailorAPI("/get/wood",(result) =>{
    SailorAPI("/build/boat/",(result) =>{
        SailorAPI("/sail/ocean",(result) =>{
            SailorAPI("/explore/island",(result) =>{
                SailorAPI("/treasure/dig",(result) =>{
                   //asynchronous code 
                   //with dependencies is ugly!
                });
            });
        });
    });
});
```

 - A series of calls written this way share the problem of dependency. In addition,
a large gap of time can be created between each call, if at least one of the API
calls lags, significantly slowing down the entire process. Wasn’t asynchronous code
supposed to happen at the same time?
 - Besides, inside each callback we must manually check whether the previous request
returned successfully. This produces code that looks complicated and hard to read.
 - This ugly code is often referred to as Callback Hell. How can we escape from it?

```javascript
let password = "felixx";
let p = new Promise((resolve, reject)=>{
 if(password != "felix")
     return reject("Invalid password");
 resolve();
});
console.log(p);
```

 - The internal logic of a promise is entirely up to you.
 - If you are validating a password, as in above example, you will determine whether to
call the resolve or reject command.   
- Let’s take at resolve and reject individually
before putting together a complete promise.

**20.0.3 Promise.resolve**
 - The resolve method indicates that the promise has been successfully fulfilled and
contains the return value. For example, it can be a string:

```javascript
//resolve to "message"
let promise = Promise.resolve("message");
```

 - In the same way, the following promise is resolved to ”resolve value”, which technically can be a string, number, or even another promise:

```javascript
 let promise = Promise.resolve("resolve value")
```
 - The then method intercepts the value in the event of successful outcome as
a response to resolve method. In the next example then method is used to
intercept ”resolve value” message.

**20.0.4 .then**
 - The then method receives the resolve value:
```javascript
 let promise = Promise.resolve("resolve value");
promise.then(function(resolved){
 console.log("then:" + resolved);
});

//Output => then:resolve value
```

**20.0.5 .catch**
 - The catch method responds only to reject method. In this example, it will not
even be executed because all we did was call resolve method by itself. But it’s
possible to attach a callback to it to catch errors later:

```javascript
let promise = Promise.reject("reject value");

promise.catch(function(error){
    console.log("catch:" + error);
})
```
**20.0.6 .finally**
 - The finally method is executed regardless of whether event succeeded with resolve
method or failed with reject method.  - It is a good place for cleaning up the code or update the UI view (for example hide the loading animation):

```javascript
let promise = Promise.reject("reject value");

promise.finally(function(msg){
    console.log("finally: hide loading animation.");
})
```
**20.0.7 Promise.reject**
 - But what happens in cases when a condition isn’t met and the promise is rejected?

```javascript
let promise = Promise.reject("request rejected");

promise.catch(function(error){
    console.log("catch:" + error);
});
```
 
 - Here we paired a reject method with catch. The then method is never called on
reject action. But the finally method will be called to wrap things up:
```javascript
promise.finally(function(msg){
    console.log("finally: hide loading animation");
})
```

**20.0.8 Putting It All Together**
 - Because a promise returns a promise object, we can write everything in a single
statement:

```javascript
let promise = new Promise(function(resolve, reject){
   let condition = false;
   if(condition)
     resolve("message");
    else 
      reject("error details")
}).then(function(msg){
    console.log("promise resolved to " + msg)
    }).catch(function(error){
        console.log("promise rejected with " + error)
    }).finally(()=> console.log("finally"));
```

 - Here is another similar but slightly different pattern. If it makes the code cleaner,
you might want to separate the promise call from then and catch calls:

```javascript
let takeTheTrashOut = new Promise((resolve, reject) => {
    let trash_is_out = take_trash_out();
    if(!trash_is_out)
     reject("No");
    else 
      resolve("Yes");
});

takeTheTrashOut.then(function(fromResolve){
    console.log("Is the trash out? Answer=" + fromResolve);
}).catch(function(fromReject){
    console.log("Is the trash out? Answer=" + fromReject);
});
```
**20.0.9 Promise.all**
 - Unlike an HTTP request, promises can resolve any statement – including simple
variable values. Having said this, we can resolve multiple promises at once using
a single call to the Promise.all method as shown in the following example:

```javascript
let promise = "promise";
let threat = "threat";
let wish = Promise.resolve("I wish");

let array = [promise, threat, wish];

Promise.all(array).then(function(values){
    console.log(values);
});
```
**20.0.11 Final Words**
 - In many traditional cases, the following pattern is usually used:

```javascript
new  Promise ((resolve, reject)=>{resolve("resolved.");})
.then((msg)=>{console.log(msg)})
.catch((error)=>{console.log("error");})
.finally(()=>{console.log("finally.")});

```
**20.0.12 Axios**
 - Axios is a popular Promise-based library for talking to the database.

```console
npm  install  axios  --save
```
 - Use the command above to install it on your Node server.

 - Then, to include Axios directly into your JavaScript file:

 ```console
  import axios from 'axios';
 ```
 - Or to embed it directly into your HTML page:

```html
   <script src = "https://unpkg.com/axios/dist/axios.min.js"></script>

```

 - Now let’s say we have an endpoint /get/posts/:

 ```javascript
 const url = 'http://example.com/endpoint/get/posts';
  axios.get(url)
  .then(data => console.log(data))
  .catch(err => console.log(err));
 ```
 - As you can see Axios follows the same Promise pattern we explored in previous section. Surprisingly, there isn’t much more to it. You can use Axios to provide an elegant solution for talking to an API.

 - The complete Axios documentation is available at https://github.com/axios/axios

**20.0.13 Fetch API**
 - The built-in fetch API offers another Promise-based interface for talking to a web
server:

```javascript
let loading_animation = true;
fetch(request).then(function(response){
    var type = response.headers.get("content-type");
    if(type && type.includes("application/json"))
        return response.json();
    throw new TypeError("content is not in JSON format.");    
})
.then(function(json){ console.log("handle json here"+json); })
.catch(function(error){ console.log(error); })
.finally(function(){ loading_animation = false; });
```
**20.0.14 Fetch POST Payload**
 - When an application requires talking to a database server, you will find yourself
sending and receiving data from an endpoint. An endpoint is simply a URL
location that performs specific action. What it does is determined by the API
server. It is often part of entire API that contains multiple endpoints.
For example: /get/messages can be an endpoint that returns a JSON object
containing messages.
But requests come in two common flavors: POST and GET. And when using
POST, we can attach a payload object to communicate detail. Let’s form POST
request that grabs messages but only for user ”Felix” whose user ID is 12:


```javascript
let loading_animation = true;
fetch(request).then(function(response){
    var type = response.headers.get("content-type");
    if(type && type.includes("application/json"))
        return response.json();
    throw new TypeError("content is not in JSON format.");    
})
.then(function(json){ console.log("handle json here"+json); })
.catch(function(error){ console.log(error); })
.finally(function(){ loading_animation = false; });
```

**20.1 async / await**
 - Invoking the function now returns a promise. This is one of the traits of async functions — their return values are guaranteed to be converted to promises.
 - Promise-based code suffers from similar issues as regular callbacks. After all then,
catch and finally are still basically callback functions. Promises just make code
cleaner by segmenting the callbacks into generalized predictable results!
This means that there is still potential to end up in Promise Hell rather than
Callback Hell by stacking callbacks. Promises provide a nice attempt at making
the situation better. But code can be even more elegant than this with async.

**The Basics Of async Keyword**
 - First, let’s take a look at what exactly happens when we call two functions:
```javascript
 function x(){
    console.log("I am x");
}
function y(){
    console.log("I am y");
}
x();
y();
```
 - Function y() will be executed soon as function x() returns:

  - This is exactly what you would expect from asynchronous code, which means
code executes in a sequence after a previous command finishes executing, instead
of two functions executing simultaneously at the same time.
 - Now let’s take a look at what happens when we use async keyword.
 - First, the async keyword can be used only on functions. To do so, simply prepend
async to the function definition:
```javascript
async function a() {return 1;}
```
 - I know that we are trying to get away from the Promise pattern we saw in an earlier
section. This is true, but the async function now actually returns a promise object.
 - We’re just breaking away from the Promise Hell pattern here in pursuit of cleaner
code. But we still can call .then method on the function:

```javascript
a().then(console.log);//1
```
Remember that first argument of .then method is the resolve (success) function,
and the second argument is reject. So when we pass console.log as the first
argument, it treats it as the function that will be executed to display the result.
Essentially, the two examples below are exactly the same except the text in the
string return value:
```javascript
async function a() {return "first";}
async function b() {return Promise.resolve("second");}
```
 - They both return a promise. Even if function a() doesn’t explicitly specify it!
Let’s call both functions and then call then on the return value:

```javascript
a().then(console.log);
b().then(console.log);
//first
//second
```
 - **To actually consume the value returned when the promise fulfills, since it is returning a promise, we could use a .then() block:**

**20.1.1 await**
 - So where does await fit in? The async and await keywords are usually used in
combination with each other. The await keyword is prepended to any statement
within an async function:

```javascript
async function a() { await Math.sqrt(1);
return "first";
}

async function b(){
    return "second";
}
```

 - Note: Using await outside of async function will generate an error.
Here we added await to a simple math operation that calculates square root of
 - But the important thing here is the fact that now function b() will return first,
even though it is second in the execution order:

```javascript
a().then(console.log);
b().then(console.log);
// second
// first
```
 - Prepending await to a statement will execute it as if it were a promise. The
execution flow in the async function will pause on that statement until it is fulfilled.
 - This means that return ”first” does not return immediately like b() function.
 - This is just a simple example to demonstrate a point. 
- In reality, await is used primarily as the most elegant solution for dealing with
multiple API endpoints.
 - The most important thing about async/await is that it allows you to run synchronous code while it is still written in asynchronous form in your program. This
solves all of the problems with  -  Callback Hell, keeps your code clean while providing
maximum efficiency for executing multiple API requests.
 - The best way to demonstrate it is to put await in the context of a try / catch
statement. Let’s take a look at that in the following section.

**20.1.2 async / await with try-catch**

 - Let’s take a look at the following example where async and await are implemented
for common purpose of grabbing user info object:

```javascript
const get = async function(username, password){
    try {
        const user = await API.get.user(username, password);
        const roles = await API.get.roles(user);
        const status = await API.get.status(user);
        return user;
    } catch (error){
        console.log(error);
    }
};

const userinfo = get();
```

 - We will wait until API.get.user produces a value and stores it in user variable.
 - Until then none of the following await statements will be executed. This is ideal,
because the two await statements that follow require user object, which will become available only if user was authenticated.

 - Let’s assume if API.get.user fails, API.get.roles and API.get.status will fail
silently and a null object will be returned:


```javascript
const userinfo = get();

if(getinfo != null){
    let roles = getinfo.roles;
}else{
    //wrong username or password
}
```

**20.1.3 Final Words**
 - async / await syntax is the epitome of synchronous programming in JavaScript.
 - Functions decorated with async conveniently return a promise object.
Here we get both of both worlds. Our functions take on the asynchronous order,
but execute synchronously, just like callbacks, promises or fetch API requests.
 - We’ve finally escaped from both Callback Hell and Promise Hell without sacrificing clean code.
 - Does it mean you have to abandon using the Promise object with new operator?
Of course not. All of the techniques mentioned in this chapter can be used to
write successful applications. It depends on design choices you make.
 - The async / await keywords help us execute code synchronously, without ever having to directly use callbacks or promises, and without modifying the asynchronous
nature of code.

**20.2 Generators**
 - Generators are similar to async. They came out prior to async keyword, but they
share a similar pattern. The reason I wanted to mention them here is because it
is still common to see them in JavaScript code.
 - A generator is defined by adding the star (*) character to the function definition:
 
```javascript
function* generator(){}
```

 - You can also create it via anonymous function definition assignment:

```javascript
let generator = function*(){}
```
**20.2.1 yield**
 - Just like async works together with await, generators work together with yield
producing exactly the same effect.
```javascript
let generator = function*(){
    yield 1;
    yield 2;
    yield 3;
    yield "hello";
    return "Done.";
}
```
 - But we can’t call generator() function directly. Because every time we do, it will
be reset to first yield statement.  - 
 - Also, a single generator is designed to be used
only once. After it returns, you can not call it again.
 - For this reason, proper way to initialize new generator is by variable assignment:
 
 ``` javascript
 let gen = generator();
 ```
 - In a similar way to then method on a Promise object, generators have next
method. Whenever you call next on a generator, the next yield statement from
the generator’s function body will be executed:


```javascript
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
```

 - Generators don’t require a return value, but if there is one it will be treated as
the final value. Note that next produces an object like {value: 1, done: false},
instead of a single return value. Last statement returns done: true
 - After this, generator cannot be rewound and repeated again and should be discarded. To create a new one re-assign generator() function to a variable again.

**20.2.2 Catching Errors**
  - To catch an error using a generator you can use throw method:

```javascript
  function* generator(){
   try
   {
    yield 1;
    yield 2;
    yield 3;
   }catch(error){
    console.log("error caught", error);
}
}
let gen = generator();

console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

gen.throw(new Error('Something went worng'));
```
 - Within the generator function, make sure to branch out with try-catch statement.
 - An error should be thrown if at least one yield statement has been already executed. Of course, yield 1, yield 2 and yield 3 would be something more meaningful in a real-case scenario, such as an API call.


# **Chapter 21**

**Event Loop**

 - An event loop is something that pulls stuff out of the queue and places it onto the function execution stack whenever the function stack becomes empty.

 - As a JavaScript programmer, you don’t need to understand actual implementation
of the event loop. But understanding how the Event Loop works is important for
at least two reasons:
 - First, questions related to the event loop are often asked at job interviews.
 - The second reason is a bit more practical. By developing an awareness of how
it works, you will be able to understand the order of events as they occur, for
example, when working with callbacks and timers such as setTimeout function.
 - In the previous section we’ve seen how when functions are executed they are
placed on the Call Stack. We can even use the stack trace to track which function
was originally called to produce an error. This makes sense when working with a
deterministic set of events (one statement will proceed to be executed immediately
after the previous one is finished executing.)
 - But writing JavaScript code is often based on listening to events: timers, mouse
clicks, HTTP requests, etc. Events assume there will be a period of waiting time
until they return after accomplishing whatever task they were set to perform. But
while events are doing their work, we don’t want to halt our main program.
For this reason, whenever an event occurs, it is handed over to the Event Loop.

 - In abstract terms, the Event Loop can be thought of as just what it sounds like.
It’s a loop, with a process that keeps running in circles.

 - Whenever an event occurs, which can be thought of as a task, it is delegated to
the Event Loop, which ”goes out of its way” to pick up the task.

 - But it’s not that simple. The event loop handles events such as mouse clicks, and
timeouts. But it also needs to take care of updating the browser view:

 - The process in the event loop will continue to make rounds, sometimes spending
time processing tasks or updating the view.
 - The whole experience of how users interact with your front-end application will
often depend on how optimized your code is for the event loop.
 - To create smooth user experience,  your code should be written in such way, that
balances task processing with screen updates.
 - In modern browsers updating the view usually consists of 4 steps: checking for
requestAnimationFrame, CSS style calculations, determining layout position,
and rendering the view (actually drawing the pixels.)
 - Choosing the right time to update the browser is tricky. After all setTimeout
or setInterval were never meant to be used together with rendering the browser
view. In fact if you’ve tried to use them to animate elements, you may have
experienced choppy performance.
 - This is because setInterval hijacks the event loop, by executing the callback (in
which many place their animation code) as fast as possible. For this reason many
have moved animations that can be done in CSS to their respective CSS style
definitions, instead of performing them in JavaScript.
 - However, choppy performance can be fixed with requestAnimationFrame. What
happens is that event loop will actually sync to your monitor’s refresh rate, rather
than execute each time setInterval fires its callback function.

```javascript
console.log("Before delay");
  
function delayBySeconds(sec) {
   let start = now = Date.now()
   while(now-start < (sec*1000)) {
     now = Date.now();
   }
}
  
delayBySeconds(2);
  
// Executes after delay of 5 seconds
console.log("After delay");
```

# **Chapter 22**
 
 **Call Stack**
 - The call stack is a place to keep track of currently executing functions. As your
code executes, each call is placed on the call stack in order in which it appears in
your program. Once the function returns it is removed from the call stack.
 - Placing a function call onto the stack is called pushing and removing it from the
call stack is called popping. Same idea behind Array.push and .pop methods.
  - The console.log prints 1 to the console and returns. It is then popped
from the stack. Main function continues to run until it returns. This usually will
happen when browser is closed.

**How does this apply to writing code?**
 - The call stack is a fundamental building block of computer language design. Most
languages implement a call stack in one way or another. But how does this apply
to those who are simply writing code and not designing computer languages?

**Call Stack Example**
 - Complex tasks have priorities. Many things require to be done in a logical order.
When writing software you will often call one function from the body of another
function. You can’t mop the floor until you fill the bucket with water. You have
no reason to fill the bucket with water until you decide to clean the house first:

```javascript
console.log("Before delay");
  
function delayBySeconds(sec) {
   let start = now = Date.now()
   while(now-start < (sec*1000)) {
     now = Date.now();
   }
}
  
delayBySeconds(2);
  
// Executes after delay of 5 seconds
console.log("After delay");
```

 - Our last function mop floor throws an error. When this happens a stack trace is
shown in the console.
```console
cleanHouse();
Cleaning house.
Filling bucket with water
Mop the floor
Uncaught Error: Ran out of water!
    at mopFloor   
    at fillBucket   
    at cleanHouse 
    at <anonymous>:16:1
```

 - Error displays the trace of the call stack history, starting with the most recently
called function mop floor, in which the error occurred. When debugging this help
us trace the error all the way back to the original function clean house.
 
 - Most of the time you won’t be concerned with thinking about them when writing
code. But you might need to understand them when debugging complex large
scale software.

**22.1 Execution Context**
 - The call stack is a stack of execution contexts. When discussing one we will
inevitably run into the other.
 - You don’t need to understand execution context or the call stack in great detail
to write JavaScript code. But it might help understand the language better.

**What Is Execution Context?**
 - As your program continues to run, the statements being executed exist alongside
something called an execution context. Note that the execution context is
pointed to by this keyword in each scope. Not only function-scope either. Blockscope also carries with it a link to execution context via this keyword.
This often creates confusion, because in JavaScript the this keyword is also used
as a reference to an instance of an object in class definitions, so that we can access its member properties and members.
But things become clear if we understand that execution context is represented
by an instance of an object. It is just not used to access its properties or methods.
Instead, it establishes a link between sections of code flow across multiple scopes.

**Root Execution Context**
 - When your program opens in a browser, an instance of a window object is created
automatically. This window object becomes the root execution context, because
it’s the first object instantiated by the browser’s JavaScript engine itself. The
window object is the execution context of global scope – they refer to the same
thing. The window object is an instance of Window class.

**So how does it work?**
 - If you call a function from global scope, the this keyword inside the function’s
scope will point to window object – the context from which the function was
called. The context was carried over into the function’s scope.
 - It’s like a link was established from current execution context to the previous one.
 - The execution context is something that is carried over from one scope to another,
during code execution flow throughout lifetime of your program. You can think of
it as a tree branch that extends into another scope from the root window object.
 - In the remaining sections of this chapter we will take a look at one possible interpretation of execution context and the call stack.

**22.2 Execution Context In Code**
 - There is a difference between the logic of call stack and execution contexts and
how it manifests itself to the programmer. Obviously, being aware of the call stack
isn’t required when writing code. In JavaScript, the closest you will get to working
with execution contexts is via the this keyword.
 - Execution context is held by this keyword in each scope. The name context
suggests that it can change. This is true. The this keyword in each scope may
change or point to another new object in various situations. But where does it all begin?

**22.2.1 Window / Global Scope**
 - When the window object is created, we get a handful of things happening under the
hood. A new lexical environment is created: it contains variable environment
for that scope – a place in memory for storing your local variables. Around this
time the first ever this binding takes place.

 - A new execution context is created when main window object is
instantiated. The this keyword points to the window object.
 - In global scope this keyword points to window object-

**22.2.2 The Call Stack**
 - The call stack keeps track of function calls. If you call a function from context of
the global scope, a new entry will be placed ”on top” of the current context. The
newly created stack will inherit execution context from the previous environment.
 - To visualize this, let’s take a look at this diagram:

 - Binding of this object across execution contexts on the call stack.
A new stack is created when function is called. This new context is logically placed
”on top” of the previous object on the call stack.

**Call Stack & Execution Context Chain**

  - As more functions that depend on each other are called from within
other functions, the stack grows.

 - As you can see the context carries over to the newly created stack and remains
accessible via the this keyword. This process repeats while maintaining a chain of
execution contexts all the way up to the currently executing context:
 - Calling multiple functions from within each other’s scope will build a
tower of function calls on the call stack. Note that this would happen only one at
a time for each function if all functions were called from global scope context.
 - Note that each function carries with it its own execution context EC0 – EC3.
 - There is always one current executing context. This is the context on the very top
of the stack. While all of the previous stacks remain below, until execution returns
from the current context (function ran it’s course and returned, so JavaScript
removes the context from memory and we no longer need it...)

 - After the function is finished executing the stack is removed from the top and
the code flow returns to the remaining previous / uppermost execution context.
 - Contexts are constantly pushed and popped from the call stack.
Stacking only occurs if you call a function from another function. It won’t happen
if all functions are executed consequently from the same execution context.
 - In which case... you will have one function pushed to the stack, popped from the
stack, and then the next function will be pushed onto the empty stack again...
and so on.

**22.2.3 .call(), .bind(), .apply()**

 - These three functions can be used to call a function and choose what this keyword
should point to within the scope of that function, overriding its default behavior.

**call() Method:**

 - The call() method is a predefined JavaScript method.

 - It can be used to invoke (call) a method with an owner object as an argument (parameter).

 - With call(), an object can use a method belonging to another object.

```javascript
const person = {
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
    }
    const person1 = {
    firstName:"John",
    lastName: "Doe"
    }
    const person2 = {
    firstName:"Mary",
    lastName: "Doe"
    }
 
    // This will return "John Doe":
    let result = person.fullName.call(person1);
    console.log(result);   			//John Doe
```

**The call() Method with Arguments**

The call() method can accept arguments:
```javascript
const persons = {
    fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
}
const persons1 = {
    firstName:"John",
    lastName: "Doe"
}
let result = persons.fullName.call(persons1, "Oslo", "Norway");
console.log(result);		//John Doe,Oslo,Norway
```
**apply() method:**

 - The apply() method is similar to the call() method (previous chapter).

 - In this example the fullName method of person is applied on person1:

```javascript
  const person = {
     fullName: function() {
     return this.firstName + " " + this.lastName;
     }
 }
 const person1 = {
     firstName:"John",
     lastName: "Doe"
 }
 const person2 = {
     firstName:"Mary",
     lastName: "Doe"
 }
 let result = person.fullName.apply(person1);
 console.log(result);            //John Doe
```
**The Difference Between call() and apply()**

 - The difference is:

 - The call() method takes arguments separately.

 - The apply() method takes arguments as an array.

 - The apply() method is very handy if you want to use an array instead of an argument list.

 **The apply() Method with Arguments**

 - The apply() method accepts arguments in an array:
 ```javascript
  //The apply() Method with Arguments
 const persons = {
     fullName: function(city, country) {
     return this.firstName + " " + this.lastName + "," + city + "," + country;
     }
 }
 const persons1 = {
     firstName:"John",
     lastName: "Doe"
 }
 let result = persons.fullName.apply(persons1, ["Oslo", "Norway"]);
 console.log(result);     //John Doe,Oslo,Norway
 ```

**bind() method :**

The bind() method creates a new function, when invoked, has the this sets to a provided value.

The bind() method allows an object to borrow a method from another object without making a copy of that method. This is known as function borrowing in JavaScript.

```javascript
 const person = {
      fullName: function() {
      return this.firstName + " " + this.lastName;
      }
  }
  const person1 = {
      firstName:"John",
      lastName: "Doe"
  }
  const person2 = {
      firstName:"Mary",
      lastName: "Doe"
  }
  let result = person.fullName.bind(person1);
  console.log(result());            //John Doe
```

**Stack Overflow:**
 - The call stack has a maximum size assigned. Stack Overflow occurs when the number of function calls added to the stack increases the stack’s maximum limit (the call stack has a maximum size). A classic example to cause such a situation is Recursion. Recursion is a process in which a function calls itself until a terminating condition is found.

 - In real time example like when you pour your favorite soda into a tall glass, it will lose its carbonation and given enough amount and pace it will fizz over the rim.

 - You can think of stack overflow in a similar way. The glass is the call stack’s memory address space. The foam above rim is memory that could not be allocated.

```javascript
  function recursion(){ 
       recursion();      //a function calling itself
   }
   recursion();
```

**console output**

```console
   Uncaught RangeError: Maximum call stack size exceeded
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
       at recursion (<anonymous>:2:5)
```
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

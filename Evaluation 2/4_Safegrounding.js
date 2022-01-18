let obj = {};
let f = function(){return "This is function";}

function myFunction(func){  
    (typeof func == "function")?console.log(func()):console.log("This is not function");   
}   
myFunction(obj);     //pass object instead of function 
myFunction(f);
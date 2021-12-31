let print = function(){
    console.log("Print something in 1 second.");
    console.log(arguments);
}
let clicked = function(){
    console.log("Document was clicked");
    console.log(arguments);
}
//call anonymous named functions
setTimeout(print,1000);
clicked();
//document.addEventListener('click', clicked);


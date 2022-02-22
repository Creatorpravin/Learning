
let callback = function(){
    console.log("do something");
}
document.addEventListener("click", callback);
document.removeEventListener("click", callback);
document.removeEventListener("click", function(){});


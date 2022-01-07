let arrow = (event) =>{
    console.log("Hello, I am an arrow funciton");
    console.log(this);
}
document.addEventListener("click", arrow);

function classic(event){
    console.log("Hello, I am a classic ES5 function");
    console.log(this);
}
document.addEventListener("click",classic);
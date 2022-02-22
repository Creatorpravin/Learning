function classic(){
    let b = () => {
        console.log("Hello, I am arrow functionB()");
        console.log(this);
    }
    document.addEventListener("click",b);
}
let object = new classic();
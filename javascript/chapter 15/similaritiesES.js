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

classic_one();
classic_two();
arrow();

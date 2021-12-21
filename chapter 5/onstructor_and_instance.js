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
let pancake = new Pancake();
pancake.bake();
pancake.bake();
pancake.bake();
console.log(pancake.number);
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
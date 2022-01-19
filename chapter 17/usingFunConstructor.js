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

let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();
let tom = cat("tom",5,1,"sleeping");
tom.sleep();
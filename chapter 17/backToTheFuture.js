function cat(name, hunger, energy, state){
    let Cat = Object.create(cat.prototype);
    let Cat = {};
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



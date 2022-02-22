const prototype = {
    sleep(amount){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    },
    wakeup(amount){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    },
    eat(amount){

    },
    wander(amount){

    }

}

function cat(name, hunger, energy, state){
    let cat = {};
    cat.name = name;
    cat.hunger = hunger;
    cat.energy = energy;
    cat.state = state;

    cat.sleep = prototype.sleep;
    cat.wakeup = prototype.wakeup;
    return cat;
}

let sam = cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();

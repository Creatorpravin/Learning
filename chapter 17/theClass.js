class cat{
    constructor(name, hunger, energy, state){
        this.name = name;
        this.hunger = hunger;
        this.energy = energy;
        this.state = state;
    }
    sleep(amount){
        this.state = "sleeping";
        console.log(`${this.name} is ${this.state}`);
        this.energy += 1;
        this.hunger += 1;
    }
    wakeup(amount){
        this.state = "idle";
        console.log(`${this.name} woke up. `);
    }
    eat(amount){

    }
    wander(amount){

    }

}

let sam = new cat("sam",5,1,"sleeping");
sam.wakeup();
sam.sleep();
let tom = new cat("tom",5,1,"sleeping");
tom.wakeup();
tom.sleep();

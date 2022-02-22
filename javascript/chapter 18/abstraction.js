class Car{
    constructor(color,cost,milage){
        this.color = color;
        this.cost = cost;
        this.milage = milage;
        //this.nextYearPrice = 20000; //data is not hiding here
        }
        getdetails(){
            console.log(this.color);
            console.log(this.cost);
            console.log(this.milage);
        }
        getNextYearPrice(){
            let nextYearPrice = 20000;//hide the price of next year
            console.log(this.cost+nextYearPrice);
        }
}

let swift = new Car("red",800000,"25");
swift.getdetails();
swift.getNextYearPrice();
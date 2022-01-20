class Ingredient {
    constructor(name, type, calories){
        this.name = name;
        this.type = type;
        this.calories = calories;
        this.minutes = {
            fried: 0,
            boiled:0,
            baked:0
        }

        //export values 
        this.meat = 5;
        this.vegetable = 1;
        this.fruit = 2;
        this.egg = 3;
        this.sauce = 4;
        this.grain = 5;
        this.cheese = 6;
        this.spice = 7;
        
    }
    
}

export { Ingredient };

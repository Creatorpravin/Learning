class animal{
    constructor(name){
        this.nam = name;
    }
    eats(){
        console.log(this.nam+" eats food");
    }
}
class animal2 extends animal{
    //if we comment these method it look the same method from parent class
    eats(){
        super.eats();//call the method from parent class with same value
         console.log(this.nam+" eats fishes");
     }
}
//const{print}  = require('./print');
//print("haai");
let dog = new animal2("dogs");
dog.eats();
// const{Ingredient}  = require('./ingredient');
//import {print} from './print.js';
// const fun = require('')
//print("new");
// const val = new Ingredient();
// console.log(val.meat);
import { Ingredient } from './ingredient.js'; //import from ingredient

let val = new Ingredient();
console.log(val.meat); //import current object values from ingredient

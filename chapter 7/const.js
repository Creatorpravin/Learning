/*let a;
console.log(a);
const b;//Uncaught SyntaxError: Missing initializer in const declaration
const speed_of_light = 186000;
speed_of_light = 1; //VM1126:2 Uncaught TypeError: Assignment to constant variable.
    at <anonymous>:2:16

const A = {
    property: 1,
    method: func(){ ... }
         }
A = {something: 1 }; //Error
A.property = 2; //No error
A.method = () => {...} //No error
*/
// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};

// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson";
console.dir(car);
//const car = {type:"Fiat", model:"500", color:"white"};

//car = {type:"Volvo", model:"EX60", color:"red"};    // ERROR
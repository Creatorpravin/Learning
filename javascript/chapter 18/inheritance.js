class Bike  
{  
  constructor()  
  {  
    this.company="Honda";  
  }  
}  
class Vehicle extends Bike {  
  constructor(name,price) {  
   super();  
    this.name=name;  
    this.price=price;  
  }   
}  
var v1 = new Vehicle("Shine","70000");  
console.log(v1.company+" "+v1.name+" "+v1.price);  
const v2 = new Vehicle("Trigger", "90000") ;
console.log(v2.company+" "+v2.name+" "+v2.price);
function display(a,b){
    this.name = a;
    this.age = b;
}
display.prototype.year = "this year";
display.prototype.getDetails = function(){
    return this.name +" "+ this.age +" "+this.year;

}
let s1 = new display("Navin",26);
let s2 = new display("Kavin",26);

console.log(s1.getDetails());
console.log(s2.getDetails());
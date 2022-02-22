let sym = new Symbol('sym'); // type error
let sym = Symbol('sym');//symbol created
Symbol('sys') === Symbol('sys') //flase

let sym1 = Symbol('unique');
let bol = Symbol('dictinct');
let one = Symbol('only-one');
let obj = {property:"regular property",[sym1]:1,[bol]:2};
obj[one]=3;//add the property
console.log(obj);
//hide properties
for (let prop in obj)
console.log(prop+ ":" +obj[prop]);//property: regular property
console.log(Object.entries(obj));//(2) ["property","regular property"]
console.log(JSON.stringify(obj));//{"property":"regular property"}
console.log(Object.getOwnPropertySymbols(obj));//0: Symbol(unique)
//1: Symbol(dictinct)
//2: Symbol(only-one)
//length: 3
const seasons={
    Winter:Symbol('Winter'),
    Spring:Symbol('Spring'),
    Summer:Symbol('Summer'),
    Autumn:Symbol('Autumn')
};
let sym = Symbol.for('age');
let bol = Symbol.for('age');
let obj = {};
obj[sym]= 20; 
obj[bol]=25; //25
console.log(obj[sym]); //25 tide eachother by key 'age'

"use strict";
var x = new Set();
var array = [
    {id: 1, name: 'Stephen covey'},
    {id: 2, name: 'Robin Sharma' }, 
    {id: 3, name: 'Tolstoy'}, 
    {id: 3, name: 'Tolstoy'}, 
    {id: 5, name: 'James clear'}
];
var filteredArray = array.filter(value => {
  var duplicate1 = x.has(value.id);
  x.add(value.id);
  var duplicate2 = x.has(value.name);
  x.add(value.name);
  return !duplicate1 && !duplicate2;
});
console.log(filteredArray);
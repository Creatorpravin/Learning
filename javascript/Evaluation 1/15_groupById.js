"use strict";
var peoples=[
    {id: 1, name: 'edison' }, 
    {id: 2, name: 'Annand' }, 
    {id: 3, name: 'Vasnath'}
];
var groupByid = peoples.reduce((acc, intex) => {
    acc[intex.id] = acc[intex.id] + 1 || 1;
    return acc;
  }, {} );
console.log(groupByid); 
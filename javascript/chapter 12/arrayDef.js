var fruit = [
    {name:"Apple", count:13,},
    {name:"Pear", count:12,},
    {name:"Banana", count:12,},
    {name:"Strawberry", count:11,},
    {name:"Cherry", count:11,},
    {name:"Blackberry", count:10,},
    {name:"Pineapple", count:10,}

];
//create our own criteria function:
let mySort=(a,b)=>a.count - b.count;
//Perform stable ES10 sort:
let sorted = fruit.sort(mySort);
console.log(sorted);
//console.log(fruit)

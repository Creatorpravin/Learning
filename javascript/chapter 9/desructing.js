[a,b,...rest] = [30,40,50,60,70];
console.log(a,b);
console.log(...rest);
//Destructuring to oranges from oranges property in a object
/*let {oranges} = {oranges :1 };
console.log(oranges);*/
let fruitBasket={apples:1,oranges:2,mangoes:3};
let {apples, mangoes} = fruitBasket;
console.log(apples+mangoes);



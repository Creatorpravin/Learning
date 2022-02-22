/*function sum(...args){
    let sum = 0;
    for (let temp of args)
    sum +=temp;
    return sum;
}
let add = sum(1,2,3,4,5);
console.log(add);*/
/*function sum(...args){
    return args.reduce((k, j)=>k+j,0)
}
let add=sum(1,2,3,4,5,20);
console.log(add);*/
let sum = (...args)=>args.reduce((k,j)=>k+j,0);
sum(1,2,3,4,5,20);
console.log(sum);

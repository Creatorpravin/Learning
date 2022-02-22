let x ={p:1};
let y=x;
x.p=2;
console.log(y.p);

let a ={p:5};
let b=a;
let c=b;
let d=c;
let f=d;
a.p=10;
console.log(f.p);
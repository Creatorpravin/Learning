console.log(this===window);
var c="c";//latches on to window("this" is global scope)
let d="d";//exists separately from "this"
console.log(c);
console.log(this.c);
console.log(window.c);

console.log(d);//c
console.log(this.d);//undefined
console.log(window.d);//undefined


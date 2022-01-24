async function a() {return "first";}
async function b() {return Promise.resolve("second");}

a().then(console.log);
b().then(console.log);







// function x(){
//     console.log("I am x");
// }
// function y(){
//     console.log("I am y");
// }
// x();
// y();
function* generator(){
   try
   {
    yield 1;
    yield 2;
    yield 3;
   }catch(error){
    console.log("error caught", error);
}
}
let gen = generator();

console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

gen.throw(new Error('Something went worng'));

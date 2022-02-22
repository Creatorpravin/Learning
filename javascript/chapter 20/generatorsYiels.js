let generator = function*(){
    yield 1;
    yield 2;
    yield 3;
    yield "hello";
    return "Done.";
}
let gen = generator();

console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());


function* generator(){
    yield 1;
    yield 2;
    yield 3;
}
for(let value of generator())
  console.log(value)

 /* this is same as above one
 let gen = generator();

  console.log(gen.next().value);
  console.log(gen.next().value);
  console.log(gen.next().value);*/
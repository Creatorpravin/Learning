function print(a,b,c, ...args)
{
    console.log(a);
    console.log(b);
    console.log(c);
    console.log(args);
}
print(...[1,2,3],4,5);
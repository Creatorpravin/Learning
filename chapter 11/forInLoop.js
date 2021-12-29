let object = {a:1,b:2,c:5,method:()=>{}};
for (let value in object)
   console.log(value, object[value]);
   
/*Console
a 1
b 2
c 5
method [Function: method]*/
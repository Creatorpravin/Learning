var students = [{
    name: 'Nick',
    achievements: 158
   }, {
    name: 'Jordan',
    achievements: 175
  }, {
    name: 'Ramon',
    achievements: 55
    }];
let a = [],b=[];
let d = {}
students.forEach(function(obj){
    d[obj.name] = obj.achievements;
//     a.push(obj.name);
//     b.push(obj.achievements);
 })
 console.log(d);
// let k = a[0];

// d[k] = b[0];
// console.log(d);



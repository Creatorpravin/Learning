const radius = [1,2,3,4];
const output = [];
function area(radius){
    return Math.PI * radius * radius;
}

radius.forEach(value=>output.push(area(value)));
console.log(output);
// let calculate = function (radius, logic){
//     const output = [];
//     for (i=0;i < radius.length;i++){
//         output.push(logic(radius[i]));
//     }
//     return output;
    
// }
// console.log(calculate(radius, area));//create iteration of array 
// console.log(radius.map(area));//use inbuilt map funciton


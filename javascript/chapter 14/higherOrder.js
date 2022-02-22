const radius = [1,2,3,4];
const area = function (radius){
    return Math.PI * radius * radius;
}

let calculate = function (radius, logic){
    const output = [];
    for (i=0;i < radius.length;i++){
        output.push(logic(radius[i]));
    }
    return output;
    
}
console.log(calculate(radius, area));//create iteration of array 
console.log(radius.map(area));//use inbuilt map funciton


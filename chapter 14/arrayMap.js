let number = [24,24,2,4,56,85,63];
let copy = [];
function addOne(value){return value + 1;}
function maap(num, f){
    for (let index = 0; index < num.length; index++) {
        const original = num[index];
        let modify = f(original);
        copy[index] = modify;
        
    }
    return copy;
}
console.log(maap(number, addOne));
function objcmp(a,b){
    //Copy properties into a and b
    let A = Object.getOwnPropertyNames(a);
    let B = Object.getOwnPropertyNames(b);
     
    //Return early if number of properties is not equal
    if(A.length != B.length)
    return false;

    //Return early if number of properties on both objects
    for(let i = 0; i<A.length;i++)
    {
        let propName = A[i];
        //properties must equal by value *and type
        if(a[propName] !== b[propName])
        return false;
    }
    //objects are equal
    return true

}

let a = {prop:[1,2], obj:{}};
let b = {prop:[1,2], obj:{}};
const res = objcmp(a,b);//false
console.log(res);

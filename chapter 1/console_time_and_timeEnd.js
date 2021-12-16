console.time();
let arr = new Array(1000);
for (let i = 0; i < arr.length;i++){
    arr[i]=new Object();
    console.log(i,Object);
}
console.timeEnd();
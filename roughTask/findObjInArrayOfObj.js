let a = [{type:45,id:1},{type:46,id:2}]

let obj = a.find(o => o.type === 45);

console.log(obj);
a.forEach(function(obj){
    if(obj.type === 46){
        console.log(obj)
    }
})
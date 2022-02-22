new  Promise ((resolve, reject)=>{resolve("resolved.");})
.then((msg)=>{console.log(msg)})
.catch((error)=>{console.log("error");})
.finally(()=>{console.log("finally.")});

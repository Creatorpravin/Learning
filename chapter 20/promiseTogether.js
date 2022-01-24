let promise = new Promise(function(resolve, reject){
   let condition = false;
   if(condition)
     resolve("message");
    else 
      reject("error details")
}).then(function(msg){
    console.log("promise resolved to " + msg)
    }).catch(function(error){
        console.log("promise rejected with " + error)
    }).finally(()=> console.log("finally"));
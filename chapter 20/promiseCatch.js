let promise = Promise.reject("reject value");

promise.catch(function(error){
    console.log("catch:" + error);
})
let promise = Promise.reject("reject value");

promise.finally(function(msg){
    console.log("finally: hide loading animation.");
})

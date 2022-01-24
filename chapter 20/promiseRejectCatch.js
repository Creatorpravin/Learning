let promise = Promise.reject("request rejected");

promise.catch(function(error){
    console.log("catch:" + error);
});

promise.finally(function(msg){
    console.log("finally: hide loading animation");
})

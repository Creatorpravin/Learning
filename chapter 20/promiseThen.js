let promise = Promise.resolve("resolve value");
promise.then(function(resolve){
 console.log("then:" + resolve);
});


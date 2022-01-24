let promise = "promise";
let threat = "threat";
let wish = Promise.resolve("I wish");

let array = [promise, threat, wish];

Promise.all(array).then(function(values){
    console.log(values);
});


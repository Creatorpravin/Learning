// let callback = function(){
//     console.log("event!")};

// setTimeout(callback, 1000);

let callback = function(){
    console.log("do something");
}

let timer = setTimeout(callback, 1000);

clearTimeout(timer);
timer = null;
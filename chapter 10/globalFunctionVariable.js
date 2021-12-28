let print,set, increase, decrease;
function manager(){
    console.log("manager();");
    let number = 15;
    print = function(){console.log(number)}
    set = function(value) {number = value}
    increase = function() {number++}
    decrease = function() {number--}
}


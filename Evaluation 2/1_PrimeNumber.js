
"use strict"
function primeNumber(value){
 if(typeof value === "number" && value > 2 ){
      for (let counter = 0; counter <= value; counter++) {

    var notPrime = false;
    for (var i = 2; i <= counter; i++) {
        if (counter%i===0 && i!==counter) {
            notPrime = true;
        }
    }
    if(counter >= 2)
    if (notPrime === false) {
        
                console.log(counter);
    }
}

}else
    console.log("Enter the valid value");

}

primeNumber(200);

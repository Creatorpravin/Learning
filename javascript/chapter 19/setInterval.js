let a = 0;
let callback = function(){
    if(a<=5){
     console.log(a);
    a++;
    }
    else{
        clearInterval(interval);
    }
  }
let interval = setInterval(callback, 1000);

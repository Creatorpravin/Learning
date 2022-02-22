
// for(var i = 0; i <= 10; i++) {
//         let k = i;
//         setTimeout(function() {
//         console.log(k);
//         }, 1000 * (k + 1));
//         }
for(var i = 0; i < 10; i++) {
        Hello(function() {
        console.log(i);
        }, 10);
        }

function Hello(fun,num){
    fun();
    
}

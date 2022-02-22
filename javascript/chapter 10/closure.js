function global(){
    function inner(){
        console.log("inner");
    }
    inner();
}
global();

function fun(text, number, array, object, func, misc){
    console.log(text);
    console.log(number);
    console.log(array);
    console.log(object);
    console.log(func);
    console.log(misc);
    //Call the function by its parameter name
    func();
}

function volleyball(){return "volleyball"};
fun("text",125,[1,2,3],{count:1},volleyball, volleyball());

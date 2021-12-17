function strict_function(){
    'use strict';
    function inner(){console.log("me too");}
    return 'I am in strict mode.'+inner();
}
strict_function();
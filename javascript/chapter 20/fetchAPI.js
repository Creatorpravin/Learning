
let loading_animation = true;
fetch(request).then(function(response){
    var type = response.headers.get("content-type");
    if(type && type.includes("application/json"))
        return response.json();
    throw new TypeError("content is not in JSON format.");    
})
.then(function(json){ console.log("handle json here"+json); })
.catch(function(error){ console.log(error); })
.finally(function(){ loading_animation = false; });
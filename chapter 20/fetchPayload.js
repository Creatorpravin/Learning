
const url = "http://example.com/endpoint/get/messages";
const data = {name: "felix", id:12};
const params = {
    headers: {
        "content-type": "application/json"
    },
    body: data,
    method: "POST"
}
const callback = function(response){
    var type = response.headers.get("content-type");
    if(type && type.includes("application/json"))
        return response.json();
    throw new TypeError("content is not in JSON format.");        
}
fetch(url,params).then(callback)
.then(function(json){ console.log("handle json here"+json); })
.catch(function(error){ console.log(error); })
.finally(function(){ loading_animation = false; });
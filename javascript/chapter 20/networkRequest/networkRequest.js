const Http = new XMLHttpRequest();
const url = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js";
Http.open("GET", url);
Http.send();
//http request response callback
Http.onreadystatechange = function(event){
    console.log(Http.respondText);
}


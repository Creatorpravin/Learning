const Http = new XMLHttpRequest();
const url = "object.js";

Http.onreadystatechange =  function(){
    //check for successful request status:
    if(this.readyState == 4 && this.status == 200){
       //Read content in json forma
       let json = JSON.parse(Http.responseText);

       //Extract properties from object 
       let id = json.id;
       let name = json.name;

       //Update application view with received data
       let userId = document.getElementById("id");
       if(userId) userId.innerHTML = id;

       let userName = document.getElementById("name");
       if (userName) userName.innerHTML = name;

    }

};

Http.open("GET", url);
Http.send();
let div = document.createElement("div");
//set ID of the element
div.setAttribute("id","element");
//set class attribute of the element
div.setAttribute("class","box");

div.style.position = "absolute";
div.style.display = "block";
div.style.width = "100px";//px is requried
div.style.height = "100px";//px is requried
div.style.top = 0; //px is not required
div.style.left = 0;//px is not required
div.style.zIndex = 1000; // z-index of > zIndex
div.style.borderStyle = "solid";
div.style.borderColor = "gray";
div.style.borderWidth = "1px";
div.style.backgroundColor = "white";
div.style.color = "black"; 
//add element to DOM by insert into <body>
document.body.appendChild(div);
//Insert element into another element by id:
document.getElementById("id-1").appendChild(div);
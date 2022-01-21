window.onmousemove = function(event){
    let mouseX = event.pageX;
    let mouseY = event.pageY;
    let localX = event.clienntX;
    let localY = event.clienntY;
    console.log(localX,mouseX,localY,mouseY);
    }
 window.onclick = function(event){
        let mouseX = event.pageX;
        let mouseY = event.pageY;
        let localX = event.clienntX;
        let localY = event.clienntY;
        console.log(localX,mouseX,localY,mouseY);
        }
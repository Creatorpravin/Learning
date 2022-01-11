//create a generic HTML element
export let element =(id,type,l,t,w,h,z,r,b,value,color)=>{
    //default-used to replace missing arguments
    const position=0;
    const size=10;
    const Z=1;
    //create a <div> element dynamically
    let div=document.createElement("div");
    //inner html
    div.innerHTML=value;
    //set ID of the element
    div.setAttribute("id",id);
    //set abosolute behavior
    div.style.position=type;
    div.style.display="block";
    div.style.color = color;
    if(r)//if right is provided,reposition element
        div.style.right=r?r:position+"px";
    else
        div.style.left=l?l:position+"px";

    if(b)//if bottom is provided,reposition element
        div.style.bottom=b?b:position+"px";
    else
        div.style.left=t?t:position+"px";

    div.style.width=w?w:size+"px";
    div.style.height=h?h:size+"px";
    div.style.zIndex=z?z:Z;
    
    //return the element object we just created
    return div;
};
document.body.appendChild(element("id1","button",10,10,200,10,10,10,10,"created by function","blue"));

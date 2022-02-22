let element = (id,type,l,t,w,h,z,r,b)=>{
const position = 0;
const size = 10;
const z = 1;
// let a = element("id-1","static",0,0,100,25,"unset");
// let b = element("id-2","relative",0,0,50,25,1);
// let c = element("id-3","absolute",10,10,50,25,20);
let div = document.createElement("div");
div.setAttribute("id",id);
div.style.position = type;
div.style.display = "block";

if(right)
   div.style.right = r ? r : position + "px";
else  
   div.style.left = l ? l : position + "px";

if(bottom)
  div.style.bottom = b ? b : position + "px";
else  
  div.style.left = t ? t : position + "px";

div.style.width = w ? w : size + "px";
div.style.height = h ? h : size + "px";
div.style.zIndex = z ? z : Z;

return div;
};
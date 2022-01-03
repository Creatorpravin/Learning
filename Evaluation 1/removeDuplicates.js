let animals = [1,2,9,4,5,8,3,5,1,4,5];  
let unique = [];  
animals.forEach((item) => {  
   if(!unique.includes(item)){  
      unique.push(item);  
   }  
});  
console.log(unique); 
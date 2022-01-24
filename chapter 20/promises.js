let password = "felix";
let p = new Promise((resolve, reject)=>{
 if(password != "felix")
     return reject("Invalid password");
 resolve("password  matches");
});
console.log(p);


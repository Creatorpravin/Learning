let takeTheTrashOut = new Promise((resolve, reject) => {
    let trash_is_out = take_trash_out();
    if(!trash_is_out)
     reject("No");
    else 
      resolve("Yes");
});

takeTheTrashOut.then(function(fromResolve){
    console.log("Is the trash out? Answer=" + fromResolve);
}).catch(function(fromReject){
    console.log("Is the trash out? Answer=" + fromReject);
});
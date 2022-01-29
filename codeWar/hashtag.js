 function generateHashtag (str) {
    if(str.length>1){ 
    let arg = str
      .trim()
      .split(" ");
  
    let arr = arg.map((v, i, arr) =>
      v ? v.slice(0, 1).toUpperCase() + v.slice(1) : v
    );
    let a = "#" + arr.join("");
    return (a.length<=140 ? false : a) 
    }else{
        return false
    }
  };

  console.log(generateHashtag("hello world"));
  console.log(generateHashtag("   "));

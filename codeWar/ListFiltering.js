
function filter_list(l) {
    return l.filter((v) => typeof v == "number");
  }
  
  console.log((filter_list([1,2,'a','b'])))
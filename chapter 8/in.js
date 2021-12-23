"c" in {"a": 1, "b":2,"c":3};//true
1 in {"a": 1, "b":2,"c":3};//false
"c" in["a","b","c"];//false
0 in["a","b","c"];//true
1 in["a","b","c"];//true
2 in["a","b","c"];//true
3 in["a","b","c"];//false
"length" in [];  //true
"length" in["a","b","c"];//true
"length" in {};//false
"length" in {"length":1}//true
"constructor" in Object;//true
"prototype" in Object;//true
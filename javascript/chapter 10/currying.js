let planets = function(a){
    return function(b){
    return 'favorite planets are ' + a + ' and ' +b;
    }

};
let favoritePlanet = planets('jupiter');
let fav1 = favoritePlanet('Earth');
console.log(fav1);
let fav2 = favoritePlanet('Mars');
console.log(fav2);
let fav3 = favoritePlanet('Saturn');
console.log(fav3);
/* Also it will be invoked immediately
let p = planets('Earth')('Mars');
console.log(p);*/





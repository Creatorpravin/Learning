function season(name){
    this.name = name;
    this.getName = function(){
        return this.name;
    }
}

let winter = new season("winter");
let summer = new season("summer");
let spring = new season("spring");
let autumn = new season("autumn");
console.log(winter.getName());
console.log(summer.getName());
console.log(spring.getName());
console.log(autumn.getName());

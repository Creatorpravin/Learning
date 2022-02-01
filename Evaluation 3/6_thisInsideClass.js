class student{
    constructor(name,location){
        this.name=name;
        this.location=location;
    }
    getdetails(){
        console.log('Hi, i am '+this.name+' from '+this.location+'.');
    }
}

const std1 = new student("Pravin","Chennai")
std1.getdetails();

const std2 = new student("Dinesh","Covai");
std2.getdetails();
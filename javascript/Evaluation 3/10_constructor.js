"use strict"
class vehicle{
    constructor(vname){
        this.vname = vname;
    }
    getdetails(){
        console.log("The vehicle is "+this.vname);
    }
}

const veh1 = new vehicle("bus");
veh1.getdetails();

const veh2 = new vehicle("car");
veh2.getdetails();
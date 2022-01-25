function mopFloor(){
    console.log("Mop the floor");
    throw new Error("Ran out of water!");
}

function fillBucket(what){
    console.log("Filling bucket with " + what);
    mopFloor();
}

function cleanHouse(){
    console.log("Cleaning house.");
    fillBucket(("water"));
}

cleanHouse();
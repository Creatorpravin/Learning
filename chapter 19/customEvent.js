//create event detail payload
let info = {
    detail: {position: [125,210],info:"map location"}
};

let eventPin = new CustomEvent("pin", info);
let callback = function(event){
    console.log(event);
}

document.addEventListener("pin", callback);

document.dispatchEvent(eventPin);



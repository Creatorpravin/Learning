const cat = {
    name: "Tom",
    state: "idle",
    hunger: 1,
}
const kitten = Object.create(cat);
kitten.name = "Loki";
kitten.state = "sleeping";
console.log(kitten);
console.log(kitten.hunger);

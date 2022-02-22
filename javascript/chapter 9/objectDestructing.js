let deep = {
    basket:{
        fruit:{
            name: "orange",
            shape: "round",
            weight: 0.2
        }
    }
}
let {name, shape, weight} = deep.basket.fruit;
console.log(name);
console.log(shape);
console.log(weight);




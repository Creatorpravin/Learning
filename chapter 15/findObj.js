const orders=[
    {id:1, item:"maggi"},
    {id:2, item:"ac"},
    {id:3, item:"ac"}
];
let result = orders.find((order)=>(order.item=="acss"));
result =typeof result != "undefined" ? result : "It's invalid";
console.log(result);
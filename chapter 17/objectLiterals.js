let literals = {
    prop:123,
    meth: function(){}
};
literals.__proto__;  //object{}
literals.__proto__.constructor; //ƒ Object() { [native code] }
literals.constructor; //ƒ Object() { [native code] }

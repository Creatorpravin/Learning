"use strict";
//Instance method in class
class InstanceMethod {
    instanceMethod() {
    return 'instance method has been called.';
  }
}
let obj = new InstanceMethod();
console.log(obj.instanceMethod()); //"instance method has been called."
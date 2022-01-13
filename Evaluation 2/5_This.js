const x = 25;
function y(){
    var a = 35;
    console.log(a);
    console.log(this.a);
}
y();
console.log(this);
const test = {
          prop: 42,
          func: function() {
          return this.prop;
      },

    };
  console.log(test.func());
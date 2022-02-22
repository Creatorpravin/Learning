String.prototype.camelCase = function() {
    let arg = this.toString()
      .trim()
      .split(" ");
      console.log(arg);
    let arr = arg.map((v, i, arr) =>
      v ? v.slice(0, 1).toUpperCase() + v.slice(1) : v
    );
    return arr.join("");
  };

  console.log("hello case".camelCase());
  
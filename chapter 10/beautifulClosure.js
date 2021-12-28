let get = null; //placeholder for global getter function
function closure(){
    this.inc = 0
    get = () => this.inc;//getter
    function increase() {this.inc++;
    console.log(this.inc);}
    function decrease() {this.inc--;
        console.log(this.inc);}
    function set(v) {this.inc = v;
        console.log(this.inc);}
    function reset() {this.inc=0;
        console.log(this.inc);}
    function del(){
        delete this.inc;//become undefined
        this.inc = null;
        console.log("this.inc deleted");

    }
    function readd(){
        if(!this.inc)
         this.inc = "re-added";
    }
    return [increase,decrease,set,reset,del,readd];
}
let f = closure();
let inc = f[0];
let dec = f[1];
let set = f[2];
let res = f[3];
let del = f[4];
let add = f[5];
inc();//1
inc();//2
inc();//3
dec();//2
get();//2
set(7);//7
get();//7
res(0);//0
get();//0

class Mouse{
    constructor(){
        this.current = {x:0, y:0};
        this.memory = {x:0, y:0};
        this.diffrence = {x:0, y:0};
        this.dragging = false;
        document.body.addEventListener("mousedown",()=>{
            if(this.deagging == false){
                this.dragging = true;
                this.memory.x = this.current.x;
                this.memory.y = this.current.y;
                this.inverse.x = this.memory.x;
                this.enverse.y = this.memory.y;
            }
        });
        document.body.addEventListener("mouseup",()=>{
            this.dragging = false;
            this.current.x = 0;
            this.current.y = 0;
            this.memory.x = 0;
            this.memory.y = 0;
            this.diffrence.x = 0;
            this.diffrence.y = 0;
            this.inverse.x = 0;
            this.inverse.y = 0;
        });
        document.body.addEventListener("mousemove",(event)=>{
            this.current.x=event.pageX;
            this.current.y = event.pageY;
            if(this.dragging){
                this.diffrence.x=this.current.x - this.memory.x;
                this.diffrence.y=this.curre this.memory.y;
                if(this.current.x<this.memory.x)
                  this.inverse.x = this.current.x;
                if(this.current.y<this.memory.y)
                  this.inverse.y = this.current.y;
                }

        });
        
    }

}

export { Mouse };
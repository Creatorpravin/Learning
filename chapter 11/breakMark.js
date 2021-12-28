let c = 0;
mark: for(let i=0; i<5;i++)
    inner: for(let j=0; j<5;j++){
        c++;
        if(i==2)
        break mark;
    }
    console.log(c);//11

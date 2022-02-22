async function a() { await Math.sqrt(1);
return "first";
}

async function b(){
    return "second";
}

a().then(console.log);
b().then(console.log);
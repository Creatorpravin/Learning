function sendEmail(from,sub,message){
    let msg = `"${sub}">"${message}" received from "${from}"`;
    let send =function () {console.log(msg)}
    return send;
}
let ref = sendEmail('Pravin','re:subject','Good news');
ref();
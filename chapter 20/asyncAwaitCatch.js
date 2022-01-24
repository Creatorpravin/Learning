const get = async function(username, password){
    try {
        const user = await API.get.user(username, password);
        const roles = await API.get.roles(user);
        const status = await API.get.status(user);
        return user;
    } catch (error){
        console.log(error);
    }
};

const userinfo = get();

if(getinfo != null){
    let roles = getinfo.roles;
}else{
    //wrong username or password
}


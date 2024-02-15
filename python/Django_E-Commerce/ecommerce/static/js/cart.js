var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(`Product ID: ${productId}, Action: ${action}`)
        console.log("USER", user)
        
        if (user === 'AnonymousUser'){
            alert('You must be logged in to perform this action.')
        }else{
            console.log("User is logged in, sending data...")
        }
    })
    
}
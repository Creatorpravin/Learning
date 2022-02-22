
SailorAPI("/get/wood",(result) =>{
    SailorAPI("/build/boat/",(result) =>{
        SailorAPI("/sail/ocean",(result) =>{
            SailorAPI("/explore/island",(result) =>{
                SailorAPI("/treasure/dig",(result) =>{
                   //asynchronous code 
                   //with dependencies is ugly!
                });
            });
        });
    });
});

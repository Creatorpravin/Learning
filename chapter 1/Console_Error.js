let fuel = 99;
function launch_rocket(){
    function warning_mgs(){
        console.error("Not enough fuel.");  
    }

if(fuel >= 100)
{
    //looks everything is fine
 }
  else
        warning_mgs(); 
}
launch_rocket();
class A  
  {  
     display()  
    {  
      console.log("A is invoked");  
    }  
  }  
class B extends A  
  {  
    display()  
    {  
      super.display();//invoke both method 
      console.log("B is invoked");  
    }  
  }  
  
// var a=[new A(), new B()]  
// a.forEach(function(msg)  
// {  
// msg.display();  
// });  
var b = new B();
b.display();


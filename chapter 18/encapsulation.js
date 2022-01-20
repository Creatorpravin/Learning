//Allows us to control data and variable
//Allows to handle an object read/write
class Student  
  {  
    constructor()  
    {  
       var name;  
       var marks;  
    }  
        getName()  
        {  
          return this.name;  
        }  
      setName(name)  
      {  
        this.name=name;  
      }  
        
      getMarks()  
      {  
        return this.marks;  
      }  
    setMarks(marks)  
    {  
        if(marks<0||marks>100)  
        {  
          console.log("Invalid Marks");  
        }  
      else  
        {  
          this.marks=marks;  
        }  
    }  
    }  
    var stud=new Student();  
     stud.setName("Praveen");  
     stud.setMarks(90);//alert() invokes  
     console.log(stud.getName()+" "+stud.getMarks());  

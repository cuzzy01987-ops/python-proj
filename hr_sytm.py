
total = 0

print("*" * 50)
with open(r"C:\Users\User\Desktop\BYU_Classes\CSE110\CSE110\main_project\w6\HR_system.txt") as hr_file:
    next(hr_file)
    print("These are the monthly payroll for the stuffs")
    print("*" * 50)  
    for line in hr_file:
        

        
        parts = line.split()
        name = parts[0]
        ID = parts[1]
        job_title = parts[2]
        salary = int(parts[3])
        
        
        m_pay = salary / 12 
        

        if job_title.lower() == "engineer":
            m_pay += 1000
            
        if job_title.lower() == "ceo":
            m_pay += 2000
            
        print(f"{name} (ID:){ID}- {job_title} ${m_pay: 2f}") 
        
print("*" * 50)
total += salary
print(f"Total salary Distributed is ${total}")

print("*" * 50)




    
 

            
       
            
      
          
            
     
        
        
        
        
        
        
        
        
        
            
         
        
        
            
        
                                         
        
        
   
    
    
        
        
    
            
            
       
            
            
        
        
        

    
    
    
 
        
        
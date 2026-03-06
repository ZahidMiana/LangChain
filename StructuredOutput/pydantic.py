from pydantic import BaseModel

class Student(BaseModel):
    name: str
    

new_student = Student(name="Zahid")

student = Student(**new_student)
print(student)



#Next Output Parser
#String Output Parser
#Structured Output Parser
#JSON Parser
#Pydantic Output Parser
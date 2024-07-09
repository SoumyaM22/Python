##1. Convert the following dictionary into JSON format.
import json
#Student_data = {"name": "David", "age": 13, "marks": 87}
#print(type(Student_data))
#converting dictionary into JSON
#data = json.dumps(Student_data)
#print(data)
#print(type(data))



##2. Access the value of age from the given data.
#Student_data = """{"name": "David", "age":13, "marks": 87}""" #json string
##using loads method we converted json string to python object
#data = json.loads(Student_data)
#print(data["age"])

##3. Pretty print the follwing JSON data.
## Pretty print - it means we need use indent & separators
#Student_data = {"name": "David", "age": 13, "marks": 87}
#data = json.dumps(Student_data,indent=4,separators=(",","="))
##dumps() used to serialize Python object into JSON
#print(data)

##4.Sort the following JSON Keys & write them into a file
#Student_data = {"name": "David", "age": 13, "marks": 87}
##open file in writing mode
#f = open("demo.json","w")
#data =json.dumps(Student_data,indent=4,separators=(",","="),sort_keys=True)
#f.write(data)

##5. Access the nested key "marks" from the following nested data
student_data="""{    "student": 
                        {"grade": 
                            {"name": "David","marks":87}
                        }    
            }"""

data = json.loads(student_data)
print(data["student"]["grade"]["marks"])

class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor called")
        self.last_name=last_name
        self.eye_color=eye_color
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys

    def show_info(self):
         print("Last Name - "+self.last_name)
         print("Eye Color - "+self.eye_color)  
         print("Number of toys - "+str(self.number_of_toys))
billy=Parent("manisha","black")
#billy.show_info()
miley = Child("agarwal","blue",5)
miley.show_info()

      

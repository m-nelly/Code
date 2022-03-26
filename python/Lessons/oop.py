def classes(): 
    # think of a class as a blueprint and an object as the constructed counterpart of that blueprint.
    # the class can be used multiple times to build the same thing, but each iteration is a unique object. 

    class FirstClass:

        # __init__ is a special constructor method that performs actions during initialization.
        def __init__(self, author, title): # the self attribute points this instance of the class.
            self.author = author
            self.title = title
        
        def printresult(self): # the self attribute allows instancing using objects.
            print(self.author, ": ", self.title)

    # let's create a class to use with our next lesson. 
    # we want to create a set of containers that each track their weight as items are added or subtracted. 
    # for the sake of simplicity, we will assume all objects to be weighted equally and at 1 unit of weight. 

    class Example: # name and define the class.
        def __init__(self, capacity, weight): # initialize the class and create properties. 
            self.weight = 0 # set a default value for weight.  
            self.capacity = capacity # set a value passed as a parameter for capacity.
        
        def addWeight(self): # function or method to add weight to our objects.
            w = input('How much weight do we add?')
            self.weight += w
        
        def removeWeight(self): # function to remove weight from our objects. 
            w = input('How much weight do we remove?')
            self.weight -= w

        def checkCapacity(self): # function to test weight against capacity
            if self.weight < self.capacity: 
                print('Container is under capacity!')
            elif self.weight == self.capacity:
                print('Container is at capacity!')
            else:
                x = self.weight - self.capacity # checks to see how over weight this container is.
                print('Container is over capacity! Remove ' + str(x) + ' from this container!') 

    return()

def objects():
    # to begin working with objects, we will use our previous example class.
    class Example: # name and define the class.
        def __init__(self, capacity, weight = 0): # initialize the class and create properties. 
            self.weight = weight # set a default value for weight.  
            self.capacity = capacity # set a value passed as a parameter for capacity.
        
        def addWeight(self): # function or method to add weight to our objects.
            w = int(input('How much weight do we add? : '))
            self.weight += w
        
        def removeWeight(self): # function to remove weight from our objects. 
            w = int(input('How much weight do we remove? : '))
            self.weight -= w

        def checkCapacity(self): # function to test weight against capacity
            if self.weight < self.capacity: 
                print('Container is under capacity!')
            elif self.weight == self.capacity:
                print('Container is at capacity!')
            else:
                x = self.weight - self.capacity # checks to see how over weight this container is.
                print('Container is over capacity! Remove ' + str(x) + ' from this container!') 
        # because we are in a different function with a different namespace, we have to copy our class here. 
        # normally, classes would be used to avoid this problem.

    Container1 = Example(10)
    Container2 = Example(20)
    Container3 = Example(5)
    Container4 = Example(100)
    # we have now defined several objects for our example class.
    # we can now use the base class to pull information about the objects.

    # let's check the weight of all of our containers to make sure they are empty.
    print(Container1.weight, Container2.weight, Container3.weight, Container4.weight)

    # now that we have confirmed our containers are empty, let's check the capacities.
    print(Container1.capacity, Container2.capacity, Container3.capacity, Container4.capacity)

    # let's start addling weight to the containers.
    Container1.addWeight()
    Container2.addWeight()
    Container3.addWeight()
    Container4.addWeight()

    # now that we have added weight, we will want to check the capacity.
    Container1.checkCapacity()
    Container2.checkCapacity()
    Container3.checkCapacity()
    Container4.checkCapacity()

        
    return()

def inheritance():
    # this section will contain notes covering the creation of child classes. 

    # we can use inheritance to assist when creating new classes that need to be similar to existing classes. 
    # we can create a class with a core set of properties and methods and then create child classes for more specific uses that extend the properties and methods available in the parent class. 

    class Person():
        def __init__(self, fname, lname): # properties that objects are initialized with.
            self.firstname = fname # property definitions
            self.lastname = lname

        def printname(self): # method definition
            print(self.firstname, self.lastname)

    # we won't create objects for this class.
    # instead, we will create child classes for the sub types we want to manage with additional properties and methods. 

    class Student(Person):
        def __init__(self,fname,lname,major,minor): # properties that objcts will be initialized with.

        # defining __init__ in a sub class overwrites the __init__ from the parent which means we need to call it back into the sub class in order to access its properties. 
        # we do this with the super() function. 
            super().__init__(fname,lname) # inherit property definitions from parent class.
            self.major = major # create additional properties.
            self.minor = minor

        def printfull(self): # create an additional method.
            print(self.firstname, self.lastname, self.major, self.minor)

    class Professor(Person):
        def __init__(self, fname, lname, department, specialization):
            super().__init__(fname,lname)

            self.department = department
            self.specialization = specialization

        def printfull(self):
            print(self.firstname, self.lastname, self.department, self.specialization)

    # at this point we are ready to define objects for our child classes. 

    John = Student('John', 'Doe','Computer Science','Machine Learning')

    John.printfull()

    Jane = Professor('Jane','Doe','Sciences','Machine Learning')

    Jane.printname()

    return()



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
    return()



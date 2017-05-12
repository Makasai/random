##Encapsulation
* Safe storage of data in an instance
	* instance state (data) should be accessed only through methods 
		* if not = 'breaking encapsulation' 
	* safe from external processes
	* usually a 'setter' method (but not neccessarily)
	* voluntary restriction in python

_____init_____ validates instance values before instance is returned for the first time  

* can be used for networking (check the socket connection)





##Class vs. Instance attributes
**instance** attributes, then **class**  
class instance is shared among instances



##Inheretance
* use 'super' to call method from parent class

python has a 'new style' class where classes can inherit from 'object' class  

* ex. class Child(object):
	* related to multiple inheritance 

##Multiple Inheritance
* classes can inherit from many parents
* mro - method resolution order 
* python looks 'depth-first'


##Polymorphism
* same interface between different objects that do similar (if not the same) things
	* ex. Cat().show_affection() vs.Dog().show_affection

	
##Decorators
**@classmethod**  

* now the method is no longer bound (affecting the instance per se) and is done on the class  
* def *method*(cls) vs def *method*(self)

**@staticmethod**  

* neither class nor instance method. Utility method. Not a bound method, it is a static method.  
Add this method decorator if the method will not be used on the instance or class.

##Abstract Class
These classes aren't instantiated, but used to be subclassed. Creates a template for classes

metaclass - class used to define other classes  
@abc.abstractmethod

* what does that mean??

when implementing an abstract class, you cannot create an instance of it  

	Class DummyClass(object):
	@abc.abstractmethod
	def print_something(self):
		print("do something")

abstract methods must be implemented  
create 'interface' = methods that must be implemented by subclasses


##Inheritance Examples
1. Inherit - simply use parent methods
2. Override/Overload - child method has same name, but does something different than parent
3. Extend - add additional functionality to parent method
4. Provide - implement required abstract method from parent

##Syntactic Sugar (Core Syntax)
######www.rafekettler.com/magicmethods.html (for more magic methods)
var + var2 ===> var._____add_____(var2)  
it actually resolves to a method call!  
Remeber, the double underscore means it is meant to be implicitly called, though it is possible to call it directly

We can create classes and take adv of this 'syntactic sugar'



def _____repr_____(self):  
return str(self.mylist)

"print" calls _____repr_____()

##Inheriting from Core (Built-in)Objects
Examples of core objects from python: dict, str, int, list

ex. class MyDict(dict):

you can create a custom core object!

##Attribute Encapsulation
Remember, you can set attributes in any object/class at anytime (ex. x.thing = 'hello'), but this breaks encapsulation; doesn't force user through process nor through regulation

however, because python does not enforce privacy, it relies on user cooperation. To force a user into a specific behavior is un-pythonic

@property  
add this decorator to attribute and it will be "encapsulate-able"

**For example:**  
@property
def var(self)

@var.setter
def var(self, value)

@var.deleter
def var(self)

##Private Variables
"Private" attributes defined for a class will not be imported/subclassed "_____var_____"

##With
in a 'with' block, there are two magic classes _____enter____ and _____exit_____  

* they are called when 'entering' and 'exiting' a with block

useful when creating a class that needs to clean up after itself and doesn't want to rely on user manually cleaning up   

* ex. allocating space, or networks that need to be closed after use

##New-Style Classes
ex. class TestClass(object):

* after python 3, all classes will need to inherit from the super ancestor class **object**   
* These new classes can be constructed with 'metaclasses'
	* Metaclasses can create classes, as classes create instances; you can build classes from metaclasses. 
		*  you can set default attributes
		*  can create classes with special behaviors like, 'only one instance of this class can be created'

* descriptors

##Error/Exception handling
sys.exit() - cause programs to exit

each Exception instance has two attributes, 'message', and 'args'

* message - contains message that Python would display
* args - tuple containing arguments, with first element being the message

### Custom Exceptions
can raise exceptions  
ex. raise ValueError('please submit number...')

You don't necessarily use a 'try' block, you can raise an exception when appropriate.

##Serialization
(this respects Object Oriented Programming)
*persistant storage* i.e: on disk  
object serialization - store python obj as 'obj'  
convert python object to character stream, which can then be transmitted over network. From RAM to text  
can save state of ipython session to a file that you can recreate later. *That seems pretty useful*

###Pickling
pickling - create python object, change values (into data that is more compact), then stores it  
not human readable
	
	
	//store object
	with open('datafile.txt', 'w') as fh:
		pickle.dump(obj, fh)
	
	//return object
	with open('datafile.txt') as fh:
		unpickledlist = pickle.load(fh)
	
	//dumps and loads are for strings. You can dump to strings
	
		
* you can store instances along with its attribute values  
what....that's pretty cool  
* it would be as if it never stopped running. You can store most objects as a pickle, however, you need the relevant code to be available.

Pickling does not store classes, modules, nor functions, rather it stores *references* to them. (ooooo pointers? :P)  

cPickle is a c-compiled implementation (it's faster)


if pickle complains about not having the same class object:  
	
* pickle doesn't like dumping an object that's changed since it's creation [http://pythoscope.org/dont-use-pickle-for-object-serialization](http://pythoscope.org/dont-use-pickle-for-object-serialization)

###JSON
Javascript Object Notation

More human-readable than pickling

uses dump(s) and load(s) 

json.dump json.load


###YAML
Yet Another Markup Language
YAML Ain't Markup Language

Even more human-readable!


##Debugging
PDB - "Python Debugger"

You can pause the execution, and check values of variables:   

	pdb.set_trace()
	
pretty useful. Will be in all python distributions

##Logging
Levels of "Severity"

- DEBUG (debug())
- INFO (info())
- WARNING (warning()) 
- ERROR (error())
- CRITICAL (critical())

default level is **WARNING**

logging.basicConfig(level=logging.DEBUG, filename='log1.txt', format='%(asctime)s	%(levelname)s:%(message)s')

check the parameters of **basicConfig** to customize it


##Benchmarking
comparing two snippets of code to see which execute faster

* you'll want to run test multiple times  
* times are affected by what else is running on your machine, so the lowest time is usually considered the 'most accurate' 


##PyTest
PyTest is a module useful for testing  

* Each piece of code (i.e. functions) are considered a 
**unit**

**Unit testing**: testing each unit of code

Let's say you want to test your program, myprogram.py  
The test program would be called test_myprogram.py  
pytest will recognize the 'test__' prefix

assert:  

* if statement is true, assert will stay silent!
* with pytest.raises() - assert an exception will be raised

run py.test and it will test all 'test__' programs


**Test-Driven Development**  

* writing tests first, and then developing code to fulfill tests


Can group tests that test similar script along with appropriate variables

Test will usually provide own mock data as to not change any production data

setup_class()  
teardown_class()  


You need to write tests for your programs!

### Writing a good test

1. Create a class to group all related tests together
2. Define all necessarily inputs as variables as class variables. Define them before creating test methods (i.e. test_method(self))
3. Try to account for all possible outputs. Remember, the user may not use method correctly
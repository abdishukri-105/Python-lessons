# variables 

 Variables are containers for storing data values.

## general rules 
- String variables can be declared either by  using single or double quotes:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.



   Python has no command for declaring a variable.

 # Multi Words Variable Names

  -  Camel Case - Each word, except the first, starts with a capital letter: e.g myVariableName = "John"

  - Pascal Case - Each word starts with a capital letter: e.g MyVariableName = "John"

  - Snake Case - Each word is separated by an underscore character: e.g my_variable_name = "John"

  ## Global Variables

  Variables that are created outside of a function (as in all of the examples above) are known as global variables.

  Global variables can be used by everyone, both inside of functions and outside.

## The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword
    
    
          x = "awesome"

            def myfunc():
            global x
            x = "fantastic"

            myfunc()

            print("Python is " + x)

        
       




          

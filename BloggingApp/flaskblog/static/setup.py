from cx_Freeze import setup, Executable 
  
setup(name = "Doc Scanner" , 
      version = "0.1" , 
      description = "" , 
      executables = [Executable("Scanner.py")])
from pathlib import Path

def create_project(self,name:('The name of project','positional')):
    '''
    Creates a plac cli project.
    '''
    project= Path(name)
    if project.exists():
        raise Exception(f'{name} already exists!')
    project.mkdir()
    (toolbox:=project/'toolbox').mkdir()
    tools = toolbox/'tools.py'
    tools.write_text(f"""def {name}():
'''
This is just a dummy sub command to use as an example.
You can use this as help message.
'''
    """)
    cli:Path = project / f'{name}.py'
    class_name = name.capitalize()
    cli.write_text(f"""from plac import Interpreter
from typing import Callable
from importlib import import_module
from inspect import getmembers, isfunction


def get_tools() -> list[tuple[str,Callable]]:
    tools = import_module('toolbox.tools')
    return [ (n,tool) 
            for n,tool in getmembers(tools) 
            if isfunction(tool)]
    
class {class_name}(object):
    
    commands = tuple(n for n,_ in get_tools()) 
   
for name,tool in get_tools():
    setattr(MagicToolBox,name,tool) 
        
if __name__ == '__main__':
    Interpreter.call({class_name})
    """)
    print(f'Created {name}/{name}.py and {name}/toolbox/tools.py')
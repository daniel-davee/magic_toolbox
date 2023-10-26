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

class {class_name}():
commands = tuple()

if __name__ =='__main__':
Interpreter.call({class_name})
    """)
    
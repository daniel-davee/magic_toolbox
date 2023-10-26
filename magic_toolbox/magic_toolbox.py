from inspect import currentframe, getframeinfo
from pathlib import Path
import plac


mwd = Path(__file__).parent.absolute()


class MagicToolBox(object):
    
    """
    A CLI framework

    Raises:
        plac.Interpreter.Exit: [signals to exit interactive interpreter]
    """
    
 
    
    commands = 'create', 
    
    def create_project(name:('The name of project','positional')):
        ...
    
        
if __name__ == '__main__':
    plac.Interpreter.call(MagicToolBox)
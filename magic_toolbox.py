#!/home/mage/anaconda3/envs/magic38/bin/python
from io import DEFAULT_BUFFER_SIZE
from run_cmd.run_cmd import run_cmd
from shutil import copytree
from os import environ, error
from yaml import load, FullLoader
from pysimplelog import Logger
from run_cmd.run_cmd import run_cmd
from pathlib import Path
from inspect import currentframe, getframeinfo
import plac
from yes_or_no.yes_or_no import yes_or_no
from features.behave_util import logger

logger.set_log_file_basename(__name__)

mwd = Path(__file__).parent.absolute()

import_path = f"""
from sys import path
"""

path_append = f"""
path.append('{mwd}')
"""
class MagicToolBox(object):
    
    """[Manages a tool box of util and other cli tools]

    Raises:
        plac.Interpreter.Exit: [signals to exit interactive interpreter]
    """
    
 
    tools = set([t.stem for t in mwd.iterdir() if (t / '__init__.py').exists()])
    
    commands = 'quit', 'exit', 'add', 'init', 
    
    def quit(self):
        "quits the interpreter"
        raise plac.Interpreter.Exit

    def exit(self):
        "exits the interpreter"
        self.quit()

    def init(self,target:('The target directory','positional')=''):
        """[a]
        """
        cwd = Path(target)
        tbx = cwd / 'tool_box'
        tbx.mkdir(exist_ok=True, parents=True)
        init = tbx / '__init__.py'
        init.touch(exist_ok=True)
        init_text = init.read_text()
        init_text = init_text if import_path in init_text else\
                    import_path + init_text
        init_text += path_append
        init.write_text(init_text)
        
    def add(self,target:('The target directory','positional')='',
            copy_:('When true full copy instead sym_lnk','flag','c') = False):
        """
        Adds a sym link in magic_dict dircetory 
        """
        
        target = Path(target).absolute()
        stem = target.stem
       
        debug_msg = f"""
                        What is {target=}? 
                        What is {stem=}? 
                        """
        logger.debug(debug_msg)
          
        copytree(target, mwd / stem) if copy_ else\
        (mwd / stem).symlink_to(target)
        
if __name__ == '__main__':
    plac.Interpreter.call(MagicToolBox)
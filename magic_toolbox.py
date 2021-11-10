#!/home/mage/anaconda3/envs/magic38/bin/python
from os import SEEK_CUR
from yaml import load, FullLoader
from pysimplelog import Logger
from run_cmd.run_cmd import run_cmd
from pathlib import Path
from inspect import currentframe, getframeinfo
import plac
from ask.ask import yes_or_no

logger = Logger(__name__)

logger.set_minimum_level(logger.logLevels['warn'])
logger.set_log_file_basename(__name__)
# fmt = "[%(levelname)s] - %(asctime)s - %(name)s - :  in %(pathname)s:%(lineno)d \n%(message)s"
# logger._Logger__logTypeFormats = {level:fmt for level in logger.logLevels}
log_header = """############################
                file_name:{}
                line_number:{}
                """
class MagicToolBox(object):
    
    """[summary]

    Raises:
        plac.Interpreter.Exit: [signals to exit interactive interpreter]
    """
    
    mwd = Path(__file__).parent
    
    tools = set([t.stem for t in mwd.iterdir() if (t / '__init__.py').exists()])
    
    commands = 'quit', 'add', 'init', 
    
    def quit(self):
        "quits the interpreter"
        raise plac.Interpreter.Exit

    def init(self):
        """[setup toolbox directory and mtb.yml]
        """
        cwd = Path.cwd()
        tool_box = (cwd / 'tool_box')
        tool_box.mkdir(exist_ok=True)
        mtb = (tool_box / 'mtb.yml')
        mtb.touch(exist_ok=True)

    def add(self,tool_name):
        """
        adds a tool named tool_name if exist
        """ 
        cwd = Path.cwd()
        files = [cwd / f for f in ['tool_box','tool_box/mtb.yml']]
        if not all([f.exists() for f in files]): self.init()
        tool_box, mtb = files
        debug_msg = f"""
                        {getframeinfo(currentframe())=}
                        What is {self.mwd.absolute()=}?
                        Whats is cwd?: {cwd=}
                        what is {files=}?
                        Is {yes_or_no(f'{tool_box=} a directory?', tool_box.is_dir())}
                        {yes_or_no(f'{mtb=} exists?', mtb.exists())}
                        What is {mtb=}?
                        """
        logger.debug(debug_msg)
                        
        mtb = load(mtb.read_text(), Loader=FullLoader)
        debug_msg = f"""What is mtb{mtb=}?
                        """
        logger.debug(debug_msg)
                        
        debug_msg = f""" Is{yes_or_no(f"{tool_name=} in {self.tools}", tool_name in self.tools)}
                        """
        logger.debug(debug_msg)
                        
        if tool_name not in self.tools:
            ls = run_cmd(f'ls {self.mwd.absolute()}',split=True)
            msg = f"""{tool_name=} is not in {self.tools=}
                    what is in {self.mwd.absolute()=} using ls?
                    {ls=}
                    {yes_or_no(f'is {tool_name=} in {self.mwd.absolute()}',tool_name in ls)}
                    {yes_or_no(f'is {tool_name=} in {self.tools}',tool_name in ls)}
                    that should definitly be no"""
            logger.error(msg)
            raise ValueError(msg)
        
        des = (tool_box / tool_name).absolute()
        src = ( self.mwd / tool_name).absolute()
        
        
        debug_msg = f"""
                        what is {str(des.absolute())=}?
                        what is {str(src.absolute())=}?
                        {yes_or_no('is src == des?', src == des)}"""
        logger.debug(debug_msg)
        assert des != src, f"""{yes_or_no(f'is {des=} equal to {src=}?', des == src)}"""
                        
        if des.is_symlink():
            des.unlink()
        debug_msg = f"""
                        {yes_or_no('does {src=} is dir?', src.is_dir())}
                        {yes_or_no('is {des.is_symlink()=}?',des.is_symlink())}"""
        logger.debug(debug_msg)
            
        des.symlink_to(src)
        debug_msg = f"""
                        what is {str(des.absolute())=}?
                        what is {str(src.absolute())=}?
                        {yes_or_no(f'is {des=} as sym link?', des.is_symlink())}"""
        logger.debug(debug_msg)
        
if __name__ == '__main__':
    plac.Interpreter.call(MagicToolBox)
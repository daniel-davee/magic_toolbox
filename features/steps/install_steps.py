from behave import*
from pathlib import Path
from run_cmd.run_cmd import run_cmd
from magic_dict.magic_dict import Magic_dict
from magic_toolbox import MagicToolBox, mwd
from yes_or_no.yes_or_no import yes_or_no
from setup_steps import logger
from os import environ
@given(u'magic_toolbox has ben installed')
def step_impl(context):
    shell = environ['SHELL']
    path = environ['PATH'].split(':')
    def in_path():
        return str(mwd) in environ['PATH'].split(':')
    debug_msg = f"""
                    What is {shell=}?
                    What is {mwd=}?
                    What is {path=}?
                    {yes_or_no(f'Is {str(mwd)} in path?', in_path())}
                    """
    logger.debug(debug_msg)
    assert_msg = debug_msg

    if not in_path():
        cmd = f'fish_add_path {str(mwd.absolute())}' if 'fish' in shell else\
              f'export PATH=$PATH:{str(mwd.absolute())}'
       
        debug_msg = f"""
                        What is {cmd=}?
                        """    
        logger.debug(debug_msg)
        assert_msg += debug_msg
        
        out = run_cmd(cmd)
    
        debug_msg = f"""
                        What is {out=}?
                        """    
        logger.debug(debug_msg)
        assert_msg += debug_msg
 
    mtb = mwd / 'magic_toolbox'
    mpy = mwd / 'magic_toolbox.py'
    
    debug_msg = f"""
                    What is {mtb=}?
                    what is {mpy=}?
                    """    
    logger.debug(debug_msg)
    assert_msg += debug_msg
    
    if not mtb.exists():mtb.write_text(mpy.read_text())
    
    mtb.chmod(mode=0o777)
     
    debug_msg = f"""
                    {yes_or_no(f'Does {mtb} exists?', mtb.exists())}
                    {yes_or_no(f'Is {str(mwd)} in path?',in_path())}
                    """    
    logger.debug(debug_msg)
    assert_msg += debug_msg

    assert in_path(), assert_msg
    assert mtb.exists, assert_msg 

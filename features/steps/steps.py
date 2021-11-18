from pysimplelog import Logger 
from behave import*
from pathlib import Path
from run_cmd.run_cmd import run_cmd
from magic_dict.magic_dict import Magic_dict
from magic_toolbox import MagicToolBox
from yes_or_no.yes_or_no import yes_or_no
from os import environ

logger = Logger(__name__)

logger.set_minimum_level(logger.logLevels['warn'])
logger.set_log_file_basename(__name__)
    
def value_as_type(value,type_):
    return eval(type_)(value)

@given(u'{path} is DNE')
def step_impl(context,path):
    path = Path(path)
    if path.exists():
        warn = f"""{path} should be DNE
                    but {path.exists()=}
                    did you want to rm {path=}?
                    {yes_or_no(f"{context.safe_rm=}"),context.safe_rm}"""
        logger.warn(warn)
        cmd = f'rm -rf {path}'
        _ = run_cmd(cmd)
    assert not path.exists()

@when(u'run cmd {cmd}')
def step_impl(context,cmd):
    context.result = run_cmd(cmd)
    debug_msg = f"""DEBUG 0000###
                    run cmd {cmd=} => {context.result=}"""
    logger.debug(debug_msg)


@then(u'{path} exist')
def step_impl(context,path):
    
    path = Path(path)
    debug_msg = f"""{yes_or_no(f"Does {path=} exist?", path.exists())}
                    Maybe you mispelled in feature file"""
    logger.debug(debug_msg) 
    
    assert path.exists(), debug_msg

@given(u'logging level is {level}')
def step_impl(context,level):
    levels = {'debug': 0.0,
              'info': 10.0,
              'warning': 20.0,
              'error': 30.0,
              'critical': 100}
    logger.set_minimum_level(levels[level])
    
@given(u'{var} is {value} as {type_}')
def step_impl(context, var, value, type_):
    value_ = value_as_type(value, type_)
    setattr(context,var,value)
    msg = f"""{var=} is {value=} as {type_}
              What is type of {var}?
              {type(value)=}
              {yes_or_no(f'does context have {var}', hasattr(context,var))}"""
    assert hasattr(context, var), msg
    assert getattr(context,var) == value, msg

@given(u'magic_toolox.py is installed')
def step_impl(context):
    dirs = list(MagicToolBox.mwd.iterdir())
    
    debug_msg = f"""What is {dirs=}?
                    {yes_or_no("Is dist in in dir?", 'dist' in dirs)}
                    """
    logger.debug(debug_msg)
    
    if 'dist' not in dirs:
        cmd = 'pyinstaller -F magic_toolbox.py'
        out = run_cmd(cmd)
        
        debug_msg = f"""Ran {cmd}
                        What is {out=}?
                        """
        logger.debug(debug_msg)
        
    path_var = [Path(p) for p in environ['PATH'].split(':')]
    dist = (Path.cwd() / 'dist').absolute()
    
    debug_msg = f"""What is {path_var=}?
                    What is {str(dist)=}?
                    {yes_or_no(f'Is {str(dist)} in {[str(p) for p in path_var]}',
                        dist in path_var)}
                    """
    logger.debug(debug_msg)
    
    if dist not in path_var:
        logger.info(f'adding {str(dist)} to $PATH')
        cmd = f'fish_add_path {str(dist)}'
        out = run_cmd(cmd)
        debug_msg = f"""{cmd=} => {out}
                            """
        logger.debug(debug_msg)
        
    cmd = 'echo $PATH'
    out = run_cmd(cmd)
    debug_msg = f"""{cmd} => {out}
                    {yes_or_no(f'Is {str(dist)} in  {out}', str(dist) in out)}
                    What is {str(dist)}?
                    """
    logger.debug(debug_msg)
    
    assert str(dist) in out, debug_msg
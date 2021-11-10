from pysimplelog import Logger 
from behave import*
from pathlib import Path
import magic_dict
from run_cmd.run_cmd import run_cmd
from magic_dict.magic_dict import Magic_dict

logger = Logger(__name__)
logger.set_log_file_basename('behave_magic_toolbox')

def yes_or_no(question:str, answer:bool):
    return question + '\n' + ('yes' if answer else 'no')
    
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


@then(u'{} exist')
def step_impl(context,path):
    path = Path(path)
    msg = f"{path.exists()=}" 
    assert path.exists(), msg

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

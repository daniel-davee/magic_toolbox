from behave import *
from setup_steps import logger
from pathlib import Path
from yes_or_no.yes_or_no import yes_or_no
from behave_util import logger 
from magic_dict.magic_dict import Magic_dict
from run_cmd.run_cmd import run_cmd
from magic_toolbox import mwd

        
@given(u'{name}["{key}"] is {value}')
@when(u'{name}["{key}"] is {value}')
@given(u"{name}['{key}'] is {value}")
@when(u"{name}['{key}'] is {value}")
def step_impl(context, name, key, value):
    
    debug_msg = f"""
                    {name=} is {value=}
                    """
    logger.debug(debug_msg)
    this = context.this
    this[name][key] = eval(value) 
    

@given(u'{name} is {value}')
@when(u'{name} is {value}')
def step_impl(context,name,value):
   this = context.this
   value = eval(value) 
 
   debug_msg = f"""
                   {name=} is {value=}
                   """
   logger.debug(debug_msg)
   assert_msg = debug_msg
  
   this[name] = value
 
   debug_msg = f"""
                   {yes_or_no(f'Is {this[name]()=} equal to {value}',
                    this[name]() == value)}
                   """
   logger.debug(debug_msg)
   assert_msg += debug_msg  
   
   assert this[name], assert_msg
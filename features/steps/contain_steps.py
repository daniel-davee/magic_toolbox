from behave import*
from pathlib import Path
from run_cmd.run_cmd import run_cmd
from magic_dict.magic_dict import Magic_dict
from magic_toolbox import MagicToolBox, mwd
from yes_or_no.yes_or_no import yes_or_no
from setup_steps import logger


@given(u'{value} not in {obj}')
@then(u'{value} not in {obj}')
def step_impl(context, value, obj):
    this = context.this
    value = eval(value)
    obj = eval(obj)
    debug_msg = f"""
                    Given  {value=} in {obj=})
                    {yes_or_no(f'Is {value} in {obj}?', value in obj)}?
                    """
    logger.debug(debug_msg)
    assert_msg = debug_msg
    
    assert value not in obj, assert_msg 

@given(u'{value} in {obj}')
@then(u'{value} in {obj}')
def step_impl(context, value, obj):
    this = context.this
    value = this[value]()
    obj = eval(obj)
    debug_msg = f"""
                    Given  {value=} in {obj=})
                    {yes_or_no(f'Is {value} in {obj}?', value in obj)}?
                    """
    logger.debug(debug_msg)
    assert_msg = debug_msg
    
    assert value in obj, assert_msg 



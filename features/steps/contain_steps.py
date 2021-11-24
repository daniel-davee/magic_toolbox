from behave import*
from pathlib import Path
from run_cmd.run_cmd import run_cmd
from magic_dict.magic_dict import Magic_dict
from magic_toolbox import MagicToolBox
from yes_or_no.yes_or_no import yes_or_no
from behave_util import value_as_type
from setup_steps import logger
    



@given(u'{key} not in {name}')
def step_impl(context, key, name):
    this = context.this
    debug_msg = f"""
                    Given  {key=} not in {name=})
                    {yes_or_no(f'Is {key} not in this?', key not in this)}?
                    """
    logger.debug(debug_msg)
    assert_msg = debug_msg
    
    assert key not in this, assert_msg 



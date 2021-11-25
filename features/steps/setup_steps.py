from behave import *
from magic_dict.magic_dict import Magic_dict
from yes_or_no.yes_or_no import yes_or_no
from behave_util import logger 


#Given log level is set to debug
@given(u'log level is set to {level}')
def step_impl(context,level):
    
    context.this = Magic_dict('this')
    logger.set_minimum_level(logger.logLevels[level])
    degbug_msg = f"""
                     What is {level=}?
                     What is {logger.stdoutMinLevel=}?
                     {yes_or_no(f'Is {logger.logLevels[level]=} equall to {logger.stdoutMinLevel}?',
                     logger.logLevels[level] == logger.stdoutMinLevel)}
                     """
    logger.debug(degbug_msg)
    
    assert logger.logLevels[level] == logger.stdoutMinLevel

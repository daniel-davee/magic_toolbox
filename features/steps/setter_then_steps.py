from behave import *
from setup_steps import logger
from yes_or_no.yes_or_no import yes_or_no
from behave_util import logger 
from magic_dict.magic_dict import Magic_dict

        
#Then foo is instance of Magic_dict
@then(u'{name} is instance of {type_}')
def step_impl(context, name, type_):
    
    this = context.this
    type_ = eval(type_)
    is_label = '()' not in name
    name = name if is_label else name[:-2]
    obj = this[name] if is_label  else this[name]()
    
    debug_msg = assert_msg = f"""
                                 {name=} is instance of {type_=}
                                 What is {obj=}?
                                 {yes_or_no('Do we add a ()', not is_label)}
                                 """
    logger.debug(debug_msg)
     
    debug_msg = f"""
                    {yes_or_no(f'Is {name} the type of {type_}',
                    isinstance(obj, type_))}
                    """
    logger.debug(debug_msg)
    assert_msg += debug_msg 
    
    assert isinstance(obj,type_)

@then(u'{name}["{key}"] is {value}')
@then(u"{name}['{key}'] is {value}")
def step_impl(context, name, key, value):
     
    this = context.this

    debug_msg = f"""
                    Then  {name=}["{key=}"] is {value=}
                    What is {eval(value)=}?
                    {yes_or_no(f'Is {name} in this?', name in context.this)}
                    {yes_or_no(f'Does {name}["{key}"] == {eval(value)}?', 
                     eval(value) == this[name][key]())}
                    """
    logger.debug(debug_msg)
    
    assert eval(value) == this[name][key](), debug_msg


@then(u'{name} is {value}')
def step_impl(context, name, value):
    
    this = context.this
    obj = this[name]()
    value = eval(value) 
    debug_msg = f"""
                    Then {name=} is {value=}?
                    What is {obj=}?
                    {yes_or_no(f'Is {name} in this?', name in context.this)}
                    {yes_or_no(f'Does {name} == {value}?', value == obj)}
                    """
    logger.debug(debug_msg)
    
    assert value == obj, debug_msg
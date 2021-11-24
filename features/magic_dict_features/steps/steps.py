from behave import *
from magic_dict.magic_dict import Magic_dict
from yes_or_no.yes_or_no import yes_or_no
from typing import Any
from pysimplelog import Logger

logger = Logger(__name__)
logger.set_log_file_basename('run_cmd')

def value_as_type(value,type_):
    return eval(type_)(value)

@given(u'foo is testing Magic_dict')
def step_impl(context):
    context.name = 'foo'
    context.create = Magic_dict

@given(u'input is {value} as {type_}')
def step_impl(context,value,type_):
    """[input is {value} as {type_}]
    """
    value_ = value_as_type(value,type_)
    context.input = value_
    questions = f"""input is {value=} as {type_=}
                    what is the input value as string?
                    {value=}
                    what is the value as {type_=}?
                    {value_=}
                    what is context.input?
                    {context.input=}"""
    assert context.input == value_, "context.input error:\n" + questions
    assert isinstance(context.input, eval(type_)), "type error:\n" + questions

@given(u'log level is set to {level}')
def step_impl(context,level):
    """[sets the log level]

    Args:
        context ([type]): [description]
        level ([type]): [description]
    """
    
    logger.set_minimum_level(logger.logLevels[level])
    degbug_msg = f"""
                     What is {level=}?
                     What is {logger.stdoutMinLevel=}?
                     {yes_or_no(f'Is {logger.logLevels[level]=} equall to {logger.stdoutMinLevel}?',
                     logger.logLevels[level] == logger.stdoutMinLevel)}
                     """
    logger.debug(degbug_msg)
    
    assert logger.logLevels[level] == logger.stdoutMinLevel

@given(u'foo is created')
def step_impl(context):
    _input = context.input if hasattr(context,'input') else None
    context.foo = context.create(_input) if _input else context.create()
    


@then(u'{obj} is is instance of Magic_dict')
def step_impl(context, obj:Any):
    """
    foo needs to be an instance of Magic_dict
    """
    obj_ = getattr(context,obj)
    debug_questions = f"""then {obj=} is instance of Magic_dict
                            {yes_or_no(f"is {obj=} in context(hasattr)",hasattr(context,obj))}
                            What is type(context.{obj})?
                            {type(getattr(context,obj))=}
                            What is context.result?
                            {context.result=}
                            {yes_or_no(f"Is context.result == context.{obj} {obj_}?", context.result == obj_)}
                          """
    assert isinstance(obj_, Magic_dict), debug_questions 

@when(u'foo exist')
def step_impl(context):
    """ {yes_or_no('Does foo exist?', context.foo)}
        What is context?{context=}
        yes_or_no('context has foo',hasattr(context,'foo'))
        """
        
    assert context.foo, eval("f'{}'".format(step_impl.__doc__))
    context.result = bool(context.foo)


@then(u'result is {value} as {type_}')
def step_impl(context,value,type_):
    """{context.result=} is {value=} as {type_}"""
    value = value_as_type(value, type_)
    msg = f"""{context.result=} is {value=} as {type_}
                what is context?
                {dir(context)=}
                what is {value=} as {type_=}?
                {value_as_type(value,type_)} as type {type(value)}
                what is result?
                {context.result=}
                {yes_or_no('is result the same as value, check type again?', context.result == value)}"""
    assert context.result == value, msg
    
@given(u'foo.{key} = {value} as {type_}')
def step_impl(context, key, value, type_):
    """foo.key ={value=} as {type_}"""
    value = value_as_type(value,type_)
    setattr(context.foo,key,value)




@given(u'foo["{key}"] = {value} as {type_}')
def step_impl(context, key, value, type_):
    """[given foo[{key=}] = {value=} as {type_=}]

    Args:
        context ([context]): [context I don't know ask behave?]
        key ([str probably]): [key being set]
        value ([any]): [the object]
        type_ ([type]): [gives the type for behave to check]
    """
    value = value_as_type(value,type_) 
    context.foo[key] = value
    questions = f"""given foo[{key=}] = {value=} as {type_=}
                    what context.foo[key]?\n{context.foo[key]=}
                    what context.foo.key?\n{getattr(context.foo,key)=}
                    what context.foo.key?\n{ context.foo.bar =}
                    what is type of value?\n{type(value)=}"""
    logger.debug(questions)

@given(u'{key} not in foo')
def step_impl(context,key:str):
    """[{key} not in foo]
    """
    msg = f"""
            What is key?
            {key=}
            whats dir context?
            {dir(context)=}
            {yes_or_no('does contex have foo', hasattr(context,'foo'))}
            {yes_or_no('is key in foo?',key in context.foo)}"""
    assert key not in context.foo, msg

@given(u'foo does not have {attr}')
def step_impl(context,attr):
    """[foo does not have attr {attr}]
    """
    msg = f"""
            What is attr?
            {attr=}
            whats dir context?
            {dir(context)=}
            {yes_or_no('does contex have foo', hasattr(context,'foo'))}
            {yes_or_no('does foo has attr?',hasattr(context.foo, attr))}"""
    assert hasattr(context.foo,attr), msg

@when(u'result is foo.{key}')
def step_impl(context,key):
    context.result = getattr(context.foo,key)

@when(u'result is foo["{key}"]')
def step_impl(context,key):
    context.result = context.foo[key]
    debug_message = f"""trying to get {key=} out of foo
    ********************************************************
        {yes_or_no('Does foo exist?',context.foo)}
        {yes_or_no(f'is {key=} in foo',key in context.foo)}
        What is {context.foo[key]=}
        What is {context.result=}?
        {yes_or_no(f'is context.result == context.foo[{key}]',context.result == context.foo[key])}"""
    assert context.result == context.foo[key], debug_message
    logger.debug(debug_message)
    
@when(u'result is foo()')
def step_impl(context):
    context.result = context.foo()
    questions = f"""{yes_or_no("foo in context?", hasattr(context,'foo'))}
                    What is foo._obj?
                    {context.foo._obj=}
                    What is foo()?
                    {context.foo()=}
                    {yes_or_no('is contex.result the same as context.foo()',context.result == context.foo())}"""
    assert context.result == context.foo()
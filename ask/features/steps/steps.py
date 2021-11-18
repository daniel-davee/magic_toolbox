from behave import *
from pysimplelog import Logger
from yes_or_no.yes_or_no import yes_or_no

from magic_dict.magic_dict import Magic_dict

logger = Logger(__name__)
logger.set_log_file_basename(__name__)

@given(u'logging level is {level}')
def step_impl(context,level):
    logger.set_minimum_log_level(logger.logLevel[level])


@given(u'context object is {call}')
def step_impl(context,call):
    debug_msg = assert_msg = f"""
                    What is {call=}?
                    """
    logger.debug(debug_msg)                
            
    call = eval(call)
    
    debug_msg = f"""
                    {yes_or_no(f'is {call=} callable?', callable(call))}
                    """
    logger.debug(debug_msg)                
    assert_msg += debug_msg
    assert callable(call), assert_msg
    context.call = Magic_dict(call)
    


@given(u'input is {input_list}')
def step_impl(context, input_list):
    input_list = input_list.split(', ')
    args = [eval(i) for i in input_list if ':' not in i]
    kwargs = [i for i in input_list if i not in args]
    kwargs = [kv.split(':') for kv in kwargs]
    context.input = Magic_dict(dict([(k,eval(v)) for k,v in kwargs]))
    context.input.args = args
    

@when(u'context object is created')
def step_impl(context):
    args = context.input.args
    kwargs = context.input()
    context.object = context.call(*args,**kwargs)

def instance_of(obj,type_):
    type_ = eval(type_)
    return isinstance(obj,type_)

should_be = Magic_dict(eval)
should_be.instance_of = instance_of

@then(u'context object should be instance_of Magic_dict')
@then(u'context object should be {conditional}')
def step_impl(context, conditional):
    function = conditiona    


@then(u'context object.validate should be True')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context object.validate should be True')


@given(u'input is qt.Expand, {\'foo\' : \'bar\'}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given input is qt.Expand, {\'foo\' : \'bar\'}')


@then(u'context object.foo should be \'bar\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context object.foo should be \'bar\'')


@then(u'context object.choices should be instance_of dict')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context object.choices should be instance_of dict')


@given(u'input is qt.CheckBox, [\'foo\']')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given input is qt.CheckBox, [\'foo\']')


@then(u'context context should throw AssertionError')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context context should throw AssertionError')


@then(u'context object.validate should False')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context object.validate should False')


@given(u'input is qt.Expand, {\'key\': \'foo\', \'bar\':\'42\'}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given input is qt.Expand, {\'key\': \'foo\', \'bar\':\'42\'}')


@then(u'context object.key should be \'foo\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context object.key should be \'foo\'')


@then(u'context object.bar should be \'42\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then context object.bar should be \'42\'')


@given(u'input is qt.Expand, {\'ke\': \'foo\', \'bar\':\'42\'}')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given input is qt.Expand, {\'ke\': \'foo\', \'bar\':\'42\'}')


@given(u'input is qt.Expand, [\'foo\']')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given input is qt.Expand, [\'foo\']')

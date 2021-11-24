from keyword import iskeyword
import keyword
from typing import Any
from magic_dict.magic_dict import Magic_dict
from pysimplelog import Logger

from yes_or_no.yes_or_no import yes_or_no

logger = Logger(__name__)
logger.set_log_file_basename(__name__)

def value_as_type(value:str,type_:str or type) -> Any:
    """
    Take a string repersentation of vale,
    converts to type_, and returns the result    
    Don't use this with untrust
    Args:
        value (str): string repersentation
        type_ (str): the name of the type as string

    Returns:
        eval(type_)(value): [description]
    """
    if value == '_': return 
    type_ = type_ if isinstance(type_,type) else eval(type_)
    return type_(value)

    
    
def parse_symbol(this:Magic_dict, sym:str):
    
    is_identifier = sym.isidentifier() and not iskeyword(sym)
    debug_str = f"""
                    What is {list(this.keys())=}?
                    {yes_or_no(f'Is {sym=} vailid id?'),is_identifier}?
                    """
    logger.debug(debug_str)
    
    new_sym = sym.replace("['",'.').replace('["','.').\
                  replace("']",'').replace('"]','')
    head, tail = new_sym.split(".", 1) if '.' in new_sym else new_sym, None
    
    is_head_in_this = yes_or_no(f'Is {head=} in {this.keys()}?', head in this)
    the_next_question = f'eval({new_sym})' if 'no' in is_head_in_this else f'this[{head}]'
    the_next_answer = f'{eval(new_sym)}' if 'no' in is_head_in_this else f'{this[head]}'
    debug_str = f"""
                    What is {new_sym=}?
                    What is {head=}?
                    What is {tail=}?
                    {is_head_in_this}?
                    What is {the_next_question}? {the_next_answer}
                    """
    logger.debug(debug_str)
    
    if head not in this: return eval(new_sym)
    head = this[head]
    
    question = yes_or_no(f'Is {new_sym} = {sym}?', new_sym == sym) if tail else\
               yes_or_no(f'Is () at the end of {head=}', '()' == head[-2])
    
    answer = f'{head[tail]=}' if 'no' in question else\
             f'{getattr(head,tail)=}' if tail else\
             f'{head=}' if 'no' in question else\
             f'{head()=}'
    
    debug_str = f"""
                    {yes_or_no(f'Is {tail=} a thing?', tail)}
                    {question}?
                    {answer}
                    """
    logger.debug(debug_str)
    
    return head() if '()' == head[-2:] else head if not tail else\
           getattr(head,tail) if new_sym == sym else head[tail] 
    
#!/home/mage/anaconda3/envs/magic38/bin/python
import plac
from typing import Iterable, Callable, Any, Dict
from PyInquirer import prompt
from yaml import dump,load, FullLoader
from pathlib import Path
from enum import Enum
from magic_dict.magic_dict import Magic_dict
from yes_or_no.yes_or_no import yes_or_no
class Questions_Type(Enum):
    List = 'list'
    Raw_List = 'rawlist'
    Expand = 'expand'
    Confirm = 'confirm'
    CheckBox = 'checkbox'
    Input = 'input'
    Password = 'password'
    Editor = 'editor'

qt = Questions_Type

class Choices(Magic_dict):
    
    '''Choices interface'''
    
    should_be_dict = {qt.Expand, qt.CheckBox}
    
    def __init__(self,question_type:Questions_Type,
                 choices:Iterable):
        super().__init__(choices)
        self.question_type = question_type
        self['choices'] = choices
        self._assert(self.validate())
    
    def validate(self):
        if self.question_type in self.should_be_dict:
            assert isinstance(self.choices,Dict)
            if self.question_type is qt.Expand: 
                self.assert_('key' in self.choices, 'key not in choices')
        return True
 
class Question(Magic_dict):
    "Question Class keeps track of question"
    
    properties = {'message','type','name',
                  'choices','default','filter','eargs', 'validate'}
    
    must_have ='message', 'type', 'name'
     
    needs_choices = {qt.List, qt.Raw_List, 
                     qt.Expand, qt.CheckBox, qt.Confirm}
    
    def __init__(self, message: str, 
                 _type: Questions_Type, 
                 name: str,
                 choices: Iterable=[],
                 default: Any = None,
                 filter_: Callable = None,
                 validate: Callable = None):
        self['message'], self['type'], self['name'] = message, _type, name
        self['choices'], self['default'], self['filter'] = choices, default, filter_
        self['validate'] = self.validateor( validate)
        
    def validateor(self, validate):
        validate = validate or (lambda:True)
        def validate():
            assert validate()
            if self.type in self.needs_choices:
                pass
        assert all([h in self for h in self.must_have])
        return validate
        
    def _ask_choices(self,num=0):
        num = num if num else int(prompt(Question('How Many Choices?',
                                       'input','this_many')['this_many']))
        _questions = [("Define Choice (remaining:",
                       qt.Input,'choice')]
        if self.type in {qt.Expand, qt.CheckBox}:
            if self.type in qt.CheckBox:
                disable_any = [Question('Do you want to disable any choices',
                                       'confirmation','_disable',default=False)]
                if prompt(disable_any)['_disable']:
                    _questions += [('Disable this Choices?',
                                    'confirmation','disable')]
            else:
                _questions += [('Whats is the key',
                                'input','key')]
            
            
        return [prompt(Question(f'What is choice {i}',
                                qt.Input,'')) for i in range(num)]
        
    def __setattr__(self, key, value):
        assert key in self.properties
        return super().__setattr__(key, value)

class Answers(Magic_dict):
    
    '''
    Answer to an iterable of questions answer can be called with answer_obj.name_of_question,
    which if answered will replace the question with answer
    
    name_of_question:Question -> referece question or answer to question
    '''
    
    def __init__(self, questions:Iterable[Question]):
        '''
        questions:Iterable[Question] -> an iterable container of questions
        '''
        for question in questions:
            self[question.name] = question
            
    @property
    def unanswered(self):
        return [q for q in self.values() if isinstance(q,Question)]
          
    def answer(self):
        self.update(prompt(self.unanswered))

    def read_yaml(self, name:str or Path):
        self.update((Path / name).read_text(),Loader=FullLoader)
     
    def to_yaml(self,name:str):
        dump(self,Path(name).write_text())
        
messages = ["What would you like to ask?",
            "What is the type?",
            "What is the name?"]
types = [qt.Input, qt.List,qt.Input]
names = ['message', 'type', 'name']

what_to_ask = Answers([Question(*mtn) for mtn in zip(messages,types,names)])


def ask(answers:('answer yaml file','optional','a') = ''):
    "Ask Questions"
    answers = answers if answers else Answers(what_to_ask)
    answers.answer()
    

if __name__ == '__main__':
    plac.call(ask)

@ask @choices
Feature: choices object 

    Choices should be a Magic_dict, that takes a Question_Type and iterable which are the choices.
    If Question_Type Expand or CheckBox then choices need to be a dict, and if its Expand key needs
    to be in dict. There should also be a validate function to ensure this.
  
  Background:
    Given logging level is debug
    And context object is Choices

  Scenario: Choices(qt.List,["foo","bar"]) 
    Given input is qt.List, ["foo","bar"]
     When context object is created
     Then context object should be instance_of Magic_dict
     And context object.validate should be True

  Scenario: Choices(qt.CheckBox, {'foo': 'bar'})
    Given input is qt.Expand, {'foo' : 'bar'}
     When context object is created
     Then context object.foo should be 'bar' 
     And context object.validate should be True
     And context object.choices should be instance_of dict

  Scenario: Choices(qt.CheckBox, ['foo'])
    Given input is qt.CheckBox, ['foo']
     When context object is created
     Then context context should throw AssertionError 
     Then context object.validate should False
  
  Scenario: Choices(qt.Expand, {'key': 'foo', 'bar':'42'})
    Given input is qt.Expand, {'key': 'foo', 'bar':'42'}
     When context object is created
     Then context object.key should be 'foo' 
     Then context object.bar should be '42' 
     And context object.validate should be True
     And context object.choices should be instance_of dict

  Scenario: Choices(qt.Expand, {'ke': 'foo', 'bar':'42'})
    Given input is qt.Expand, {'ke': 'foo', 'bar':'42'}
     When context object is created
     Then context context should throw AssertionError 
     Then context object.validate should False
  
  Scenario: Choices(qt.Expand, ['foo'])
    Given input is qt.Expand, ['foo']
     When context object is created
     Then context context should throw AssertionError 
     Then context object.validate should False
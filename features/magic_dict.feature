@magic_dict
Feature: the implementation of magic_dict
    magic_dict is a dict that keys can be access as members
    plus a few extra features. The idea is that magic_dict can 
    be attached to objects, and can be give properties through composition.
    so let foo be an object. bar = Magic_dict(foo,_chain=[True]) creates a wrapper object of 
    type Magic_dict named bar. As a dict bar['key'] = value, will set a key to 
    value, but bar.key will return value. Magic_dict is also callable
    so bar() will return foo unless foo itself callable and _chain is True
    foo(*args,**kwargs). _chain default is True. Let DNE not be in foo. 
    foo['DNE'] and foo.DNE should return Magic_dict(). foo['DNE.bob'] = 42 and 
    foo.DNE.bob = 42 should set 42 to DNE.bob and DNE['bob'] which can be called through
    foo

  Background:
    Given log level is set to debug 
    Given this setup 

  Scenario: input is None: default behavior
    Given foo is Magic_dict()
     Then foo is instance of Magic_dict

     When foo["bar"] is 42
     Then foo.bar() is 42

     When foo.bar is 137
     Then foo["bar"]() is this.foo.bar()

  Scenario: foo= Magic_dict() and foo[]
    Given foo is Magic_dict()
    When foo['bar.hey'] is 42
    Then foo.bar.hey() is 42
  
  Scenario: bar is not in foo, foo['bar'] and  returns Magic_dict() 
    Given foo is Magic_dict()
    And bar not in foo
     When value is this.foo['bar']
     Then value is instance of Magic_dict
     And foo.bar() is None
  
  Scenario:foo(42) 
    Given foo is Magic_dict(42)
     Then foo() is 42
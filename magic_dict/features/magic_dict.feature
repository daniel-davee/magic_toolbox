@magic_dict
Feature: the implementation of magic_dict
    magic_dict is a dict that keys can be access as members
    plus a few extra features. The idea is that magic_dict can 
    be attached to objects, and can be give properties through composition.
    so let foo be an object. bar = Magic_dict(foo,_chain=[True]) creates a wrapper object of 
    type Magic_dict named bar. As a dict bar['key'] = value, will set a key to 
    this value, but bar.key will return value. Magic_dict is also callable
    so bar() will return foo unless foo itself callable and _chain is True
    foo(*args,**kwargs). _chain default is True. Let DNE not be in foo. 
    foo['DNE'] and foo.DNE should return Magic_dict(). foo['DNE.bob'] = 42 and 
    foo.DNE.bob = 42 should set 42 to DNE.bob and DNE['bob'] which can be called through
    foo

  Background: Setup test obj foo
    Given log level is set to info 
    Given foo is testing Magic_dict

  Scenario: input is None: default behavior
    Given foo is created
     When foo exist 
     Then result is True as bool
     And foo is isinstance of Magic_dict
     Given foo.bar = 42 as int
     When result is foo["bar"]
     Then result is 42 as int
     Given foo["bar"] = 137 as int
     When result is foo.bar
     Then result is 137 as int

  Scenario: bar is not in foo, foo['bar'] returns Magic_dict() 
    Given foo is created
    And bar not in foo
     When result is foo["bar"]
     Then result is isinstance of Magic_dict

  Scenario: foo does not have attr bar, foo.bar returns Magic_dict() 
    Given foo is created
    And foo does not have attr bar
     When result is foo.bar
     Then result is is instance of Magic_dict
  
  Scenario:foo 
    Given input is 42 as int
    And foo is created
     When result is foo()
     Then result is 42 as int








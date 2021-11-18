@ask @main
Feature: ask as a tool and a lib

    ask will allow you to ask questions and give answers.
    It should be accessable though magic_toolbox.
    1. Define Question_Type

    2. Define Choices 
    3. Define Question
    
        properties = {'message','type','name', #must be define for all questons
                      'choices',# need from expand, confirm, checkbox, list, and rawlist
                      'default','filter','eargs', 'validate'}
    magic_toolbox ask what would you like ask should ask you type and the name
    then create a question(msg="What would you like ask", type=type,name=name)= name : {type:type, msg:msg}
    magic_toolbox ask should ask msg="What would you like ask" type=type name =name
    question = name : {msg,type}

  Background:
    Given 

  Scenario: 
    Given 
     When 
     Then 


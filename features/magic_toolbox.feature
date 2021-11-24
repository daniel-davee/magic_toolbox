@magic_toolbox@cli
Feature:Magic Toolbox CLI; A toolbox management tool written in python
  #TODO the will be a lib verision which will allow you to manage
  #Includes more dynamically, but I need to flesh out how I want to work

  Magic Toolbox CLI will be a tool that will allow create a custom toolbox folder
  with symbolic links to python util packages kept in local repo or if they CLI they
  can be access through magic_toolbox [OPTION] TOOLNAME [OPTION] args. 
  
  magic_toolbox add toolname: will create toolbox folder if toolbox folder DNE. Then it checks if
  toolname references a tool in magic_toolbox; if yes then create a symbolic link in toolbox
  to tool folder, if not raise an error. If mtb.yml DNE create mtb.yml, and saving settings and
  tools.

  then python scripts in that folder should be able to import the package 
  
  magic_toolbox remove toolname: will check if toolname references a tool in toolbox; if yes
  unlink and remove reference from mtb.yml else raise an error.

  then there should not be a link in toolbox

  magic_toolbox init will create a toolbox and loud default_tools of the MTB object and create mtb.yml 
  to reflect this.

    Background:
    #can be used to change the log level
    Given log level is set to info 
     And magic_toolox.py is installed  
     And safe_rm is False as bool
  
  Scenario: magic_toolbox add ask
    # When run cmd ./magic_toolbox.py add ask
    When run cmd magic_toolbox add ask
     Then ./tool_box/mtb.yml exist
     And ./tool_box/__init__.py exist
     And ./tool_box/ask exist
@magic_toolbox@cli
Feature:Magic Toolbox CLI; A toolbox management tool written in python
  magic_toolbox init [dir=.] : if __init__.py does not exist in dir, 
  this will create, then it will append to the end of the file code 
  that will add magic_toolbox to you python path.
  magic_toolbox add [dir=., copy=False]: runs init adds a sym_link of dir, in 
  magic_toolbox directory, if copy it will do a full copy. 
    Background:
    #can be used to change the log level
    Given log level is set to debug 
     And magic_toolbox has ben installed
     And reset is run_cmd('rm -rf ~/temp')
   
  Scenario: magic_toolbox init
    # When run cmd ./magic_toolbox.py add ask
    Given target is (Path.home()/'temp')
    And tool_box is this.target() / 'tool_box'
    And init is this.tool_box() / '__init__.py'
    And mwd is str(mwd)
    And op is this.target().mkdir()
    And cmd is f"magic_toolbox init {str(this.target())}"
    When run is run_cmd(this.cmd())
    And exists is this.init().exists()
    And cat is run_cmd('cat ~/temp/tool_box/__init__.py')
    Then exists is True
    Then mwd in this.cat()
    Given reset is run_cmd('rm -rf ~/temp')
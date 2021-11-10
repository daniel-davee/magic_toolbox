# Magic Toolbox
A magic toolbox to hold all your tools you use, with few tools included.
But this will allow to create a local directory named tool_box,
then create symbolic to the package in the toolbox directory. This way for
small utils you use but don't want to turn into a pypy package but you're tried of copying over
can easily be added to any project. For more information at the feature files in features direcory.

## Install

    1. pip install -r requirements.txt
    2. behave

Step 1 installs the requirements in requirements.txt.
Step 2 uses behave framwork to install and test build

## Usage

    - magic_toolbox -h : prints help message
    - magic_toolbox add tool_name : will add a tool_name
    - magic_toolbox init : create toolbox and mtb.yml

## Todo

    [] define mtb.yml structure
    [] add an __init__.py to toolbox
    [] implement list and remove



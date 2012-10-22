# Readme
This is my personalalization of the awesome editor which is [Sublime Text](http://www.sublimetext.com/). These include: 

## Open Command window here
file opencmd.py takes care of this. It provides a right click menu for any file you are editing saying ***Open Command Window here***. clicking that opens up a command window in the current directory of the file.

## Codechef specific Modifications
These modifications are specific to codechef c++ programmers.
### Build system
see codechef/codechef_c++.sublime-build. This adds a codechef specific build system to your sublime text. to use this build system for C++, use tools->build system->codechef_c++. make sure that:
* You have g++ in your path. I recommend installing dev-c++ and adding C:\Dev-Cpp\bin to your path. 
* You have an input file(txt) with the same base name as your cpp file. so if your cpp file is my.cpp then the there should be a my.txt file in the same directory
* The full path to your cpp file does not have any spaces.

### Snippet
see codechef/codechef_c++.sublime-snippet. This adds a new snippet for your cpp files. To use this
1. create a new .cpp file. 
2. type codechef, you will see a dropdown, press enter on that
3. use `tab` and `shift+tab` to navigate back and forth. 
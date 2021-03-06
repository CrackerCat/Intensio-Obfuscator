# Intensio-Obfuscator (Beta)

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.1-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Takes a python source code and transform it into an obfuscated python code, replace name of variables/classes/functions to random chars and defined length, removes comments, line breaks and add to each line a random script with an always differents values.

## Requirement
- Python >= 3.5

## Files supported
- Files written in python 2.x and 3.x 

## Installation
`git clone https://github.com/Hnfull/Intensio-Obfuscator.git`

`cd Intensio-Obfuscator/intensio/` 

## Features
| Features | Descriptions |
| ------ | ------ |
| Replace | Replace all names of variables/classes/functions defined and remove all line breaks |
| Padding | Add random scripts after each line and remove all line breaks |
| Remove | Remove all commentaries and all line breaks |
| Mixer lower | Generate words with 32 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified |
| Mixer medium | Generate words with 64 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified|
| Mixer high | Generate words with 128 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified |

## Usages
| Parameters | Descriptions |
| ------ | ------ |
| -h, --help | show this help message and exit |
| -f, --onefile | if only one file |
| -d, --multiplefiles | if multiple files (project) |
| -i, --input  | source file or directory - if multiple files indicate a directory that contain all your files |
| -c, --code | language used in input file or directory, default value: [python], possible value: [python] |
| -o, --output | output file or directory that will be obfuscated - if multiple file indicate a empty directory that will contain all your files |
| -m, --mixer | length levels of the number of characters  for output variables /classes/functions, default value: [medium], possible values: [lower, medium, high] |
| -r, --replace | activate the 'replace' obfuscation feature |
| -p, --padding | activate the 'padding' obfuscation feature |
| -rm, --remove | activate the 'remove' obfuscation feature |

- If you want exclude python variables/classes/functions which will be taken by the 'replace' feature, edit `intensio/exclude_python_words.txt`
- If you want to include python variables/classes/functions that are not included when launching the 'replace' feature, edit `intensio/include_python_words.txt`

## Examples
#### Python target file(s):
- Multiple files basic: 
    - `python3.x intensio_obfuscator.py -d -i test/python/multiplefiles/basic/input/basicRAT -c python -o test/python/multiplefiles/basic/output/basicRAT -m lower -r -rm`
        - [source directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/basic/input/basicRAT)
        - [output directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/basic/output/basicRAT)
- Multiple files advanced: 
    - `python3.x intensio_obfuscator.py -d -i test/python/multiplefiles/advanced/input/basicRAT -c python -o test/python/multiplefiles/advanced/output/basicRAT -m high -r -p -rm`
        - [source directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/advanced/input/basicRAT)
        - [output directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/advanced/output/basicRAT)

- One files basic and advanced :
    - The command is same that for multiple file, just do not pointed a directory but a python file directly for `-i` and `-o` parameters, then change `-d` parameter into `-f` parameter

## Possible malfunctions

- **Do not define identically your names of local variables/classes/functions to python keywords or names of functions/classes of imported python libraries !**
- If a variable/class/function has an identical name with a word between `' '` or `" "` in `print()` function, your text will have the same value that the mixer variables/class/function.
-  If a variable/class/function has an identical name with a word  in after `#` (commentary) your text will have the same value that the mixer variables - class - function, but if between `"""` or `'''` without  a variables before, no replacing is performed.
- If you named your variables/classes - functions in the same way as python keywords or  names of functions/class of imported python libraries, an error may appear. Edit `intensio/excluded_python_words.txt` to add the variables not to obfuscate or change your names of local variables/classes - fuctions, if your variables/classes - functions  have the same name as a keyword it, he will be obfuscated and errors will appear.

## Todo
- Version 1.0.1-x:
    - Code optimization
    - Fix bugs and problems
    - Improved features already present
    
- Version 1.1.0:
    - Support files written in C
    
- Version 1.2.0:
    - Support files written in C++

## License
- MIT

## Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided

# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob

from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Remove:
    def __init__(self):
        self.utils = Utils()

    def LineBreaks(self, oneFileArg, codeArg, outputArg):
        checkLine       = 0
        numberFiles     = 0
        numberFileGood  = 0
        
        ######################################### One file only #########################################
        
        if oneFileArg:
            # -- Delete line breaks -- #
            with fileinput.FileInput(outputArg, inplace=True) as inputFile:
                for line in inputFile:
                    if line.strip():
                        print(line.rstrip())

            # -- Check if all line breaks are deleted -- #
            with open(outputArg, "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    if eachLine == "\n":
                        checkLine += 1
                    if checkLine == 0:
                        return EXIT_SUCCESS
                    else:
                        return EXIT_FAILURE

        ######################################### Multiple files #########################################

        else:
            if codeArg == "python":
                inputExt    = "py"
                blockdirs   = r"__pycache__"

            recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]

            # -- Delete line breaks -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with fileinput.FileInput(output, inplace=True) as inputFile:
                        for line in inputFile:
                            if line.strip():
                                print(line.rstrip())

            # -- Check if all line breaks are deleted -- #
            for output in recursFiles:
                checkLine = 0 # Initialize check vars for the next file 

                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            if eachLine == "\n":
                                checkLine += 1
                            if checkLine == 0:
                                numberFileGood += 1
                                numberFiles     += 1
                            else:
                                numberFileGood += 0
                                numberFiles     += 1
                        
            if numberFileGood == numberFiles:
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE

    def Commentaries(self, oneFileArg, codeArg, outputArg):
        countLineOutput = 0
        countLineInput  = 0
        noCommentary    = 0
        isCommentary    = 0

        if codeArg == "python":
            classicCommentariesDefine       = r"\#+.*"                      # begin '#' and begin code then '#'
            quoteOfCommentariesMultipleLine = r"^[\"\']+"                   # """ and ''' without before variables and if commentaries is over multiple lines
            quoteOfCommentariesOneLine      = r"[\"\']{3}.*[\"\']{3}"       # """ and ''' without before variables and if commentary is over one line, (""" commentaries """)
            noQuoteOfCommentaries           = r"\w+\s*\={1}\s*[\"\']{3}"    # """ and ''' with before variables

        print("############### [ Commentaries ] ###############\n")

        print("\n[+] Running commentaries remove...\n")

        ######################################### One file only #########################################

        if oneFileArg:
            # -- Count commentaries will be removed -- #
            with open(outputArg, "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    search = re.search(classicCommentariesDefine, eachLine)
                    if codeArg == "python":
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                            
                        if re.match(noQuoteOfCommentaries, eachLine):
                            noCommentary += 1
                        elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                            isCommentary += 1
                        else:
                            pass

                        if isCommentary == 1 and noCommentary == 0:
                            if re.match(quoteOfCommentariesOneLine, eachLine):
                                isCommentary    = 0
                                countLineInput  += 1
                                continue
                            countLineInput += 1
                            continue
                        elif isCommentary == 0 and noCommentary == 1:
                            continue
                        elif isCommentary == 2:
                            isCommentary    = 0
                            countLineInput  += 1
                            continue
                        elif isCommentary == 1 and noCommentary == 1:
                            isCommentary = 0
                            noCommentary = 0
                            continue
                        else:
                            pass

                    if search is not None:
                        countLineInput += 1
                    
            # -- Remove commentaries -- #
            with fileinput.input(outputArg, inplace=True) as inputFile:
                for eachLine in inputFile:
                    search = re.search(classicCommentariesDefine, eachLine)
                    if codeArg == "python":
                        if "coding" in eachLine or "#!" in eachLine:
                            print(eachLine)
                            continue

                        if re.match(noQuoteOfCommentaries, eachLine):
                            noCommentary += 1
                        elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                            isCommentary += 1
                        else:
                            pass

                        if isCommentary == 1 and noCommentary == 0:
                            if re.match(quoteOfCommentariesOneLine, eachLine):
                                isCommentary = 0
                                continue
                            continue
                        elif isCommentary == 0 and noCommentary == 1:
                            print(eachLine)
                            continue
                        elif isCommentary == 2:
                            isCommentary = 0
                            continue
                        elif isCommentary == 1 and noCommentary == 1:
                            isCommentary = 0
                            noCommentary = 0
                            print(eachLine)
                            continue
                        else:
                            pass

                    if search is not None:
                        eachLine = eachLine.replace(search.group(0), "")
                        print(eachLine)
                    else:
                        print(eachLine)

            # -- Check if all commentaries are removed -- #
            with open(outputArg, "r") as readFile:
                countLineOutput = 0
                readF           = readFile.readlines()

                for eachLine in readF:
                    search = re.search(classicCommentariesDefine, eachLine)
                    if codeArg == "python":
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                        
                        if re.match(noQuoteOfCommentaries, eachLine):
                            noCommentary += 1
                        elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                            isCommentary += 1
                        else:
                            pass

                        if isCommentary == 1 and noCommentary == 0:
                            if re.match(quoteOfCommentariesOneLine, eachLine):
                                isCommentary = 0
                                countLineOutput += 1
                                continue
                            countLineOutput += 1
                            continue
                        elif isCommentary == 0 and noCommentary == 1:
                            continue
                        elif isCommentary == 2:
                            isCommentary = 0
                            countLineOutput += 1
                            continue
                        elif isCommentary == 1 and noCommentary == 1:
                            isCommentary = 0
                            noCommentary = 0
                            continue
                        else:
                            pass

                    if search is not None:
                        countLineOutput += 1

            if countLineOutput == 0:
                print("-> {0} lines of commentaries removed\n".format(countLineInput))
                if (Remove.LineBreaks(self, oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE

        ######################################### Multiple files #########################################

        else:
            if codeArg == "python": 
                inputExt    = "py"
                blockdirs   = r"__pycache__"

            recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]

            # -- Count commentaries will be removed -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            search = re.search(classicCommentariesDefine, eachLine)
                            if codeArg == "python":
                                if "coding" in eachLine or "#!" in eachLine:
                                    continue
                                
                                if re.match(noQuoteOfCommentaries, eachLine):
                                    noCommentary += 1
                                elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                                    isCommentary += 1
                                else:
                                    pass

                                if isCommentary == 1 and noCommentary == 0:
                                    if re.match(quoteOfCommentariesOneLine, eachLine):
                                        isCommentary    = 0
                                        countLineInput  += 1
                                        continue
                                    countLineInput += 1
                                    continue
                                elif isCommentary == 0 and noCommentary == 1:
                                    continue
                                elif isCommentary == 2:
                                    isCommentary    = 0
                                    countLineInput  += 1
                                    continue
                                elif isCommentary == 1 and noCommentary == 1:
                                    isCommentary = 0
                                    noCommentary = 0
                                    continue
                                else:
                                    pass

                            if search is not None:
                                countLineInput += 1
                            
            # -- Remove commentaries -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    # -- Remove commentaries -- #
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            search = re.search(classicCommentariesDefine, eachLine)
                            if codeArg == "python":
                                if "coding" in eachLine or "#!" in eachLine:
                                    print(eachLine.rstrip())
                                    continue
                                
                                if re.match(noQuoteOfCommentaries, eachLine):
                                    noCommentary += 1
                                elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                                    isCommentary += 1
                                else:
                                    pass

                                if isCommentary == 1 and noCommentary == 0:
                                    if re.match(quoteOfCommentariesOneLine, eachLine):
                                        isCommentary = 0
                                        continue
                                    continue
                                elif isCommentary == 0 and noCommentary == 1:
                                    print(eachLine)
                                    continue
                                elif isCommentary == 2:
                                    isCommentary = 0
                                    continue
                                elif isCommentary == 1 and noCommentary == 1:
                                    isCommentary = 0
                                    noCommentary = 0
                                    print(eachLine)
                                    continue
                                else:
                                    pass
                            
                            if search is not None:
                                eachLine = eachLine.replace(search.group(0), "") # Util if line containt code and then '#'. (currently commentary)
                                print(eachLine)
                            else:
                                print(eachLine)

            # -- Check if all commentaries are removed -- #
            for output in recursFiles:
                countLineOutput = 0

                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        countLineOutput = 0
                        readF           = readFile.readlines()

                        for eachLine in readF:
                            search = re.search(classicCommentariesDefine, eachLine)
                            if codeArg == "python":
                                if "coding" in eachLine or "#!" in eachLine:
                                    continue
                                
                                if re.match(noQuoteOfCommentaries, eachLine):
                                    noCommentary += 1
                                elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                                    isCommentary += 1
                                else:
                                    pass

                                if isCommentary == 1 and noCommentary == 0:
                                    if re.match(quoteOfCommentariesOneLine, eachLine):
                                        isCommentary = 0
                                        countLineOutput += 1
                                        continue
                                    countLineOutput += 1
                                    continue
                                elif isCommentary == 0 and noCommentary == 1:
                                    continue
                                elif isCommentary == 2:
                                    isCommentary = 0
                                    countLineOutput += 1
                                    continue
                                elif isCommentary == 1 and noCommentary == 1:
                                    isCommentary = 0
                                    noCommentary = 0
                                    continue
                                else:
                                    pass

                            if search is not None:
                                countLineOutput += 1

            if countLineOutput == 0:
                print("-> {0} lines of commentaries removed\n".format(countLineInput))
                if (Remove.LineBreaks(self, oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE
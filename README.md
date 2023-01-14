# How to install PyQt Designer with PyCharm
1. Go to C:\Users\YOUR_NAME\AppData\Local\Programs\Python (or wherever your python is installed).
2. Right click -> open terminal here.
3. Put command: pip install pyqt5.
4. Put command: pip install pyqt5-tools.
5. If after this command an error occurs don't worry - just leave it.
6. Install PyCharm.
7. Install PyQt Designer from: https://build-system.fman.io/qt-designer-download. Remember where it is installed!
8. Open PyCharm.
9. At the top go to: File -> Settings -> Project: NAME -> Project Interpreter.
10. Make sure there is your python interpreter putted there.
11. Click on the "+".
12. Find and install (if not already installed): pyqt5, pyqt5-sip, pyqt5-tools.
13. If an error occurred with the tools - ignore that.
14. Stay in settings and go to Tools -> External Tools -> Click on "+".
15. Name: "QTdesigner"
16. Group: "External Tools"
17. Program: Find and add the designer.exe here
18. Working directory: $ProjectFileDir$
19. Click OK
20. Click on the "+" again
21. Name: "PyUIC"
22. Group: "External Tools"
23. Program: Find and add the python.exe here
24. Arguments: -m PyQt5.uic.pyuic -x $FileName$ -o $FileNameWithoutExtension$.py
25. Working directory: $ProjectFileDir$

# How to use above tools
1. At the top go to Tools -> External Tools -> QTdesigner to open designer
2. Do the work there
3. Save file
4. Go back to PyCharm
5. There should be a file xxxx.ui. If not try to refresh.
6. Right click on it -> External Tools -> PyUIC, to generate the code
7. The file xxxx.py should be generated
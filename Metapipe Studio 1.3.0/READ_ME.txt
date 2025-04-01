#1 - If you have previous version, move files to somewherelse

#2 - Now Maya 2022 and 2023 uses same DNA Calibartion. Install DNA_Calibration 1.1.0 (https://github.com/EpicGames/MetaHuman-DNA-Calibration/archive/refs/tags/1.1.0.zip) Extract the files to C Drive and rename Main folder as dna_calibration.

#3 - Go to downloaded folder and type "cmd" in textfield. Control Panel will pop up

Write "python metapipe.py"



OR if it not works or prefer other solution


- Copy all python files and paste in to "c:/Arts and Spells/Scripts" (Recommended).

- Open "MetaPipeStudioSource.py" and change to your versions of

* ROOT_DIR
* MAYA_VERSION
* dnaPath
* body_type

- After changing those save the file as "dat.py" inside "c:/Arts and Spells/Scripts"




#4 - "Documents\Megascans Library\support\plugins\maya\7.0\MSLiveLink\DHI\plugins\Windows\2023" (7.0 is current MSLiveLink Version it may change)  Go to this path and copy embeddedRL4.mll file

#5 - Create a folder named "plug-ins" in "Documents/Megascans Library/support/plugins/maya/7.0/MSLiveLink/" and past the file inside it.

#6 - Follow tutorials for usage

#7 - If you have any question, feel free to ask form Discord or Artstation! Enjoy!


Body Build Automatic Code:
#


import sys

sys.path.append("c:/Arts and Spells/Scripts")
import Body_Prep
Body_Prep.run()


#

Metapipe Shelf Editor Code:
#


import sys

sys.path.append("c:/Arts and Spells/Scripts")
import MetaPipeStudio
MetaPipeStudio.show_dna_edit_window()


#




Corrective Blendshape Installation:

#1 - Copy extractDerltas.py and paste it in to Maya Plugins folder --> documents/maya/"""2023/2022"""/plug-ins
#2 - Copy the text that inside correctiveBlendshape.txt file and paste it in to Maya Shelf Editor "MEL SCRIPT TAB"
#3 - Enable extractDeltas plugin inside Maya - Windows - Settings and Preferences - Plugin Manager
#4 - Copy paste bsIndex.py file to C:/Arts and Spells/Scripts (Recommended) or change the code correctiveBlendshape inside Shelf Editor and set your path.



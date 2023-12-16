from metrics import *


files = getFileList()

for file in files :
    eval = Evaluation(file)
    print(file)
    eval.do_evaluation()

from pyAudioAnalysis import audioTrainTest as aT

myList = ['Austin/a','Austin/b','Austin/c','Austin/d','Austin/e','Austin/f','Austin/g','Austin/h','Austin/i','Austin/j','Austin/k','Austin/l','Austin/m','Austin/have','Austin/in','Austin/that','Austin/the',"Austin/toNew",'Austin/u','Austin/n']
aT.featureAndTrain(myList, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'svm', 'svm', False)
def classify(classifier,myFile):

    print aT.fileClassification(myFile,classifier,classifier)

    # print aT.fileClassification("Austin/a1.wav", classifier, classifier)
    # print aT.fileClassification("Austin/f1.wav", classifier,classifier)
    # print aT.fileClassification("Austin/h1.wav", classifier,classifier)
    # print aT.fileClassification("Austin/u1.wav", classifier,classifier)
    # print aT.fileClassification("Austin/c1.wav", classifier,classifier)

def classifyFile(myFile):
    print aT.fileClassification(myFile, 'svm', 'svm')

# classifiers = ["svm"]
# for classifier in classifiers:
#     classify(classifier)
#classify('svm')
listOfThings = ['Austin/a8.wav','Austin/bTest.wav','Austin/cTest.wav','Austin/dTest.wav','Austin/eTest.wav','Austin/f5.wav','Austin/gTest.wav','Austin/h5.wav','Austin/iTest.wav','Austin/jTest.wav','Austin/kTest.wav','Austin/lTest.wav','Austin/mTest.wav','Austin/a8.wav']
for test in listOfThings:
    classify('svm',test)

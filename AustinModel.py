from pyAudioAnalysis import audioTrainTest as aT

myList = ['Austin/n','Austin/a','Austin/and','Austin/be','Austin/c','Austin/f','Austin/h','Austin/have','Austin/in','Austin/that','Austin/the',"Austin/toNew",'Austin/u']
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
listOfThings = ['Austin/n2.wav','Austin/a8.wav','Austin/and.wav','Austin/beTest.wav','Austin/c5.wav','Austin/f5.wav','Austin/h5.wav','Austin/have5.wav','Austin/in5.wav','Austin/that5.wav','Austin/the5.wav',"Austin/to5.wav",'Austin/u5.wav']
for test in listOfThings:
    classify('svm',test)

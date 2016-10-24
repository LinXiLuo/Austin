from pyAudioAnalysis import audioTrainTest as aT

def classify(classifier,myFile):
    myList = ['Austin/a',"Austin/and","Austin/be","Austin/c","Austin/f","Austin/h","Austin/have","Austin/in","Austin/n","Austin/that","Austin/the","Austin/toNew","Austin/u"]
    aT.featureAndTrain(myList, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, classifier, classifier, False)
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
classify('svm', 'Austin/and.wav')

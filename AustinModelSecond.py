from pyAudioAnalysis import audioTrainTest as aT

myList = ['Austin/a','Austin/b','Austin/c','Austin/d','Austin/e','Austin/f','Austin/g','Austin/h','Austin/i','Austin/j','Austin/k','Austin/l','Austin/m','Austin/have','Austin/in','Austin/that','Austin/the',"Austin/toNew",'Austin/u','Austin/n']
aT.featureAndTrain(myList, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'svm', 'svm', False)
def classify(classifier,myFile):
    [result, p, classNames] = aT.fileClassification(myFile,classifier,classifier)
    print result
    print p
    print classNames
    maxI = maxIndex(p)
    return classNames[maxI]
    #print aT.fileClassification(myFile,classifier,classifier)

    # print aT.fileClassification("Austin/a1.wav", classifier, classifier)
    # print aT.fileClassification("Austin/f1.wav", classifier,classifier)
    # print aT.fileClassification("Austin/h1.wav", classifier,classifier)
    # print aT.fileClassification("Austin/u1.wav", classifier,classifier)
    # print aT.fileClassification("Austin/c1.wav", classifier,classifier)
def maxIndex(a):
    i = 0
    maxInd = 0
    maxProb = 0
    for element in a:
        if element > maxProb:
            maxInd = i
            maxProb = element
        i = i + 1
    return maxInd
def classifyFile(myFile):
    print aT.fileClassification(myFile, 'svm', 'svm')

# classifiers = ["svm"]
# for classifier in classifiers:
#     classify(classifier)
#classify('svm')
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a']
listOfThings = ['Austin/a8.wav','Austin/bTest.wav','Austin/cTest.wav','Austin/dTest.wav','Austin/eTest.wav','Austin/f5.wav','Austin/gTest.wav','Austin/h5.wav','Austin/iTest.wav','Austin/jTest.wav','Austin/kTest.wav','Austin/lTest.wav','Austin/mTest.wav','Austin/a8.wav']
i = 0
correctItems = 0
incorrectItems = 0
for test in listOfThings:
    lab = classify('svm',test)
    if lab == labels[i]:
        correctItems = correctItems + 1
    else:
        incorrectItems = incorrectItems + 1
    i = i + 1
accuracy = correctItems*100.0 / (correctItems+incorrectItems)
print accuracy


from pydub import AudioSegment
from pydub.silence import split_on_silence
#song = AudioSegment.from_wav("Austin/Word Recordings.wav")

listOfLetters = ['b','c','d','e','f','g','h','i','j','k','l','m']

for letter in listOfLetters:
    song = AudioSegment.from_wav("Austin/"+letter+'.wav')
    chunks = split_on_silence(song,
    # must be silent for at least half a second
        min_silence_len=300,

    # consider it silent if quieter than -16 dBFS
        silence_thresh=-45
    )
    for i,chunk in enumerate(chunks):
        #print len(chunks)
        #print letter
        #print letter+'/'+chunk+'{0}'+'.wav'.format(i)
        # print '{0}'
        # print '/Austin/'+letter
        # print '/Austin/'+letter+'/'
        # print chunk
        filePath = 'Austin/'+letter+'/'+'chunk'+str(i)+'.wav'
        #print filePath
        chunk.export(filePath.format(i), format="wav")

#
# song = AudioSegment.from_wav("Austin/b.wav")
# chunks = split_on_silence(song,
# # must be silent for at least half a second
#     min_silence_len=300,
#
# # consider it silent if quieter than -16 dBFS
#     silence_thresh=-45
# )
#
# for i,chunk in enumerate(chunks):
#     print len(chunks)
#     chunk.export("Austin/b/chunk{0}.wav".format(i), format="wav")

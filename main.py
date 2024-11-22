import re

import package.Language as Language
import package.LibraryClass as LibraryClass
import SentimentLang
from moviepy.editor import AudioFileClip
import wave, math, contextlib
import text2emotion as te
import shutil
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def getLanguage(argument):
    switcher  = {
        1: "id-ID",
        2: "en-US"
    }
    return switcher.get(argument,0)



def vtt():
    #variabel
    format_audio = ".wav"
    format_video = ".mp4"

    print("Please select type")
    print("1. Video")
    print("2. Audio")

    type = int(input('Enter a type : '))
    for case in LibraryClass.switch(type):
        if case(1):
            print("Enter Filename Video (.mp4) : ")
            Vpath = input()
            transcribed_audio_file_name = Vpath+format_audio
            video_file_name = Vpath+format_video

            audioclip = AudioFileClip(video_file_name)
            audioclip.write_audiofile(transcribed_audio_file_name)
            with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                total_duration = math.ceil(duration / 60)

            print("Please select language")
            print("1. INDONESIAN")
            print("2. ENGLISH")
            ##Convert Audio
            try:
                print("Select number : ")
                languageselection = getLanguage(LibraryClass.selection.getSelection(self=""))
                print(LibraryClass.bcolors.OKVIOLET + "Your was choice " + languageselection)

                text = Language.get_large_audio_transcription(transcribed_audio_file_name, languageselection,show_all=True)
                #print("\nFull text:", text)
                te.get_emotion(text)
                #print(te.get_emotion(text))
                f = open("result.txt", "a")
                f.write('\n')
                f.write('=======Emotion===========')
                f.write('\n')
                f.write('%s\n' % te.get_emotion(text))
                f.close()
            except:
                print("An exception occurred")

            break
        if case(2):
            print("Please select language")
            print("1. INDONESIAN")
            print("2. ENGLISH")
            try:
                print("Select number : ")
                languageselection = getLanguage(LibraryClass.selection.getSelection(self=""))
                print(LibraryClass.bcolors.OKVIOLET + "Your was choice "+ languageselection)

                print("Enter Filename Audio ("+format_audio+") : ")
                path = input()
                text = Language.get_large_audio_transcription(path+format_audio,languageselection)
                #print("\nFull text:", text)

                #emotion
                # te.get_emotion(text)
                # print(te.get_emotion(text))

                # Sentence = [str(text)]
                # analyser = SentimentIntensityAnalyzer()
                # pos_word_list = []
                # neu_word_list = []
                # neg_word_list = []
                #
                #
                # for word in Sentence:
                #     if (analyser.polarity_scores(word)['compound']) >= 0.1:
                #         pos_word_list.append(word)
                #     elif (analyser.polarity_scores(word)['compound']) <= -0.1:
                #         neg_word_list.append(word)
                #     else:
                #         neu_word_list.append(word)
                #
                # print('Positive:', pos_word_list)
                # print('Neutral:', neu_word_list)
                # print('Negative:', neg_word_list)
                #
                # for i in Sentence:
                #     v = analyser.polarity_scores(i)
                #     print(v)

                f = open("result.txt", "a")
                f.write('\n')
                # f.write('=======Emotion===========')
                # f.write('\n')
                # f.write('%s\n' % te.get_emotion(text))
                f.close()

                #print(LibraryClass.word_count(text))

                #count word sentiment + -
                if languageselection == 'id-ID':
                    SentimentLang.ID_sentiment(re.sub(r'[^\w]', ' ', text))
                elif languageselection == 'en-US':
                    SentimentLang.EN_sentiment(re.sub(r'[^\w]', ' ', text))

            except:
                print("An exception occurred")
            break





#run
if __name__ == "__main__":
    #shutil.rmtree('audio-chunks') #delete all files in folder audio-chunks
    vtt()
    print('Process Complete')




#
# input1 = input('Enter your first number: ')
# input2 = input('Enter your second number: ')
#
# #sum
# sum = float(input1 ) + float(input2 )
#
# # output
# print('The sum of {0} and {1} is {2}'.format(input1 , input2 , sum))
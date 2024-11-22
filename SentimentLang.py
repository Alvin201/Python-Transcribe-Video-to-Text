import re

def ID_sentiment(str):
    # write to text
    f = open("result.txt", "a")
    f.write('\n')
    f.write('=======Sentiment Word===========')

    # break the string into list of words
    str = str.split()
    str2 = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)

    flag_pos = 'P'
    flag_neg = 'N'
    a = 0
    b = 0

    for i in range(0, len(str2)):
        with open("sentence/positive_ID.txt", encoding="utf-8") as file:
            word_positive = [l.rstrip("\n") for l in file]

        with open("sentence/negative_ID.txt", encoding="utf-8") as file:
            word_negative = [l.rstrip("\n") for l in file]

        y = ''.join(e for e in str2[i] if e.isalnum()).strip()

        if [ele for ele in word_positive if(ele in y)]:
        #if any(element in y for element in word_positive if(element in y)):
            count_y = str.count(y)
            # print('+',y,' : ' , count_y)
            if flag_pos == 'P':
                a += count_y

            # write data to text file
            f.write('\n' + '(positive) ' + y + ' : ' + '%d' % count_y)

        elif [ele for ele in word_negative if(ele in y)]:
        #elif any(element in y for element in word_negative if(element in y)):
            count_y = str.count(y)
            # print('-',y, ' : ', count_y)
            if flag_neg == 'N':
                b += count_y


        # write data to text file
            f.write('\n' + '(negative) ' + y + ' : ' + '%d' % count_y)

    f.write('\n')
    f.write('\n' + '=======TOTAL SENTIMENT=========')
    f.write('\n' + 'Positive Word : ' + '%d' % a)
    f.write('\n' + 'Negative Word : ' + '%d' % b)
    f.write('\n')
    f.close()


def EN_sentiment(str):
    # write to text
    f = open("result.txt", "a")
    f.write('\n')
    f.write('=======Sentiment Word===========')

    # break the string into list of words
    str = str.split()
    str2 = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)

    flag_pos = 'P'
    flag_neg = 'N'
    a = 0
    b = 0

    for i in range(0, len(str2)):
        with open("sentence/positive_EN.txt", encoding="utf-8") as file:
            word_positive = [l.rstrip("\n") for l in file]

        with open("sentence/negative_EN.txt", encoding="utf-8") as file:
            word_negative = [l.rstrip("\n") for l in file]

        y = ''.join(e for e in str2[i] if e.isalnum()).strip()
        if any(element in y for element in word_positive):
            count_y = str.count(y)
            # print('+',y,' : ' , count_y)
            if flag_pos == 'P':
                a += count_y

            # write data to text file
            f.write('\n' + '(positive) ' + y + ' : ' + '%d' % count_y)

        elif any(element in y for element in word_negative):
            count_y = str.count(y)
            # print('-',y, ' : ', count_y)
            if flag_neg == 'N':
                b += count_y

            # write data to text file
            f.write('\n' + '(negative) ' + y + ' : ' + '%d' % count_y)

    f.write('\n')
    f.write('\n' + '=======TOTAL SENTIMENT=========')
    f.write('\n' + 'Positive Word : ' + '%d' % a)
    f.write('\n' + 'Negative Word : ' + '%d' % b)
    f.write('\n')
    f.close()
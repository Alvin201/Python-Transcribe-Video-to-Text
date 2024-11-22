class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        #raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

class bcolors:
    OKBEIGE = '\033[93m'
    OKVIOLET = '\33[95m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class selection:
    def getSelection(self):
        while True:
            try:
                a = int(input())
                if (a < 1 or a > 3):
                    print('not number')
                    continue
            except ValueError:
                print('not number')
                continue
            else:
                return a
                break







# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts




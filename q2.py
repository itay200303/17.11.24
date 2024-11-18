#class
#Solution(object):


def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: None
    """
    words = s.strip().split()

    if words:
        print(len(words[-1]))
    else:
        print(0)
class SingleString:
    def __init__(self, s):
        self.string = s

    def maxPower(self):
        """
        Give a string s, and the "energy" of s is defined as
        the length of the longest non empty substring containing only one character.
        :return: The "energy" of s.
        """
        s_copy = self.string
        max_len = 0
        now_len = 0
        now_flag = 1
        s_copy = s_copy + " "
        for i in s_copy:
            if i == now_flag:
                now_len += 1
                continue
            else:
                if now_len > max_len:
                    max_len = now_len
                now_flag = i
                now_len = 1
        return max_len

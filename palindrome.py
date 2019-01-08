from dequeue import Dequeue

class PalindromeChecker:
    def __init__(self):
        self.dq = Dequeue()

    def check_if_palindrome(self, word):
        self.dq.items = list(word)
        is_palindrome = True
        while self.dq.size() > 1:
            first_letter = self.dq.remove_front()
            last_letter = self.dq.remove_rear()
            if first_letter != last_letter:
                is_palindrome = False
            
        return is_palindrome

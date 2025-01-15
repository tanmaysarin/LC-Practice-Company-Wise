# 1419. Minimum Number of Frogs Croaking
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/

# Solution 1
from collections import Counter

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        char_counter = Counter()
        prevs = {
            'c': 'k',
            'r': 'c',
            'o': 'r',
            'a': 'o',
            'k': 'a',
        }

        for ch in croakOfFrogs:
            prev_ch = prevs[ch]
            if char_counter[prev_ch] > 0:
                char_counter[prev_ch] -= 1
                char_counter[ch] += 1
            elif ch == 'c':
                char_counter[ch] += 1
            else:
                return -1
            
        for ch, val in char_counter.items():
            if ch != 'k' and val > 0:
                return -1

        return char_counter['k']

# Solution 2

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = max_frog_croak = present_frog_croak = 0

        for i, v in enumerate(croakOfFrogs):
            if v == 'c':
                c += 1
                present_frog_croak += 1
            elif v == 'r':
                r += 1
            elif v == 'o':
                o += 1
            elif v == 'a':
                a += 1
            elif v == 'k':
                k += 1
                present_frog_croak -= 1
                # 1 croak complete
            
            max_frog_croak = max(max_frog_croak, present_frog_croak)

            #if any inorder occurs:
            if c < r or r < o or o < a or a < k:
                return -1
        
        # if all good, else -1
        if present_frog_croak == 0 and c == r and r == o and o == a and a == k:
            return max_frog_croak
        
        return -1
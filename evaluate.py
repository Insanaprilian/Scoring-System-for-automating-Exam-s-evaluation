import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import seaborn as sns
import re

# increase display of columns in pandas
pd.set_option('display.max_colwidth', 200)
import os
import sys


class Evaluate:
    def __init__():
        self.ref_answer = None
        self.answer = None
        
        self.is_invalid = None
        self.is_match = None
        self.is_ordering = None
        self.is_aposthrope = None
    
    def is_invalid_case(self,tuples):
        self.ref_answer = tuples[-2]
        self.answer = tuples[-1]
        
        ref_answer = self.ref_answer.lower()
        answer = self.answer.lower()
        
        # using levesthein distance
        distances = np.zeros((len(ref_answer)+1, len(answer)+1))

        for t1 in range(len(ref_answer)+1):
            distances[t1][0] = t1

        for t2 in range(len(answer) + 1):
            distances[0][t2] = t2
        
        a = 0
        b = 0
        c = 0
        
        for t1 in range(1, len(ref_answer) + 1):
            for t2 in range(1, len(answer) + 1):
                if (ref_answer[t1-1] == answer[t2-1]):
                    distances[t1][t2] = distances[t1-1][t2-1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1-1][t2]
                    c = distances[t1-1][t2-1]

                if (a<=b and a<=c):
                    distances[t1][t2] = a+1
                elif (b<=a and b<=c):
                    distances[t1][t2] = b+1
                else:
                    distances[t1][t2] = c+1
                    
        # store distance of reference answer and answer
        result = int(distances[len(ref_answer),len(answer)])
        
        # rule for max distance tolerance to be incorrect answer
        if result>0:
            self.is_invalid = ('False', answer, "Invalid/not match answer")
        else:
            self.is_invalid = None
        
        return self.is_invalid
        
    def is_match_case(self,tuples):
        self.ref_answer = tuples[-2]
        self.answer = tuples[-1]
        
        # remove all special character(punctuation,whitespace)
        ref_answer = re.sub('[^A-Za-z0-9]+', '', self.ref_answer)
        answer = re.sub('[^A-Za-z0-9]+', '', self.answer)
        
        if ref_answer == answer:
            self.is_match = None
            
        else: self.is_match = ('Partially Correct', answer, 'Upper and Lower case')
            
        return self.is_match
    
    def is_ordering_case(self,tuples):
        self.ref_answer = tuples[-2]
        self.answer = tuples[-1]
        
        ref = re.sub('[^A-Za-z0-9 ]+', '', self.ref_answer).lower().split()
        
        ref_answer = re.sub('[^A-Za-z0-9 ]+', '', self.ref_answer).lower()
        answer = re.sub('[^A-Za-z0-9 ]+', '', self.answer).lower()
            
        for word in ref_answer:
            l = len(word)
                
    def is_aposthrope_case(self,tuples):
        self.ref_answer = tuples[-2]
        self.answer = tuples[-1]

        ref_answer = re.sub("[^A-Za-z0-9']+", "", self.ref_answer)
        answer = re.sub("[^A-Za-z0-9']+", "", self.answer)
        
        if ("'" in ref_answer) & ("'" not in answer):
            self.is_apostrophe = ('Partially Correct', answer, "apostrophe's absence from the answer")
        if ("'" not in ref_answer) & ("'" not in answer):
            self.is_aposthrope = ('Partially Correct', answer, 'excessive aposthrope')
        else: self.is_aposthrope = None
        
        return self.is_aposthrope


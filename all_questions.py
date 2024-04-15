import pytest
from all_questions import *
import pickle
import math


#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = None

    # type: float
    # Calculate the probability.
    answers['(b)'] = None

    # type: float
    # Calculate the probability.
    answers['(c)'] = None
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = math.log((1-p)/p)/2

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.667
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Although the classifiers are independent, the concept of ensemble methods apply to classifiers which have some predictive power, and hence can improve their performance over multiple classifiers, iff there is an error rate involved, not if it is a purely random chance without any learning from past data."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = None

    # type: eval_float
    answers['(a) C2-TPR'] = None

    # type: eval_float
    answers['(a) C1-FPR'] = None

    # type: eval_float
    answers['(a) C2-FPR'] = None

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = None

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = None

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = None

    # type: explain_string
    answers['(c) explain'] = None
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = None

    # type: explain_string
    answers['(i) Best classifier, explain'] = None

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = None

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = None

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = None

    # type: explain_string
    answers['(iii) best classifier, explain'] = None
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = 0.1

    # type: eval_float
    answers['(a) recall for C0'] = 0.5

    # type: eval_float
    answers['(b) F-measure of C0'] = 

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] =  "yes"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = None
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = ['recall':

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = None

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = None

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = None
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T1'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "I would prefer TPR/FPR over F1 score, because TPR/FPR is a better metric to identify patients who are or are not suffering from cancer. Our goal is not to get a better precision, but to get a better recall and also abetter specifity. So the trade-off is more between sensitivity and specificity, rather than sensitivity and precision. Thus, TPR/FPR is a better measure"

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "A case where F1 measure is important is where precision is important. That is the cost of a False positive is high. A situatuon where avoiding False positive is important, is invasive treatments for cancer, where it is important for the algorithm or model to detect where exactly the tumour lies, because if it detects a wrong area, it could end up being fatal."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)

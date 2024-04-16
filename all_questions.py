import pytest
from all_questions import *
import pickle
import math


#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.0020

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.0800
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
    answers['(a) C1-TPR'] = p

    # type: eval_float
    answers['(a) C2-TPR'] = 2 * p

    # type: eval_float
    answers['(a) C1-FPR'] = p

    # type: eval_float
    answers['(a) C2-FPR'] = 2 * p

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "no"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Since both the TPR and FPR are equal in both classifier, the AUROC is a straight line, meaning it performs no better than a random classifier. Thus neither is better classifier than the other."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "The relative performance depends on the ability to discern between the two classes, and how well they distinguish each other. When comparing against the random guess line, precision recall do not give much insights, they are a measure of how well the classifier avoids false negatives. A true performance of a classifier is given by its ability to classify better than a random classifier, and hence TPR/FPR is a better measure."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "It is very subjective and depends on the domain of the task. Since both the classifiers have the same precision and accuracy, it is imperative the task requires that the positive class is correctly classified, then the recall has to be high, in which case C2 should be chosen. However, if there is FPR should be as low as possible, then C1 should be chosen" 

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "the precision recall and F1 score gives a better measure of the actual performance of both the classifiers, because the TPR FPR provides a trade-off score, the FPR is lower for C1, which is good but does not mean it is good performance. F1 measure rather gives a true picture of how the classifiers perform."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3"

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C3 is the better classifier because of the precision, which is slightly better than the random classifier"
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = 0.1 * p

    # type: eval_float
    answers['(a) recall for C0'] = p

    # type: eval_float
    answers['(b) F-measure of C0'] = 2 * ((0.1 * p) / (0.1 + p))

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] =  "yes"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.825
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {'recall':0.533,'precision':0.6154,'F-measure':0.5714,'accuracy':0.88}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'accuracy'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'recall'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "In this specific use case, it is important to predict both the classes correctly, and hence accuracy is the best metric to gauge the performance of whether the weather is going to be sunshine or rainy. Also accuracy has given the best performance, which is a good enough metric for weather prediction. For the worst metric, Recall performs poorly, and it is not relevant to the task."
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

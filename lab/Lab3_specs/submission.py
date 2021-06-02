import pandas as pd

################# Question 1 #################

    
def multinomial_nb(training_data, sms):# do not change the heading of the function
    # **replace** this line with your code
    num_h = 0          #number of ham
    num_s = 0          #number of spam
    vocabulary = set() #set of all words in the file
    if type(sms) == str:       #convert sms to a list of words in sms if sms is in type 'str'
        sms = tokenize(sms)
    
    
    for i in range(len(training_data)):
        for j in training_data[i][0].keys():
            vocabulary.add(j)
    ham = {}
    spam = {}

    for v in vocabulary:     #initialize ham and spam with key = word, value = 0
        ham[v] = 0
        spam[v] = 0
        
    for i in range(len(training_data)):      #training_data[0]: a dict  training_data[1]: its label(ham or spam)
        if training_data[i][1] == 'ham':
            num_h += 1
            for key in training_data[i][0].keys():
                ham[key] += training_data[i][0][key]  #update the value in dict ham
        else:
            num_s += 1
            for key in training_data[i][0].keys():
                spam[key] += training_data[i][0][key]  #update the value in dict spam
    p_h = num_h / len(training_data)
    p_s = num_s / len(training_data)
    
    
    #smoothing
    sum_h = 0
    sum_s = 0
    for v in vocabulary:
        ham[v] += 1
        sum_h += ham[v]
        spam[v] += 1
        sum_s += spam[v]
    for v in vocabulary:
        ham[v] = ham[v] / sum_h
        spam[v] = spam[v] / sum_s
        
    
    
    words = set(sms)
    sms_dict = {}
    for word in words:
        sms_dict[word] = 0
    for word in sms:
        sms_dict[word] += 1

    
    p_ham = 1
    p_spam = 1
    for word in sms_dict.keys():
        if word in ham:
            p_ham *= ham[word] ** sms_dict[word]
        if word in spam:
            p_spam *=  spam[word] ** sms_dict[word]
                        

            
    h_p = p_ham * p_h
    s_p = p_spam * p_s

    #the ratio of the probability of sms is spam and the probability of sms is ham
    return s_p / h_p
    # A return value larger than 1 implies the sms is spam and vice versa

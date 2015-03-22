#!/usr/bin/env python
import math

# Split-point of age is 36, of salary is 51K, for information gain and gain
# ratio
data_input_array = [
        {"department":"sales", "status":"senior", "age":"31-35",
          "salary":"46k-50k"},
        {"department":"sales", "status":"junior", "age":"26-30",
          "salary":"26k-30k"},
        {"department":"sales", "status":"junior", "age":"31-35",
          "salary":"31k-35k"},
        {"department":"systems", "status":"junior", "age":"21-25",
          "salary":"46k-50k"},
        {"department":"systems", "status":"senior", "age":"31-35",
          "salary":"66k-70k"},
        {"department":"systems", "status":"junior", "age":"26-30",
          "salary":"46k-50k"},
        {"department":"systems", "status":"senior", "age":"41-45",
          "salary":"66k-70k"},
        {"department":"marketing", "status":"senior", "age":"36-40",
          "salary":"46k-50k"},
        {"department":"marketing", "status":"junior", "age":"31-35",
          "salary":"41k-45k"},
        {"department":"secretary", "status":"senior", "age":"46-50",
          "salary":"36k-40k"},
        {"department":"secretary", "status":"junior", "age":"26-30",
          "salary":"26k-30k"}
        ]

attributes_array = ["department", "status", "salary", "age"]

def majority_value(data, target_attr):
    dic = {}
    max_item = ""
    for record in data:
        dic[record[target_attr]] = dic.get(record[target_attr], 0) + 1
    counts = [(j,i) for i,j in dic.items()]
    count, max_item = max(counts)
    del dic
    return max_item

def entropy(data_input, target_attr):
    val_freq        = {}
    data_entropy    = 0.0
    data            = data_input[:]
    length          = len(data)
    for record in data:
        if(val_freq.has_key(record[target_attr])):
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]] = 1.0

    # Calculate the entropy
    for freq in val_freq.values():
        data_entropy += (-freq/length) * math.log(freq/length, 2)

    return data_entropy

def information_gain(data_input, attr, target_attr):
    """ Calculate the information gain, to determine next target attribute """
    val_freq        = {}
    subset_entropy  = 0.0
    data            = data_input[:]
    length          = len(data)

    for record in data:
        if(val_freq.has_key(record[attr])):
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    # Calculate the sum of the entropy for each subset of records weighted by
    # their probability of occurring in the training set
    for val in val_freq.keys():
        val_prob        = val_freq[val] / sum(val_freq.values())
        data_subset     = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)

    return( entropy(data, target_attr) - subset_entropy )

def gain_ratio(data_input, attr, target_attr):
    """ Calculate the gain ratio, to determine next target attribute """
    val_freq        = {}
    splitinfo       = 0.0
    data            = data_input[:]
    length          = len(data)

    for record in data:
        if(val_freq.has_key(record[attr])):
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    # Calculate the sum of the entropy for each subset of records weighted by
    # their probability of occurring in the training set
    for val in val_freq.keys():
        val_prob        = val_freq[val] / sum(val_freq.values())
        data_subset     = [record for record in data if record[attr] == val]
        splitinfo      += (-val_prob) * math.log(val_prob, 2)

    return(information_gain(data, attr, target_attr) / splitinfo)

def gini(data_input, attr, target_attr):
    """ Calculate the gini index """
    val_freq        = {}
    data            = data_input[:]
    length          = len(data)

    for record in data:
        if(val_freq.has_key(record[attr])):
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    for val in val_freq.keys():
        pass

def choose_attribute(data_input, attributes, target_attr, fitness_func):
    """ Cycles through all the attributes and returns the attribute with the
    highest information gain """

    data = data_input[:]
    best_gain = 0.0
    best_attr = None

    for attr in attributes:
        if attr != target_attr:
            gain = fitness_func(data, attr, target_attr)
            if gain > best_gain:
                best_gain = gain
                best_attr = attr

    print best_attr
    return best_attr

def get_subset( data_input, best, val):
    """ Returns a list of all the records in data with the value of attribute
    matching the given value """

    data = data_input[:]
    list = []

    if not data:
        return list
    else:
        for record in data:
            if record[best] == val:
                list.append(record)
        return list

def create_decision_tree(data_input, attributes, target_attr, fitness_func):
    """ Returns a new decision tree """
    data    = data_input[:]
    vals    = [record[target_attr] for record in data]
    default = majority_value(data, target_attr)

    # If the dataset or attributes is empty, return the default value. Subtract
    # 1 to account for target attributes
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in dataset have the same values, return it
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        # Choose the next best attribute
        best_attr = choose_attribute(data, attributes, target_attr, fitness_func)
        # Create a new tree/node with the best attribute
        tree = {best_attr:{}}

        # Preprocess data, to generate a list containing the same data as data list
        # but without duplicate

        unique_data = []
        for record in data:
            if unique_data.count(record[best_attr]) <= 0:
                unique_data.append(record[best_attr])

        # Create a new decision tree for each of the values in the best
        # attribute field
        for val in unique_data:
            # Create a subtree for the current value under the best field
            subtree = create_decision_tree(
                    get_subset(data, best_attr, val),
                    [attr for attr in attributes if attr != best_attr],
                    target_attr,
                    fitness_func)

            # Add the new subtree to the empty dictionary
            tree[best_attr][val] = subtree

    return tree

def print_tree(tree, string):
    """ This function recursively crawls through the d-tree and print out """

    if type(tree) == dict:
        print "%s%s" % (string, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (string, item)
            print_tree(tree.values()[0][item], string + "\t")
    else:
        print "%s\t->\t%s" % (string, tree)

if __name__ == "__main__":
    #tree = create_decision_tree( data_input_array, attributes_array, attributes_array[1], information_gain )
    tree = create_decision_tree( data_input_array, attributes_array, attributes_array[1], gain_ratio )

    print "-------------------------"
    print "--    Decision tree    --"
    print "-------------------------"
    print 
    print_tree(tree, "")

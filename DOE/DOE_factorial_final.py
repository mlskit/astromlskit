###############################################################################
"""	
@author		: Nutan Kumari
@filename	:	DOE-Factorial.py
@brief		: This file provides the implementation for common 
			  functions  for DOE Factorial.
@functions	:  
	1.	OSOEST_fullfact()	:	Provides implementation for Full Factoorial
	2.	OSOEST_ff2n()		: 	Provides implementation for 2-Level 
								full-factorial 
	3.	OSOEST_fracFact()	:	Provides implementation for fractional 
								factorial
@version	:	v1.0
@date		:	29 Jan 2015
"""
###############################################################################

import re
def  getProdctValue(H1,rowIdx,OperationIndexList):
       
        retVal = 0
        if OperationIndexList[0] == "-":
            retVal = -1
        else:
            retVal = 1
        
       ## print OperationIndexList
        for i in range(1, len(OperationIndexList)):                 
                retVal = retVal*H1[rowIdx][OperationIndexList[i]]# rowIdx, idx
        
        return retVal     
def getSignAndCombinationIndicesDict(U,I):
    
   
    
    uniqueElemenetsDict = {}
    for i in range(0, len(I)):
        uniqueElemenetsDict[U[I[i]]] = i
    
    retDict = {}

    for i in range(0,len(U)):
        if len(U[i]) > 1:
            valsList = []
            token = U[i]
            
            #Check if there is a negative sign.
            if token[0] == "-":
                valsList.append('-')
            else:
                valsList.append('+')
                
            for j in range(0,len(token)):
                if( (j==0) and (token[j] == "-" or token[j]=="+")):
                    continue
                else:
                    valsList.append(uniqueElemenetsDict[token[j]])  

            retDict[i] =  valsList
               
        else:
            retDict[i] = "None"
            
    #print retDict
    return retDict


    
"""
    @function	: OSOEST_ff2n()
    @brief		: Provides implementation for OSOEST_ff2n API function.
    @processing	: 
    Create a 2-Level full-factorial design
    
    Parameters
    ----------
    n : int
        The number of factors in the design.
    
    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels -1 and 1
    
    Example
    -------
    ::
    
        >>> ff2n(3)
        array([[-1., -1., -1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1., -1.],
               [-1., -1.,  1.],
               [ 1., -1.,  1.],
               [-1.,  1.,  1.],
               [ 1.,  1.,  1.]])
       
"""

def OSOEST_ff2n(n):
	array = [] #list with element "2s"
	for i in range(0,n):
		array.append(2)
	nb_lines = 1  #finding product of the elements in the list
	for arr in array:
		nb_lines *= arr 
	#print array
	a = OSOEST_fullfact(array)
	p = len(array)
	for j in range(0,nb_lines):
		for k in range(0,p):
			if a[j][k] == 0:
				a[j][k] = -1
	return a


"""
@function		: getNDimensioanlList
@brief			: Helper function used by OSOEST_fullfact()	
"""
def getNDimensioanlList(nb_lines, n):
	# Returns a list of list. 
	# The length of list is nb_lines. 
	# Length of each inner list is n.
	nDimList = []
	for i in range(0,nb_lines):
		inner_array = []
		for j in range(0,n):
			inner_array.append(0)
		nDimList.append(inner_array)
			
	return nDimList

""" 
@function		: OSOEST_fullfact()
@brief			: Provides implementation for OSOEST_fullfact API function.
@processing		:	
	Input Params: List stating levels. 
				   e.g. The scenario where we have three levels with 
				   2, 3 and 1 variants in each respectively, the levels
				   list would be [2,3,1]  
	Return : Returns the a list of list representing the full factorial
			  For the above example return would be 
			  [	[0, 0, 0], 
				[1, 0, 0], 
				[0, 1, 0],
				[1, 1, 0], 
				[0, 2, 0],
				[1, 2, 0]]	
"""
def OSOEST_fullfact(levels):
	
	n = len(levels)  # number of factors	e.g levels= [2,3]
	nb_lines = 1
	for level in levels:
		nb_lines *= level 	# for the above example nb_lines will be 2*3 =6

	level_repeat = 1
	range_repeat = nb_lines

	# Get a list of list, with every list member initialied with zero
	# for the above case return a list of size 3*2 with each l=inner list of lenght 2.
	fullFactorial = getNDimensioanlList(nb_lines,n) 
	for i in range(n):
		range_repeat /= levels[i]
		lvl = []
		for j in range(levels[i]):
			lvl += [j]*level_repeat
		rng = lvl*range_repeat
		level_repeat *= levels[i]
		for j in range(0, nb_lines):
			fullFactorial[j][i] = rng[j]
			
	return fullFactorial
"""
    @function		: OSOEST_fractfact()
    @brief			: Provides implementation for OSOEST_fullfact API function.
    @processing		:
    Create a 2-level fractional-factorial design with a generator string.
    
    Parameters
    ----------
    gen : str
        A string, consisting of lowercase, uppercase letters or operators "-"
        and "+", indicating the factors of the experiment
    
    Returns
    -------
    H : 2d-array
        A m-by-n matrix, the fractional factorial design. m is 2^k, where k
        is the number of letters in ``gen``, and n is the total number of
        entries in ``gen``.
    
    Notes
    -----
    In ``gen`` we define the main factors of the experiment and the factors
    whose levels are the products of the main factors. For example, if
    
        gen = "a b ab"
    
    then "a" and "b" are the main factors, while the 3rd factor is the product
    of the first two. If we input uppercase letters in ``gen``, we get the same
    result. We can also use the operators "+" and "-" in ``gen``.
    
    For example, if
    
        gen = "a b -ab"
    
    then the 3rd factor is the opposite of the product of "a" and "b".
    
    The output matrix includes the two level full factorial design, built by
    the main factors of ``gen``, and the products of the main factors. The
    columns of ``H`` follow the sequence of ``gen``.
    
    For example, if
    
        gen = "a b ab c"
    
    then columns H[:, 0], H[:, 1], and H[:, 3] include the two level full
    factorial design and H[:, 2] includes the products of the main factors.
    
    Examples
    --------
    ::
    
        >>> fracfact("a b ab")
        array([[ed-1., -1.,  1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1.,  1.]])
       
        >>> fracfact("A B AB")
        array([[-1., -1.,  1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1.,  1.]])
        
        >>> fracfact("a b -ab c +abc")
        array([[-1., -1., -1., -1., -1.],
               [ 1., -1.,  1., -1.,  1.],
               [-1.,  1.,  1., -1.,  1.],
               [ 1.,  1., -1., -1., -1.],
               [-1., -1., -1.,  1.,  1.],
               [ 1., -1.,  1.,  1., -1.],
               [-1.,  1.,  1.,  1., -1.],
               [ 1.,  1., -1.,  1.,  1.]])
"""
	
def OSOEST_fracfact(gen):
    # Recognize letters and combinations
    A = [item for item in re.split('\-?\s?\+?', gen) if item]  # remove empty strings
    C = [len(item) for item in A]
    #print A
    #print C
    
    # Indices of single letters (main factors)
    I = [i for i, item in enumerate(C) if item==1]
    #print I
	
    # Indices of letter combinations
    J = [i for i, item in enumerate(C) if item!=1]
    #print J
    
    # Check if there are "-" or "+" operators in gen
    U = [item for item in gen.split(' ') if item]  # remove empty strings
#    print "-->",U
    
    # If R1 is either None or not, the result is not changed, since it is a
    # multiplication of 1.
    R1 = _grep(U, '+')
    R2 = _grep(U, '-')
    #print R1
    #print R2
	
    # Fill in design with two level factorial design
    H1 = OSOEST_ff2n(len(I))
    
    #Copy the H1 matrix, as we will update it
    retList = []
    for row in H1:        
        innerRow = []
        for item in row:
            innerRow.append(item)
        retList.append(innerRow)
            
        
	
    idxOperationDict = getSignAndCombinationIndicesDict(U,I) 
   ## print     idxOperationDict
    
   ## print H1
    for combinationIdx in J:
       ## print "combinationIdx-->",combinationIdx
       ## print "idxOperationDict[combinationIdx]--->",idxOperationDict[combinationIdx]
        for rowIdx in range(0, len(H1)):
            prodVal = getProdctValue(H1,rowIdx,idxOperationDict[combinationIdx])
            
          ##  print prodVal
            retList[rowIdx].insert(combinationIdx,prodVal)
                
                
    print retList
        
	
def _grep(haystack, needle):
    try:
        haystack[0]
    except (TypeError, AttributeError):
        return [0] if needle in haystack else []
    else:
        locs = []
        for idx, item in enumerate(haystack):
            if needle in item:
                locs += [idx]
        return locs

"""
The following main function should be used for unit testing this module
"""
if __name__=="__main__":
    print "\n---------------------------DOE FOR FACTORIAL----------------------------------\n"
    levels = [2,2,2]
    print "\n\n***************************OSOEST FULL FACTORIAL****************************\n\n"
    print OSOEST_fullfact(levels)
    print "\n\n*************************OSOEST 2 LEVEL FULL FACTORIAL**********************\n\n"
    print OSOEST_ff2n(3)
    print "\n\n*******OSOEST 2-LEVEL FRACTIONAL-FACTORIAL DESIGN WITH A GENERATOR STRING******\n\n"
    OSOEST_fracfact("a b ab")
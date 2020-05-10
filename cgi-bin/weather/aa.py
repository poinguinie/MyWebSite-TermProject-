Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> result_list = [[1,2,3],[1,2,4]]
>>> result_union = set().union(*result_list)
>>> print(result_union)
{1, 2, 3, 4}
>>> 

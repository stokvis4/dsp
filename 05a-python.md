# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists (which uses "[]") and Tuples (which uses "()")  each contain a set of values. The main difference between a list and tuple is that a list is mutable and thus the number of values (and memory) can vary while a tuple is fixed. Only a tuple can be used as a key in a dictionary because it is immutable and is used  as reference for the values in the dictionary. Every key in a dictionary has a unique hash value and since a list is mutable, if the list were to change, it would skew the dictionary and the value that was returned would be different.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A list is an group of values that is ordered (you can call individual values by their index) and may contain duplicates. A set is an unordered list and cannot contain duplicates.
>>set: l = {'a','d','b','c','d'} --> print(l) = {'d', 'b', 'c', 'a'}
>>list: l =['a','b','c','d','e'] --> print(i) = ['a','b','c','d','e']

>>If you are looking if an element exists in a list or set, the set performs better. It takes O(1) to find an element in the set compared to O(n) for the list which is linear time and takes increasingly long depending on how long the list is. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is a small anonymous function that reduces the amount of scripting needed. Lambda, in the case below, allows us to reduce the amount of code needed and allows us to use a function once in another function. 
>> Example: sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)






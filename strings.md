# Strings

## String methods

### Changing case

Method for changing character cases:

| Method | Purpose |
|:------ | :------ |
|`capitalize()`|Converts the first character to upper case|
|`lower()`|Converts a string into lower case|
|`swapcase()`|Swaps cases, lower case becomes upper case and vice versa|
|`title()`|Converts the first character of each word to upper case|
|`upper()`|Converts a string into upper case|

Try them out with this code:

```{literalinclude} ./python_files/string_case.py
:linenos:
```

### Questioning properties



### Justification

Justification adds 'padding' characters to a string so it becomes a set length.

| Method | Purpose |
|:------ | :------ |
|`center()`|Will center align the string, using a specified character (space is default) as the fill character.|
|`ljust()`|Will left align the string, using a specified character (space is default) as the fill character.|
|`rjust()`|Will right align the string, using a specified character (space is default) as the fill character.|

Try them out with this code:

```{literalinclude} ./python_files/string_justification.py
:linenos:
```



count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
translate()	Returns a translated string
zfill()	Fills the string with a specified number of 0 values at the beginning
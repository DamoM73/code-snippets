# Strings

(string-methods)=
## String Methods

### Changing Case Methods

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

### Substring Methods

These methods return information about substrings in the string

| Method | Purpose |
|:------ | :------ |
|`count()`|Returns the number of times a specified value occurs in a string|
|`find()`|Searches the string for a specified value and returns the position of where it was found|
|`index()`|Searches the string for a specified value and returns the position of where it was found|
|`rfind()`|Searches the string for a specified value and returns the last position of where it was found|
|`rindex()`|Searches the string for a specified value and returns the last position of where it was found|

Try them out with this code:

```{literalinclude} ./python_files/string_substring.py
:linenos:
```

### String Comparison Methods

These methods evaluate a string and return a Boolean value

| Method | Purpose |
|:------ | :------ |
|`endswith()`|Returns true if the string ends with the specified value|
|`isalnum()`|Returns True if all characters in the string are alphanumeric|
|`isalpha()`|Returns True if all characters in the string are in the alphabet|
|`isascii()`|Returns True if all characters in the string are ascii characters|
|`isdecimal()`|Returns True if all characters in the string are ASCII decimals|
|`isdigit()`|Returns True if all characters in the string are digits|
|`isidentifier()`|Returns True if the string is an valid variable name|
|`islower()`|Returns True if all characters in the string are lower case|
|``isnumeric()`|Returns True if all characters in the string can be used as numbers such as digits, fractions, subscripts, superscripts, Roman numerals, currency numerators etc.|
|`isprintable()`|Returns True if all characters in the string are printable|
|`isspace()`|Returns True if all characters in the string are whitespaces|
|`istitle()`|Returns True if the string follows the rules of a title|
|`isupper()`|Returns True if all characters in the string are upper case|
|`startswith()`|Returns true if the string starts with the specified value|

Try them out with this code:

```{literalinclude} ./python_files/string_comparison.py
:linenos:
```

### String Justification Methods

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

### String Modification Methods

These methods will modify a string

| Method | Purpose |
|:------ | :------ |
|`join()`|Converts the elements of an iterable into a string|
|`lstrip()`|Returns the string with the leading whitespace characters (spaces, tabs, newlines) removed|
|`replace()`|Returns a string where a specified value is replaced with a specified value|
|`rsplit()`|Splits the string at the specified separator from right to left, and returns a list|
|`rstrip()`|Returns the string with the trailing whitespace characters (spaces, tabs, newlines) removed|
|`split()`|Splits the string at the specified separator from left to right, and returns a list|
|`splitlines()`|Splits the string at line breaks and returns a list|
|`strip()`|Returns a trimmed version of the string with leading a trailing whitespace removed.|

Try them out with this code:

```{literalinclude} ./python_files/string_modify.py
:linenos:
```

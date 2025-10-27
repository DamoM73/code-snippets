# File Input Output

## Text files

Text files are a simple way to save and retrieve data. They have the advantage of being human readable, so you can open a text file and see what has been saved. 

The disadvantage of text files is that everything is save and read as strings. You will need to [](string-methods) and data type converters to change the data back to the format you wish to use. 

### Reading text files

#### Read all the file

```{literalinclude} ./python_files/text_file_read.py
:linenos:
```

Note:

- `"python_files\names.txt"` &rarr; path to the text file
- `"r"` &rarr; read mode
- all values read from text files are strings

#### Read one line

```{literalinclude} ./python_files/text_file_read_line.py
:linenos:
```

Note:

- `"python_files\names.txt"` &rarr; path to the text file
- `"r"` &rarr; read mode
- all values read from text files are strings

#### Read a set number of lines

```{literalinclude} ./python_files/text_file_read_lines.py
:linenos:
```

Note:

- `"python_files\names.txt"` &rarr; path to the text file
- `"r"` &rarr; read mode
- all values read from text files are strings

#### Read the file into a list

```{literalinclude} ./python_files/text_file_read_to_list.py
:linenos:
```

Note:

- `"python_files\names.txt"` &rarr; path to the text file
- `"r"` &rarr; read mode
- all values read from text files are strings

### Writing text files

Writing to a text file will:

- create a new text file if it doesn't already exist
- overwrite the text file if it does already exist

#### Write a variable to text file

```{literalinclude} ./python_files/text_file_write_variable.py
:linenos:
```

Note:

- `"python_files\save_file.txt"` &rarr; path to the text file
- `"w"` &rarr; write mode
- all values written to text files are strings

#### Write a list to text file

This will write each list element on a new line.

```{literalinclude} ./python_files/text_file_write_list.py
:linenos:
```

Note:

- `"python_files\save_file.txt"` &rarr; path to the text file
- `"w"` &rarr; write mode
- all values written to text files are strings

## Pickle files

Python's pickle module saves Python objects as binary files. This may seem limiting but remember that **everything in Python is an object**.

The advantage of using pickle to save is the object type is preserved. For example, if you save a dictionary, it will return as a dictionary when you load it.

The disadvantage of pickling is that the save file is in binary, so it is not human readable. You cannot open the file to see what has been saved.

### Save a file (pickling)

```{literalinclude} ./python_files/pickle_file_save.py
:linenos:
```

Note:

- `"python_files/save_file.pkl"` &rarr; the path to the pickle file
- `wb` &rarr; the file needs to write binary

### Read a file (unpickle)

```{literalinclude} ./python_files/pickle_file_load.py
:linenos:
```

Note:

- `"python_files/save_file.pkl"` &rarr; the path to the pickle file
- `rb` &rarr; the file needs to read binary


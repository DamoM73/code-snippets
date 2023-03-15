# File Handling

## Text files

### Reading text files

Note:

- `"python_files\names.txt"` &rarr; path to the text file
- `"r"` &rarr; read mode
- all values read from text files are strings

#### Read all the file

```{literalinclude} ./python_files/text_file_read.py
:linenos:
```

#### Read one line

```{literalinclude} ./python_files/text_file_read_line.py
:linenos:
```

#### Read a set number of lines

```{literalinclude} ./python_files/text_file_read_lines.py
:linenos:
```

#### Read the file into a list

```{literalinclude} ./python_files/text_file_read_to_list.py
:linenos:
```

### Writing text files

Writing to a text file will:

- create a new text file if it doesn't already exist
- overwrite the text file if it does already exist

Note:

- `"python_files\save_file.txt"` &rarr; path to the text file
- `"w"` &rarr; write mode
- all values written to text files are strings

#### Write a variable to text file

```{literalinclude} ./python_files/text_file_write_variable.py
:linenos:
```

#### Write a list to text file

This will write each list element on a new line.

```{literalinclude} ./python_files/text_file_write_list.py
:linenos:
```
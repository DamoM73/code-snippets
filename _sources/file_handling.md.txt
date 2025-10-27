# File Handling

## Check file exists

You can use two methods from the `os.path` module to check if a file exists

- `exists()`
- `isfile()`

### `exists()`

The `exists()` method returns `True` if either a provided file or a directory exists, otherwise it returns `False`.

```{literalinclude} ./python_files/file_exists.py
:linenos:
```

Note:

- `"./python_files/example.txt"` is a path to a file
- `"./python_files/example_folder"` is a path to a folder

### `isfile()`

The `isfile()` method returns `True` if the provided file exists. If the file does not exist, or the path points to a directory, then it will return `False`.

```{literalinclude} ./python_files/file_check.py
:linenos:
```

## Delete file

To delete a file use the `remove()` function in the `os` module.

```{literalinclude} ./python_files/file_delete.py
:linenos:
```

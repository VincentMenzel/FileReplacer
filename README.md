# FileReplacer

This script can be used to replace files in a directory. The source and destination directories structure does not have to match. The matching from the source to destination directory files is done by filename. However the similariity of the paths is taken into account. Therefor even if files with the same name exist multiple times in different directories they can be replaced with the most likely match.

# Usage

Start the Script

```bash
  python3 main.py
```

After starting the script you will be Prompted with the following inputs.

```python3
    # 'File source path:' => The location the should be sourced from
    # 'File destination path: => The location the files should be replaced in
    #
    #   The files in the source directory will be used to replace the ones in the destination directory
    #
    # 'Do replace [y/n]: ' => If 'y' is passed as the option the files will be replaced. If 'y' is not passed there will still be print statements in the console
    # and the output files however the files are not replaced
```

While running the script will generate console statements of the status.

`[MISSING]` will be printed if a file in the destination directory does not exist in the src directory</br>
`[REPLACE]` will be printed when a file in the destination directory is replaced a with a file from the source directory</br>

```
REPLACE    src/some/path/file.txt -> dest/some/path/file.txt
MISSING    dest/some/path/file.txt
REPLACE    src/some/path/file.txt -> dest/some/path/file.txt
REPLACE    src/some/path/file.txt -> dest/some/path/file.txt
...
```


# Output 

The script generates 2 output files. `missing.txt` and `replaced.txt`.


## invalid_files.txt
The invalid_files.txt file contains all files that when checked did not qualify as a file by `os.path.isfile`.
```
dest/some/path/file.txt
...
```

## missing.txt

The missing.txt file contains the paths to all missing files. These files could not be mapped to the source directory.
The replaced.txt file contains the path from the source directory which was used to replace the file in the destination directory.
```
dest/some/path/file1.txt
dest/some/path/file2.txt
...
```

## replaced.txt

The replaced.txt file contains the path from the source directory which was used to replace the file in the destination directory.
```
src/some/path/file.txt -> dest/some/path/file.txt
src/file2.txt -> dest/some/path/file2.txt
...
```

## errors.txt
The errors.txt file contains all copy operations in which an error occurred.
```
src/some/path/file.txt -> dest/some/path/file.txt
src/file2.txt -> dest/some/path/file2.txt
...
```
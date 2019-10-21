# CsvSplit
Standalone tool for CSV file splitting

## Usage

```
python csv_split.py <Input File Name or Directory> <Chunk Size in MB>
```

File paths or directory are relative to the location of the batchsplit script.

## Example use-case

The script exists in ~/Downloads/BatchSplit/csv_split.py on your local machine

2 csvs were downloaded:
~/Downloads/GoogleDriveImports/a.csv
~/Downloads/GoogleDriveImports/b.csv

To split all csvs in the GoogleDriveImports folder to 200 MB each,

```
python ~/Downloads/BatchSplit/csv_split.py ~/Downloads/GoogleDriveImports 200
```

Output:
~/Downloads/GoogleDriveImports/a/split_1.csv
~/Downloads/GoogleDriveImports/a/split_2.csv
...
with filenames up split_<N> where <N> is the number of splits

~/Downloads/GoogleDriveImports/b/split_1.csv
~/Downloads/GoogleDriveImports/b/split_2.csv
...
with filenames up split_<N> where <N> is the number of splits

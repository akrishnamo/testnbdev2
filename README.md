testnbdev2
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Install

``` sh
pip install testnbdev2
```

## How to use

Fill me in please! Don’t forget code examples:

``` python
1+1
```

    2

``` python
table(6)
```

    6 times 1 = 6
    6 times 2 = 12
    6 times 3 = 18
    6 times 4 = 24
    6 times 5 = 30
    6 times 6 = 36
    6 times 7 = 42
    6 times 8 = 48
    6 times 9 = 54
    6 times 10 = 60

``` python
import pandas as pd
```

``` python
file_path="https://demo-time-series.s3.us-east-2.amazonaws.com/ex_read_csv1.csv"

col_dict={"date":("date","%d-%m-%Y"),"weight":float,"salary":float}

read_csv(file_path,col_dict, 10)[0]
```

``` python
6+7
```

    13

``` python
assert 2== (2*1)
```

``` python
get_now_date2()
```

    'Ananth says  UTC time is 2023-05-09 05:42:41.926474'

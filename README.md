[<img src="https://avatars.githubusercontent.com/u/82142807?s=400&amp;u=19e108a15566f3a1449bafb03b8dd706a72aebcd&amp;v=4" alt="OpenPecha" width="150" class="jop-noMdConv">](https://openpecha.org)

### Transfer text segment annotations to the original text

## Usage

### Install using pip.

```
pip install git+https://github.com/OpenPecha/num2tib.git

```

### Import

```python
from num2tib.core import convert
from num2tib.core import convert2text

print(convert(123.24))
```

### Transfer_text
```python

text = convert(123.24)
# བརྒྱ་དང་ཉི་ཤུ་རྩ་གསུམ་ཚེག་ཉི་ཤུ་རྩ་བཞི་

text = convert2text(123.24) #no place value 
#གཅིག་ གཉིས་ གསུམ་ ཚེག་ གཉིས་ བཞི་ 

```


**Example**


```python
from num2tib.core import convert
from num2tib.core import convert2text

#float
print(convert(123.2423))
#བརྒྱ་དང་ཉི་ཤུ་རྩ་གསུམ་ཚེག་གཉིས་ བཞི་ གཉིས་ གསུམ་

#int
print(convert(123))
#བརྒྱ་དང་ཉི་ཤུ་རྩ་གསུམ་

#str
print(convert('123.2423'))
#བརྒྱ་དང་ཉི་ཤུ་རྩ་གསུམ་ཚེག་གཉིས་ བཞི་ གཉིས་ གསུམ་

#no place value 
print(convert2text(123))
#གཅིག་ གཉིས་ གསུམ་ 
```

## Project owner(s)

<!-- Link to the repo owners' github profiles -->

- [@spsither](https://github.com/spsither)
- [@TenzinGayche](https://github.com/TenzinGayche)

## Integrations

<!-- Add any intregrations here or delete `- []()` and write None-->

None

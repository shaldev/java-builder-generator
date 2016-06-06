# java-builder-generator
Python script that generates java code using the builder pattern

## To run the script 

execute generator.py using python

``python generator.py``

## Model

Currently model.py contains the [OpenRTB 2.3](https://github.com/openrtb/OpenRTB/blob/master/OpenRTB-API-Specification-Version-2-3-1-FINAL.pdf) object.

## Generating new models

Write a simple python dictonary like `model.py`. For data types you can use the primitives int, and double. You can add more via the `util.py` config script, in the datatypes var.

Also you can use composite data types like String, List\<String\>, List\<Integer\>. 

## Example model

```python
package = 'test'
model = {
  'user' : {
      'name' : 'str',
      'surname' : 'str',
      'phone' : 'int',
      'age' : 'int',
      'luckynumbers' : 'int[]',
      'hobbies' : 'str[]'
    }
}
```

Generated code can be found in example dir.

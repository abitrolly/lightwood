# Predictor API



```python
from lightwood import Predictor

```

Lightwood has one main class; The **Predictor**, which is a modular construct that you can train and get predictions from. It is made out of 3 main building blocks (*features, encoders, mixers*) that you can configure, modify and expand as you wish.

![building_blocks](https://docs.google.com/drawings/d/e/2PACX-1vTrzcXyqDeaGWOwG-3BWOV5wj1U2M5v7ojracqv39z2Ljv-oFqxh4bxFiJxjjtd7CgehptMeBlLYx6w/pub?w=1399&h=818&a=1)

!!! info "Building blocks"
    
    * **Features**:
        * **input_features**: These are the columns in your dataset that you want to take as input for your predictor.
        * **output_features**: These are the columns in your dataset that you want to learn how to predict.
    * **Encoders**: These are tools to turn the data in your input or output features into vector/tensor representations and vice-versa.
    * **Mixers**: How you mix the output of encoded features and also other mixers


## Constructor, \__init__()

```python

my_predictor = Predictor( output=[] | config={...} | load_from_path=<file_path>)

```

!!! note ""
    Predictor, can take any of the following **arguments**
    
    * **load_from_path**: If you have a saved predictor that you want to load, just give the path to the file
    * **output**: A list with the column names you want to predict. (*Note: If you pass this argument, lightwood will simply try to guess the best config possible*)
    * **config**: A dictionary, containing the configuration on how to glue all the building blocks. 

### **config**

The config argument allows you to pass a dictionary that defines and gives you absolute control over how to build your predictive model.
A config example goes as follows:
```python
from lightwood import COLUMN_DATA_TYPES, BUILTIN_MIXERS

config = {

        ## REQUIRED:
        'input_features': [
            {
                'name': 'sensor1',
                'type': COLUMN_DATA_TYPES.NUMERIC
            },
            {
                'name': 'sensor2',
                'type': COLUMN_DATA_TYPES.NUMERIC
            }
        ],

        'output_features': [
            {
                'name': 'action_to_take',
                'type': COLUMN_DATA_TYPES.CATEGORICAL
            }
        ],
        
        ## OPTIONAL
        'mixer': {
            'class': BUILTIN_MIXERS.NnMixer
        }
        
    }
```






#### features

Both **input_features** and **output_features** configs are simple dicts that have the following schema

```python
{
    'name': str,
    Optional('type'): any of COLUMN_DATA_TYPES,
    Optional('encoder_class'): object,
    Optional('encoder_attrs'): dict
}
```
!!! note ""
    * **name**: is the name of the column as it is in the input data frame
    * **type**: is the type od data contained. Where out of the box, supported COLUMN_DATA_TYPES are ```NUMERIC, CATEGORICAL, DATETIME, IMAGE, TEXT, TIME_SERIES```:


    !!! info "If you specify the type, lightwood will use the default encoder for that type, however, you can specify/define any encoder that you want to use. "    
        
        
        * **encoder_class**: This is if you want to replace the default encoder with a different one, so you put the encoder class there
        * **encoder_attrs**: These are the attributes that you want to setup on the encoder once the class its initialized 
        

#### mixer

The **default_mixer** key, provides information as to what mixer to use. The schema for this variable is as follows:

```python
mixer_schema = Schema({
    'class': object,
    Optional('attrs'): dict
})
```

!!! note ""
    * **class**: Its the actual class, that defines the Mixer, you can use any of the BUILTIN_MIXERS or pass your own.
    * **attrs**: This is a dictionary containing the attributes you want to replace on the mixer object once its initialized. We do this, so you have maximum flexibility as to what you can customize on your Mixers.

## learn()

```python
my_predictor.learn(from_data=pandas_dataframe)
```
!!! note ""
    This method is used to make the predictor learn from some data, thus the learn method takes the following arguments.
    
    * **from_data**: A pandas dataframe, that has some or all the columns in the config. The reason why we decide to only suppor pandas dataframes, its because, its easy to load any data to a pandas draframe, and spark for python dataframe is a format we support.
    * **test_data**: (Optional) This is if you want to specify what data to test with, if no test_data passed, lightwood will break the from_data into test and train automatically.
    * **callback_on_iter**: (Optional) This is function callback that is called every 100 epocs the during the learn process.


## predict()

```python
my_predictor.predict(when={..} | when_data=pandas_dataframe)
```
!!! note ""
    This method is used to make predictions and it can take one of the following arguments
    
    * **when**: this is a dictionary of conditions to predict under.
    * **when_data**: Sometimes you want to predict more than one row a ta time, so here it is: a pandas dataframe containing the conditional values you want to use to make a prediction.


## save()

```python
my_predictor.save(path_to=string to path)
```
!!! note ""
    Use this method to save the predictor into a desired path

## calculate_accuracy()

```python
print(my_predictor.calculate_accuracy(from_data=data_source))

```
!!! note ""
    Returns the predictors overall accurary. 


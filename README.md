# TeethDetector
This is a teeth detector and dental age predictor based on TensorFlow.  
This project is based on TensorFlow models.Before you run this project,make sure you have install TensorFlow models.  
How to installed models:https://github.com/tensorflow/models

### Data preprocessing
```
xml_to_csv.py: transform annotation information to data/train.csv
generate_tf_record:transform data/train.csv and images information to data/train.record
```
### How to run
```
1.Please modify related files path:train.bat eval.bat
2.run train.bat
3.run eval.bat
4.If you want to see real-time training situation.Open terminal and "cd" to project's root directory,run command:
tensorboard --logdir=model
```

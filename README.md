# TeethDetector
This is a teeth detector and dental age predictor based on TensorFlow.

### Data preprocessing
```
xml_to_csv.py: transform annotation information to data/train.csv
generate_tf_record:transform data/train.csv and images information to data/train.record
```
### How to run
```
1: Please modify related file path:
run train.bat
run eval.bat
2: Open terminal and "cd" to project's root directory,run command:
tensorboard --logdir=model
```

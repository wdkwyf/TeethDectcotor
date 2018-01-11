# TeethDetector
基于TensorFlow目标检测的牙齿检测
```
利用xml_to_csv.py将annotation里面的标注信息整合到data/train.csv
再用generate_tf_record将data/train.csv与images里面的图片信息整合为data/train.record
```
### How to run
```
使用批处理之前请更改相关文件路径
run train.bat
run eval.bat
打开命令行进入项目根目录，执行命令 tensorboard --logdir=model
```

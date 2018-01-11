import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    train_type = 1
    if train_type == 1:# 训练数据
        annotation_path = os.path.join(os.getcwd(), './data/train/annotations')
    else:#测试数据
        annotation_path = os.path.join(os.getcwd(), './data/eval/annotations')
    xml_df = xml_to_csv(annotation_path)
    if train_type == 1:# 训练数据
        xml_df.to_csv('data/train/train_data.csv', index=None)
    else:#测试数据
        xml_df.to_csv('data/eval/eval_data.csv', index=None)
    print('Successfully converted xml to csv.')

main()
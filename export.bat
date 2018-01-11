call C:\Python_Env\tensorflow\Scripts\activate.bat
python F:\Projects\Python\TensorFlowModels\research\object_detection\export_inference_graph.py --input_type image_tensor --pipeline_config_path F:\Projects\Python\teethDetector\model\ssd_mobilenet_v1_coco.config --trained_checkpoint_prefix F:\Projects\Python\teethDetector\model\train\model.ckpt-61509 --output_directory teethDetector.pb
cmd.exe
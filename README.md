# CorrosionDegreeDetection
An automated carbon steel corrosion detection system based on YOLOv7. It is trained from scratch with an integrated Attention Mechanism for enhanced texture extraction, using a hybrid Mixup and Mosaic data augmentation strategy.
## 所需环境
torch==1.2.0      
scipy==1.2.1  
numpy==1.17.0  
matplotlib==3.1.2  
opencv_python==4.1.2.30  
torch==1.2.0  
torchvision==0.4.0  
tqdm==4.60.0  
Pillow==8.2.0  
h5py==2.10.0  
为了使用amp混合精度，推荐使用torch1.7.1以上的版本。
## 权重下载
1. 在百度网盘中下载预测所需的权值。  
链接: https://pan.baidu.com/s/1Tb828McnWLMWDVti9VwXjw?pwd=evm7  
提取码: evm7 
3. 新建logs文件夹，将下载的权重放入该文件夹中  
## 预测步骤
1. 载入权重后在predict.py文件中选择预测形式  
'predict'           表示单张图片预测    
'video'             表示视频检测，可调用摄像头或者视频进行检测   
'fps'               表示测试fps  
'dir_predict'       表示遍历文件夹进行检测并保存     
'heatmap'           表示进行预测结果的热力图可视化  
2. 模型导出  
'export_onnx'       表示将模型导出为onnx，需要pytorch1.7.1以上。
3. 运行predict.py，如果选择'predict'则输入  
```python
images/DSE_6301.JPG
```

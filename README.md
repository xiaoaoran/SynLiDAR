[![arXiv](https://img.shields.io/badge/arXiv-2107.05399-b31b1b.svg)](https://arxiv.org/abs/2107.05399)

# SynLiDAR dataset: Learning From Synthetic LiDAR Sequential Point Cloud
This is official repository of the SynLiDAR dataset. For technical details, please refer to:

<b> Transfer learning from synthetic to real LiDAR point cloud for semantic segmentation </b> ([Paper](https://www.aaai.org/AAAI22Papers/AAAI-1986.XiaoA.pdf))

  [Aoran Xiao](https://scholar.google.com/citations?user=yGKsEpAAAAAJ&hl=zh-EN), [Jiaxing Huang](https://scholar.google.com/citations?user=czirNcwAAAAJ&hl=zh-EN), [Dayan Guan](https://scholar.google.com/citations?user=9jp9QAsAAAAJ&hl=zh-EN), [Fangneng Zhan](https://scholar.google.com/citations?user=8zbcfzAAAAAJ&hl=zh-EN), [Shijian Lu](https://personal.ntu.edu.sg/shijian.lu/)

### News
[2021.Dec.01] SynLiDAR is accepted by AAAI 2022!  
[2021.Jul.28] SynLiDAR is available for download!

## Dataset
SynLiDAR is a large-scale synthetic LiDAR sequential point cloud dataset with point-wise annotations. 13 sequences of LiDAR point cloud with around 20k scans (over 19 billion
points and 32 semantic classes) are collected from virtual urban cities, suburban towns, neighborhood, and harbor. 

![image](https://github.com/xiaoaoran/SynLiDAR/blob/main/images/synlidar.png)

![image](https://github.com/xiaoaoran/SynLiDAR/blob/main/images/Fig2.PNG)

![image](https://github.com/xiaoaoran/SynLiDAR/blob/main/images/Fig3.PNG)

## Download
1) You can download SynLiDAR in [Google Drive](https://docs.google.com/forms/d/e/1FAIpQLScZR3re0YFn59mlnag8s7vD5p4JaMkX2oxug5rn1K5bc5C-4g/viewform?usp=sf_link), we provide:  
  -- **FullDataset**: Full SynLiDAR dataset (about 245GB).  
  -- **SubDataset**: uniformlly downsampled dataset (about 24GB), this is the dataset that we used in [Paper](https://arxiv.org/abs/2107.05399). You are recommend to use this smaller dataset for faster experiments.    
2) [[BaiduYun](https://pan.baidu.com/s/1EFsknahSKgDMj7F1tPqrfg)](password: p3wm)
3) You can download SynLiDAR through browser &rarr; [[DR-NTU](https://researchdata.ntu.edu.sg/dataset.xhtml?persistentId=doi:10.21979/N9/BSKUOE)]
4) You can also download through provided python script, this requires installing pyDataverse
```
pip install pyDataverse
python download.py
```

Note: For most of sequences, we compressed and split them into multiple small files. Please download them and cat into one file before extraction. E.g. for sequence 01:
```
cat 01*>01.tar.gz
tar -zxvf 01.tar.gz
```

The data should organized in the following format:
```
/SynLiDAR/
  ????????? 00/
    ????????? velodyne
      ????????? 000000.bin
      ????????? 000001.bin
      ...
    ????????? labels
      ????????? 000000.label
      ????????? 000001.label
      ...
  ...
  ????????? annotations.yaml
  ????????? read_data.py
```
We provide class annotations (in 'annotations.yaml') and example python code for reading data (in 'read_data.py').


## Citation
If you find our work useful in your research, please consider citing:  
```
@article{xiao2021transfer,
  title={Transfer learning from synthetic to real LiDAR point cloud for semantic segmentation},
  author={Xiao, Aoran and Huang, Jiaxing and Guan, Dayan and Zhan, Fangneng and Lu, Shijian},
  journal={arXiv: 2107.05399},
  year={2021}
} 
```

## Related Repos
- [Unsupervised Representation Learning for Point Clouds: A Survey](https://github.com/xiaoaoran/3d_url_survey)
- [FPS-Net: A convolutional fusion network for large-scale LiDAR point cloud segmentation](https://github.com/xiaoaoran/FPS-Net)

[![arXiv](https://img.shields.io/badge/arXiv-2107.05399-b31b1b.svg)](https://arxiv.org/abs/2107.05399)

# SynLiDAR dataset: Learning From Synthetic LiDAR Sequential Point Cloud
This is official repository of the SynLiDAR dataset. For technical details, please refer to:

<b> Transfer learning from synthetic to real LiDAR point cloud for semantic segmentation </b> ([Paper](https://www.aaai.org/AAAI22Papers/AAAI-1986.XiaoA.pdf))

  [Aoran Xiao](https://scholar.google.com/citations?user=yGKsEpAAAAAJ&hl=zh-EN), [Jiaxing Huang](https://scholar.google.com/citations?user=czirNcwAAAAJ&hl=zh-EN), [Dayan Guan](https://scholar.google.com/citations?user=9jp9QAsAAAAJ&hl=zh-EN), [Fangneng Zhan](https://scholar.google.com/citations?user=8zbcfzAAAAAJ&hl=zh-EN), [Shijian Lu](https://personal.ntu.edu.sg/shijian.lu/)


## News
[2023.Mar.] We released [SemanticSTF](https://github.com/xiaoaoran/SemanticSTF), a real adverse weather point cloud dataset with point-wise annotations for 3D semantic segmentation.  
[2022.Sep.28] Check the latest [benchmark](https://paperswithcode.com/sota/3d-unsupervised-domain-adaptation-on-synlidar) for UDA of LiDAR segmentation (from SynLiDAR to SemanticKITTI).  
[2022.Aug.06] We recommend some [projects](#projects-using-synlidar) that use SynLiDAR.  
[2021.Dec.01] SynLiDAR is accepted by AAAI 2022!  
[2021.Jul.28] SynLiDAR is available for download!

## Dataset
SynLiDAR is a large-scale synthetic LiDAR sequential point cloud dataset with point-wise annotations. 13 sequences of LiDAR point cloud with around 20k scans (over 19 billion
points and 32 semantic classes) are collected from virtual urban cities, suburban towns, neighborhood, and harbor. 

![image](https://github.com/xiaoaoran/SynLiDAR/blob/main/images/synlidar.png)

![image](https://github.com/xiaoaoran/SynLiDAR/blob/main/images/Fig2.PNG)

![image](https://github.com/xiaoaoran/SynLiDAR/blob/main/images/Fig3.PNG)

<p align="center">
<img src="https://github.com/xiaoaoran/SynLiDAR/blob/main/images/example.gif" width="512">
</p>

## 📥 Download SynLiDAR

We provide multiple download options depending on your environment and use case.

1) **\[Hugging Face (Recommended)\]** Download SynLiDAR from [huggingface](https://huggingface.co/datasets/AR-X/SynLiDAR) for both fullset and subset variants  
  -- **FullDataset**: Full SynLiDAR dataset (about 245GB).  
  -- **SubDataset**: uniformlly downsampled dataset (about 24GB), this is the dataset that we used in [Paper](https://arxiv.org/abs/2107.05399). You are recommend to use this smaller dataset for faster experiments. 
2) **\[BaiduYun (国内用户推荐)\]** [[BaiduYun](https://pan.baidu.com/s/1EFsknahSKgDMj7F1tPqrfg)](password: p3wm)
3) **\[DR-NTU\]** You can download SynLiDAR through browser &rarr; [[DR-NTU](https://researchdata.ntu.edu.sg/dataset.xhtml?persistentId=doi:10.21979/N9/BSKUOE)]
4) **\[DR-NTU\]** You can also download through provided python script, this requires installing pyDataverse
```bash
pip install pyDataverse
python download.py
```

Note: For most of sequences, we compressed and split them into multiple small files. Please download them and cat into one file before extraction. E.g. for sequence 01:
```bash
cat 01*>01.tar.gz
tar -zxvf 01.tar.gz
```

The data should organized in the following format:
```
/SynLiDAR/
  └── 00/
    └── velodyne
      └── 000000.bin
      ├── 000001.bin
      ...
    └── labels
      └── 000000.label
      ├── 000001.label
      ...
  ...
  └── annotations.yaml
  └── read_data.py
```
We provide class annotations (in 'annotations.yaml') and example python code for reading data (in 'read_data.py').


## Citation
If you find our work useful in your research, please consider citing:  
```
@inproceedings{xiao2022transfer,
  title={Transfer learning from synthetic to real LiDAR point cloud for semantic segmentation},
  author={Xiao, Aoran and Huang, Jiaxing and Guan, Dayan and Zhan, Fangneng and Lu, Shijian},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={36},
  number={3},
  pages={2795--2803},
  year={2022}
}
```

## Projects using SynLiDAR
Here we list some projects from top conferences and journals that use SynLiDAR. Please feel free to leave us messages to add your projects!
- [NeurIPS2023] Segment Any Point Cloud Sequences by Distilling Vision Foundation Models. [[paper](https://arxiv.org/pdf/2306.09347.pdf)] [[project](https://github.com/youquanl/Segment-Any-Point-Cloud)]
- [CVPR2023] 3D Semantic Segmentation in the Wild: Learning Generalized Models for Adverse-Condition Point Clouds. [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Xiao_3D_Semantic_Segmentation_in_the_Wild_Learning_Generalized_Models_for_CVPR_2023_paper.pdf)] [[project](https://github.com/xiaoaoran/SemanticSTF)]
- [CVPR2023] Adversarially Masking Synthetic to Mimic Real: Adaptive Noise Injection for Point Cloud Segmentation Adaptation. [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_Adversarially_Masking_Synthetic_To_Mimic_Real_Adaptive_Noise_Injection_for_CVPR_2023_paper.pdf)]
- [CVPR2023] Single Domain Generalization for LiDAR Semantic Segmentation. [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Kim_Single_Domain_Generalization_for_LiDAR_Semantic_Segmentation_CVPR_2023_paper.pdf)]
- [NeurIPS2022] PolarMix: A General Data Augmentation Technique for LiDAR Point Clouds. [[pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/475b85eb74d201bead9927807e713e95-Paper-Conference.pdf)] [[project](https://github.com/xiaoaoran/polarmix)]
- [ECCV2022] CoSMix: Compositional Semantic Mix for Domain Adaptation in 3D LiDAR Segmentation. [[paper](https://arxiv.org/pdf/2207.09778.pdf)] [[project](https://github.com/saltoricristiano/cosmix-uda)]
- [ECCV2022] GIPSO: Geometrically Informed Propagation for Online Adaptation in 3D LiDAR Segmentation. [[pdf](https://arxiv.org/pdf/2207.09763.pdf)] [[project](https://github.com/saltoricristiano/gipso-sfouda)]

## Related Repos
Find our other repos for point cloud understanding!
- [Unsupervised Representation Learning for Point Clouds: A Survey](https://github.com/xiaoaoran/3d_url_survey), IEEE Transactions on Pattern Analysis and Machine Intelligence 2023.
- [3D Semantic Segmentation in the Wild: Learning Generalized Models for Adverse-Condition Point Clouds](https://github.com/xiaoaoran/SemanticSTF), CVPR 2023.
- [PolarMix: A General Data Augmentation Technique for LiDAR Point Clouds](https://github.com/xiaoaoran/polarmix), NeurIPS 2022.
- [FPS-Net: A convolutional fusion network for large-scale LiDAR point cloud segmentation](https://github.com/xiaoaoran/FPS-Net), ISPRS journal of Photogrammetry and Remote Sensing 2021.

# pdg2pdf-linux
pdg 格式是超星公司开发的电子书格式,
其本质就是一堆图片和一个xml文件.

本脚本是用python3开发的, 在linux下测试

直接将pdg文件组成的.zip转换为pdf文件.

# 使用方法
0. 安装 `python3` 和 `pip3`
1. `clone` 本项目或者下载 release 中的源代码文件
2. `python pdg2pdf.py input.zip output.pdf`

# 注意事项
1. zip文件内图片为类似`000001.pdg, 0000002.pdg`的文件
2. 20分钟敲出来的东西, 可能有bug, 有bug请提issue
3. `PDG` 格式相当复杂，从网络上查到的资料来看，零几年就有人在研究。PDG 因为是超星的商业化的文件格式，有多种加密方式。本项目所能提供的是最简单的——没有加密、甚至没有PDG文件头的格式。如果有无法解决的问题，目前似乎唯一的解决方法是下载 `pdg2pic.exe` https://www.cnblogs.com/stronghorse/p/14594337.html 

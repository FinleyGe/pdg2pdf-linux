# pdg2pdf-linux
pdg 格式是超星公司开发的电子书格式,
其本质就是一堆图片和一个xml文件.

本脚本是用python3开发的, 在linux下测试

直接将pdg文件组成的.zip转换为pdf文件.

# 使用方法
1. `clone` 本项目
2. `python pdg2pdf.py input.zip output.pdf` 

# 注意事项
1. zip文件内图片为类似`000001.pdg, 0000002.pdg`的文件
2. 20分钟敲出来的东西, 可能有bug, 有bug请提issue

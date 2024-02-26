


## 简介
- 参考：
- ​       https://blog.csdn.net/qianbin3200896/article/details/125177765
- ​       https://github.com/kraasch/png2ttf
- ​       在前者基础上适配了opencv读取图片路径中含有中文的情况并且将所有图片全部纳入一个ttf
- 运行步骤：
- 1. 下载Python安装OpenCV、tdqm、numpy
- 2. 打开png2svg.py，设置img_dir，如果Windows自行加r或者修改\为/，然后在命令行使用Python运行此文件
  3. 下载安装自己系统对应的FontForge，https://github.com/fontforge/fontforge
  4. 打开svg2ttf.py，设置对应变量，Windows路径规则同2
  5. 若是Windows则使用安装路径下例如C:\Program Files (x86)\FontForgeBuilds\bin的ffpython.exe运行svg2ttf.py.
  6. linux我没测


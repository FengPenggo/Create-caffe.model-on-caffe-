主要介绍Caffe的前期配置、Caffe中网络结构的描述方法和原理，以及使用Caffe进行训练和测试的流程。

1.1 环境搭建

本章所介绍的环境搭建系统为Ubuntu 14.04或Ubuntu16.04。

1.1.1 Ubuntu环境设置

 

1.1.2 Caffe环境设置

下载所需要的依赖库：

 

在命令行输入以下命令:

 

*sudoapt-getinstall*libprotobuf-devlibleveldb-devlibsnappy-devlibopencv-dev

*sudoapt-getinstall*libhdf5-serial-devprotobuf-compiler

*sudoapt-getinstall*--no-install-recommendslibboost-all-dev

*sudo apt-get install*libatlas-base-dev

*sudo apt-get install*libgflags-dev libgoogle-glog-dev liblmdb-dev

 

下载安装Caffe：

从GitHub上下载Caffe：https://github.com/BVLC/caffe。也可以输入以下命令来下载。

*sudo git clone*https://github.com/BVLC/caffe.git

下载完成后，解压Caffe源码包，得到如错误**!**未找到引用源。文件。

![img](file:///C:/Users/FENGPE~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

 

配置Makefile.config文件：

解压完成之后，对应文件夹中有Makefile.config.example文件，是Caffe自带的Makefile的例子，复制这个文件并重命名为Makefile.config，打开之后如错误**!**未找到引用源。所示。

图

![img](file:///C:/Users/FENGPE~1/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png)

 

编译Caffe：

在命令行输入以下命令编译Caffe

make all

若CPU是4核的可以输入（8核同理）

*makeall*–j4

如果提示无法找到hdf5.h请打开Makefile.config 更改如下语句

INCLUDE_DIRS := $(PYTHON_INCLUDE)  /usr/local/include /usr/include/hdf5/serial/

如果提示无法找到libhdf5.so请打开Makefile.config更改如下语句

LIBRARY_DIRS := $(PYTHON_LIB) /usr/lib/x86_64-linux-gnu/hdf5/serial /usr/local/lib /usr/lib

编译成功后，在Caffe根目录下会出现一个build文件夹，打开之后再打开tools文件夹，可得到图1. 3结果。

![img](file:///C:/Users/FENGPE~1/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)

图1. 3编译完成后的/build/tools文件夹

之后编译test文件下的源码，同理输入以下命令即可。

*make*test

*make*runtest

 

Caffe训练及测试时会用到python接口，下面介绍pycaffe接口的配置，其流程如下：

下载库：

*sudo*apt-get install python-numpy python-scipy python-matplotlibpython-sklearn python3-pippython-pip

*sudo*pip install python-skimage 

*sudo*apt-get install python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags 

*sudo*pip installCython ipython

 

编译：

在命令行输入以下命令，即可开始编译python接口。

*cd*caffe

*make*pycaffe

 

添加环境变量：

在/etc/profile文件的最后一行中添加环境变量：

export PYTHONPATH=/path/to/caffe/python:$PYTHONPATH

之后输入以下命令，使之生效。

*source*/etc/profile

 

测试：

在命令行输入：

*cd python*

*python*

在python中输入：

*import*caffe

若结果如图1. 5所示，则python接口配置成功。

![img](file:///C:/Users/FENGPE~1/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png)

图1. 5python接口配置结果

若出现”No module named _caffe”的错误，可尝试重新输入以下命令，

*make*clean

*make*pycaffe

结束.
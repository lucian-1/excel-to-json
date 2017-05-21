# excel-to-json
Tool for excel to json  

## Usage
>If you have not installed Python or not use python2  
>Is better to use virtualenv  
>[virtualenv](https://github.com/pypa/virtualenv)  

Rename the excel file to 'toJson.xls'  
rename.sh  
 `#!/bin/bash
 a = ls |grep $'.xls';
 mv $a toJson.xls;`  

1.require python2;  
`$python --version`  
`$python2.7`  

2.pip install requirements  
`$pip install -- upgrade pip`  
`$pip install -r requirements.txt`  

3.run  
 `$sudo python excel2json.py`  

### if no permission, file permission 777  
Just a small tool, you can modify modify it according to your needs  

#
#

# excel-to-json
excel转为json的小工具

## 使用方法
>如果你没有安装python或没有使用python2  
>推荐使用virtualenv  
>[virtualenv](https://github.com/pypa/virtualenv)  

设置Excel文件名为 'toJson.xls'  
rename.sh  
 `#!/bin/bash
 a = ls |grep $'.xls';
 mv $a toJson.xls;`  

1.需要python2  
`$python --version`  
`$python2.7`  

2.使用pip安装requirements  
`$pip install -- upgrade pip`  
`$pip install -r requirements.txt`  

3.运行脚本    
 `$sudo python excel2json.py`  

### 如果no permission, 文件权限 777
只是个小工具,你可以根据你的需求修改成批处理脚本

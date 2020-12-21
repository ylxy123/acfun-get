# acfun视频下载工具

*当前版本：1.0.3*
*作者：ylxy123*

*github项目地址：https://github.com/ylxy123/acfun-get*

requests: 
| 第三方库 | 版本   |
| -------- | ------ |
| Click    | 7.0.0  |
| tqdm     | 4.32.1 |
| requests | 2.22.0 |

安装方法：
> pip install acfun-get

手动安装地址：
> https://pypi.org/project/acfun-get/

安装成功之后，即可在命令行中输入命令```-h```或```--help```获取帮助信息：

>   $ acfun-get  --help
>
>   Usage: acfun-get [OPTIONS]
>
>   Options:
>     -V, --version    显示版本信息并退出  
>     -u, --url TEXT   acfun视频链接  
>     -p, --path TEXT  视频下载路径  [default: E:\Desktop]  
>     -h, --help       Show this message and exit.  

下载视频：

1.  **参数u, p同时指定**

    >   \> acfun-get  -u  https://www.acfun.cn/v/ac12191547  -p  E:\Desktop\ylxy
    >
    >   当前操作系统：Windows  
    >
    >   {1: '1080P', 2: '720P', 3: '540P', 4: '360P'}  
    >   请选择清晰度: 1  
    >   视频存放路径：E:\Desktop\ylxy  
    >
    >   正在下载 全网首发｜陈亮同名专辑单曲《不忘初心》 中国风指弹[1080P] : 100%|███████████████████████ ███████████████████| 52/52 [00:57<00:00,  1.11s/it]
    >
    >   

2.  **参数p未指定时，使用默认路径或上次指定路径**

    >   \> acfun-get -u  https://www.acfun.cn/v/ac12191547
    >
    >   当前操作系统：Windows
    >
    >   {1: '1080P', 2: '720P', 3: '540P', 4: '360P'}  
    >   请选择清晰度: 4  
    >   视频存放路径：E:\Desktop\ylxy  
    >
    >   正在下载 全网首发｜陈亮同名专辑单曲《不忘初心》 中国风指弹[360P] : 100%|███████████████████████████████████████████| 52/52 [00:09<00:00,  5.42it/s]

3.  **参数u未指定时，会提示输入链接**

    >   \> acfun-get -p E:\Desktop\ylxy
    >
    >   当前操作系统：Windows
    >
    >   请输入链接: https://www.acfun.cn/v/ac12191547  
    >   {1: '1080P', 2: '720P', 3: '540P', 4: '360P'}  
    >   请选择清晰度: 4  
    >   视频存放路径：E:\Desktop\ylxy  
    >
    >   正在下载 全网首发｜陈亮同名专辑单曲《不忘初心》 中国风指弹[360P] : 100%|███████████████████████████████████████████| 52/52 [00:25<00:00,  2.07it/s]

4.  **当没有参数设置时，输出帮助信息**

    >   \> acfun-get
    >
    >   当前操作系统：Windows
    >
    >   Usage: acfun-get [OPTIONS]
    >
    >   Options:
    >     -V, --version    显示版本信息并退出  
    >     -u, --url TEXT   acfun视频链接  
    >     -p, --path TEXT  视频下载路径  [default: E:\Desktop\ylxy]  
    >     -h, --help       Show this message and exit.  
    >
    >   

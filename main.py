# -*- coding: utf-8 -*-

import click
import os
import re
import sys
import json
import requests
import platform
from tqdm import tqdm
  


__version__ = "1.0.3"


def load_path():
    with open(txt_path,'r') as f:
        return f.readline()

print("\n当前操作系统："+platform.system())

if platform.system()=='Windows':
    import winreg
    txt_path = 'D:/path.txt'
    def get_desktop():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        path = winreg.QueryValueEx(key, "Desktop")[0]
        with open(txt_path,'w') as f:
            f.write(path)
    if not os.path.exists(txt_path):
        get_desktop()
    default_path = load_path()
    
     
elif platform.system()=='Linux':
    txt_path = '/etc/path.txt'
    if not os.path.exists(txt_path):
        default_path = '~/acfun'
        with open(txt_path,'w') as f:
            f.write(path)
    else:
        default_path = load_path()
    

else:
    txt_path = '/Users/path.txt'
    if not os.path.exists(txt_path):
        default_path = '/Users/acfun'
        with open(txt_path,'w') as f:
            f.write(path)
    else:
        default_path = load_path()

headers = {
    'referer': 'https://www.acfun.cn/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83'
    }

pgk_dir = os.path.dirname(os.path.abspath(__file__))


class DefaultHelp(click.Command):
    def __init__(self, *args, **kwargs):
        context_settings = kwargs.setdefault('context_settings', {})
        if 'help_option_names' not in context_settings:
            context_settings['help_option_names'] = ['-h', '--help']
        self.help_flag = context_settings['help_option_names'][0]
        super(DefaultHelp, self).__init__(*args, **kwargs)

    def parse_args(self, ctx, args):
        if not args:
            args = [self.help_flag]
        print()
        return super(DefaultHelp, self).parse_args(ctx, args)

@click.command(cls=DefaultHelp)
@click.version_option(
    '{0} from {1} (Python {2})'.format(__version__, pgk_dir, sys.version[:3]),
    '-V', '--version', help='显示版本信息并退出')
@click.option('-u', '--url', prompt="请输入链接", help='acfun视频链接')
@click.option('-p', '--path', default=default_path, help='视频下载路径',show_default=True)
def cli(url, path):
    with open(txt_path,'w') as f1:
        f1.write(path)
    path = load_path()
    
    class m3u8_url():
        def __init__(self, f_url):
            self.url = f_url

        def get_m3u8(self):
            global flag, qua, rel_path
            html = requests.get(self.url, headers=headers).text
            first_json = json.loads(re.findall('window.pageInfo = window.videoInfo = (.*?)};', html)[0] + '}', strict=False)
            name = first_json['title'].strip().replace("|",'')
            video_info = json.loads(first_json['currentVideoInfo']['ksPlayJson'], strict=False)['adaptationSet'][0]['representation']
            Label = {}
            num = 0
            for quality in video_info:  # 清晰度
                num += 1
                Label[num] = quality['qualityLabel']
            print(Label)
            choice = int(input("请选择清晰度: "))
            print("视频存放路径：" + path)
            Download(name + '[{}]'.format(Label[choice]), video_info[choice - 1]['url'], path).start_download()

    class Download():
        urls = []

        def __init__(self, name, m3u8_url, path):
            '''
            :param name: 视频名
            :param m3u8_url: 视频的 m3u8文件 地址
            :param path: 下载地址
            '''
            self.video_name = name
            self.path = path
            self.f_url = str(m3u8_url).split('hls/')[0] + 'hls/'
            with open(self.path + '/{}.m3u8'.format(self.video_name), 'wb')as f:
                f.write(requests.get(m3u8_url, headers={'user-agent': 'Chrome/84.0.4147.135'}).content)

        def get_ts_urls(self):
            with open(self.path + '/{}.m3u8'.format(self.video_name), "r") as file:
                lines = file.readlines()
                for line in lines:
                    if '.ts' in line:
                        self.urls.append(self.f_url + line.replace('\n', ''))

        def start_download(self):
            self.get_ts_urls()
            for url in tqdm(self.urls, desc="正在下载 {} ".format(self.video_name)):
                movie = requests.get(url, headers={'user-agent': 'Chrome/84.0.4147.135'})
                with open(self.path + '/{}.flv'.format(self.video_name), 'ab')as f:
                    f.write(movie.content)
            os.remove(self.path + '/{}.m3u8'.format(self.video_name))
    m3u8_url(url).get_m3u8()

  
if __name__ == '__main__':
    cli()
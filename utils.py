# coding=utf-8
import configparser
import uuid
import platform
from multiprocessing import Lock
import os
import zipfile

# 锁
mutex = Lock()


# import os


def get_db_config():
    cfgpath = "config.ini"
    # 创建管理对象
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")  # python3
    items = conf.items('db')
    return dict(items)


def set_db_config(args):
    """
    将db信息写入配置文件
    :param args: 字典
    :return:
    """

    cfgpath = "config.ini"
    # 创建管理对象
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")  # python3
    items = conf.items('db')
    for item in args:
        conf.set('db', item, args[item])
    with open(cfgpath, "w+", encoding="utf-8") as cfgpath_fd:
        conf.write(cfgpath_fd)
    return dict(items)


def set_cookie_config(args):
    """
    将db信息写入配置文件
    :param args: 字典
    :return:
    """

    cfgpath = "config.ini"
    # 创建管理对象
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")  # python3
    if conf.has_section('cookies'):
        conf.remove_section('cookies')
    if not conf.has_section('cookies'):
        conf.add_section('cookies')
    # items = conf.items('cookies')
    for item in args:
        if args[item]:
            conf.set('cookies', item, args[item])
    with open(cfgpath, "w+", encoding="utf-8") as cfgpath_fd:
        conf.write(cfgpath_fd)
    # return dict(items)


def set_config(section, args):
    """
    设置配置信息
    :param section: [section] 的名字
    :param args: 字典
    :return:
    """

    cfgpath = "config.ini"
    # 创建管理对象
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")  # python3
    if conf.has_section(section):
        conf.remove_section(section)
    if not conf.has_section(section):
        conf.add_section(section)
    for item in args:
        if args[item]:
            conf.set(section, item, args[item])
    with open(cfgpath, "w+", encoding="utf-8") as cfgpath_fd:
        conf.write(cfgpath_fd)


def get_config(section):
    cfgpath = "config.ini"
    # 创建管理对象
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")  # python3
    items = conf.items(section)
    return dict(items)


def get_phantomjs_path():
    current_system = platform.system()
    phantomjs = "third-party/phantomjs"
    if "Windows" == current_system:
        phantomjs = "third-party/phantomjs.exe"
    if not os.path.exists(phantomjs) and os.path.exists(phantomjs + '.zip'):
        zipf = zipfile.ZipFile(phantomjs + '.zip')
        zipf.extractall('third-party')
    return phantomjs


def kill_process(process_name):
    try:
        current_system = platform.system()
        if "Windows" == current_system:
            os.system('taskkill /f /im %s' % process_name)
        else:
            cmd = 'ps aux | grep {process_name} '.format(process_name=process_name)
            cmd += "| awk {print '$2'} | xargs kill"
            os.system(cmd)
    except Exception as e:
        print(str(e))


def recursive_get_li(parent_id, library_id, xpath_list):
    """
    递归获取li
    :param parent_id:父节点ID
    :param library_id:
    :param xpath_list:
    :return:
    """
    re_list = list()
    if xpath_list:
        li = xpath_list.xpath('./ul/li')
        for item in li:
            temp_dict = dict()
            pk = item.attrib.get('pk')
            nm = item.attrib.get('nm')
            temp_dict['id'] = str(uuid.uuid1())
            temp_dict['parent_id'] = parent_id
            temp_dict['library_id'] = library_id
            temp_dict['pk'] = pk
            temp_dict['name'] = nm
            child = recursive_get_li(temp_dict['id'], library_id, item)
            temp_dict['child'] = child
            re_list.append(temp_dict)
    return re_list


def split_list(src_list):
    """
    拆分列表,层级关系拆成一层
    :param src_list:
    :return:
    """
    new_list = list()
    for item in src_list:
        child = item.pop('child')
        new_list.append(item)
        if child:
            child = split_list(child)
            new_list.extend(child)
    return new_list


# 取字符串中两个符号之间的东东
def txt_wrap_by(start_str, end, html):
    if not html:
        return ''
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

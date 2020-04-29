#coding=utf-8
from mailmerge import MailMerge
import ConfigParser
import os

template1 = "./template/template1.docx"
template2 = "./template/template2.docx"
#sys_info_dir = "./info/"

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path,'doc.conf')
cf = ConfigParser.ConfigParser()
cf.read(config_path)
sysls = cf.get('base', 'sysls')
#sys_info_dir = cf.get('base', 'sys_info_dir')
syslist = sysls.split(',')

for sys in syslist:
    sys_info_file = sys_info_dir + sys
    dict = {}
    if os.path.exists(sys_info_file):
        for line in open(sys_info_file):
            list = line.strip('\n').split("===")
            dict[list[0]] = list[1].decode('utf-8')
    sysname = dict.has_key('sysname') and dict['sysname'] or 'nono '
    document1 = MailMerge(template1)
    print("Fields included in {}:{}".format(template1, document1.get_merge_fields()))
    document1.merge(
        sysname = sysname,
        author = dict.has_key('author') and dict['author'] or ' ',
        level1 = dict.has_key('level1') and dict['level1'] or ' ',
        level2 = dict.has_key('level2') and dict['level2'] or ' ',
        rto = dict.has_key('rto') and dict['rto'] or ' ',
        rpo = dict.has_key('rpo') and dict['rpo'] or ' '
    )
    document1.write(('./output/' + sysname + u'系统应急预案.docx').encode('gbk'))

    document2 = MailMerge(template2)
    print("Fields included in {}:{}".format(template2, document2.get_merge_fields()))
    document2.merge(
        sysname = sysname,
        author = dict.has_key('author') and dict['author'] or ' ',
        summary = dict.has_key('summary') and dict['summary'] or ' '
    )
    document2.merge_rows('col1',
        [{'col1':'aa', 'col2':'ab', 'col3':'ac'},
         {'col1':'ba', 'col2':'bb', 'col3':'bc'},
         {'col1':'ca', 'col2':'cb', 'col3':'cc'}
        ])
    document2.write(('./output/' + sysname + u'系统应急操作技术手册--系统分册.docx').encode('gbk'))

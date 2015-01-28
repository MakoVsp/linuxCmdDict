# linuxCmdDict
A tool for linux cmd!

Instal

wget https://raw.githubusercontent.com/MakoVsp/linuxCmdDict/master/linuxCmdDict.py

sudo mv ./linuxCmdDict.py /usr/bin/dict

sudo chmod +x /usr/bin/dict

Use

$ dict hello world

###################################
#  hello world 你好,世界 (U: None E: None )
#  Explains None
###################################


数据接口


http://fanyi.youdao.com/openapi.do?keyfrom=<keyfrom>&key=<key>&type=data&doctype=<doctype>&version=1.1&q=要翻译的文

版本：1.1，请求方式：get，编码方式：utf-8


主要功能：中英互译，同时获得有道翻译结果和有道词典结果（可能没有）

参数说明：

  type - 返回结果的类型，固定为data

  doctype - 返回结果的数据格式，xml或json或jsonp

  version - 版本，当前最新版本为1.1

  q - 要翻译的文本，必须是UTF-8编码，字符长度不能超过200个字符，需要进行urlencode编码

  only - 可选参数，dict表示只获取词典数据，translate表示只获取翻译数据，默认为都获取

  注： 词典结果只支持中英互译，翻译结果支持英日韩法俄西到中文的翻译以及中文到英语的翻译

errorCode：

  0 - 正常

   20 - 要翻译的文本过长

   30 - 无法进行有效的翻译

   40 - 不支持的语言类型

   50 - 无效的key

   60 - 无词典结果，仅在获取词典结果生效

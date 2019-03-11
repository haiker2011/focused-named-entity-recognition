# -*- coding: utf-8 -*-

import json

"""
focusedNER.FocusedNER
~~~~~~~~~~~~~~~~
模块提供中心命名实体识别功能.
"""

from utils import Utils

class FocusedNER(object):

      def getFocusedNER(self, nerStringList, content):
            r"""获取每个命名实体的8个特征属性，返回json.
            :param nerStringList: 命名实体列表.
            :param content: 文章标题和正文，json格式.
            :return: 中心命名实体列表
            :rtype: json string
            """

            # 1. 获取命名实体8个特征
            nerFeaturesJson = self._getNERFeatures(nerStringList, content)

            # 2. 利用训练的模型进行预测是否是中心命名实体
            focusedNER = ['hello', nerFeaturesJson]

            # 3. 返回中心命名实体
            return focusedNER


      def _getNERFeatures(self, nerStringList, content):
            r"""获取每个命名实体的8个特征属性，返回json.
            :param nerStringList: 命名实体列表.
            :param content: 文章标题和正文，json格式.
            :return: 计算8个特征之后的json数据
            :rtype: json string
            """

            # 0. 解析json
            content_json = json.loads(content)

            # 1. 从content获取title，判断命名实体在不在标题中，在设置为1
            title = content_json['title']
            isInTitle = Utils.isInTitle(nerStringList, title)
            print("isInTitle: ")
            print(isInTitle)

            # 2. 计算每个命名实体频次（或者逆文档频次）#
            nerFrequency = Utils.nerFrequency(nerStringList, content_json)
            print("nerFrequency: ")
            print(nerFrequency)

            # 3. 获取每个命名实体类型type
            

            # 4. 每个命名实体类型分布（暂不实现）

            # 5. 每个命名实体邻居实体的类型（暂不实现）

            # 6. 每个命名实体是否出现在段落第一句话中，在设置为1

            # 7. 每一篇文档中命名实体个数 #
            nerCount = Utils.nerCount(nerStringList)
            print("nerCount: ")
            print(nerCount)

            # 8. 文档标题是否含有命名实体，含有设置为1
            print("titleHasNER: ")
            print(Utils.titleHasNER(nerStringList, ['hello', 'world']))




            nerFeaturesJson = 'hello'
            return nerFeaturesJson



if __name__=="__main__":
      focused_ner = FocusedNER()
      content = '{"news_url":"http://example.com/","title":"hello world","abstrct":"balabala","content":"balabala","comments":[{"author":"abababab","content":"ababababab"},{"author":"abababab","content":"ababababab"}]}'
      
      focused_ner.getFocusedNER(['hello', 'world'], content)

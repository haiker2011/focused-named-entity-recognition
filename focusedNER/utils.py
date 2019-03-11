# -*- coding: utf-8 -*-

class Utils(object):
      @staticmethod
      def isInTitle(nerStringList, title):
            r"""判断命名实体对否在标题中.
            :param nerStringList: 命名实体列表.
            :param content: 文章标题和正文，json格式.
            :return: 中心命名实体列表
            :rtype: list bool
            """
            isInTitle = []
            for nerString in nerStringList:
                  if nerString in title:
                        isInTitle.append(True)
                  else:
                        isInTitle.append(False)
            
            return isInTitle
      
      @staticmethod
      def nerFrequency(nerStringList, content):
            r"""获取每个命名实体的频次.
            :param nerStringList: 命名实体列表.
            :param content: 文章标题和正文，json格式.
            :return: 获取每个命名实体的频次
            :rtype: list int
            """
            nerFrequency = []
            for nerString in nerStringList:
                  eachNerFrequency = (len(content['title'].split(nerString))-1) + (len(content['content'].split(nerString))-1)
                  nerFrequency.append(eachNerFrequency)

            
            return nerFrequency

      @staticmethod
      def titleHasNER(nerStringList, title):
            r"""判断标题中是否含有命名实体.
            :param nerStringList: 命名实体列表.
            :param content: 文章标题和正文，json格式.
            :return: 判断标题中是否含有命名实体
            :rtype: bool
            """

            return sum(Utils.isInTitle(nerStringList, title)) > 0

      @staticmethod
      def nerCount(nerStringList):
            r"""返回每篇文章中命名实体的个数.
            :param nerStringList: 命名实体列表.
            :return: 中心命名实体个数
            :rtype: int
            """
            return len(nerStringList)

      @staticmethod
      def allFocusedNER(focusedNER):
            r"""返回每篇文章中核心命名实体列表.
            :param focusedNERList: 候选命名实体列表.
            :return: 中心命名实体列表
            :rtype: list string
            """

            return [i for i in focusedNER if i > 0]
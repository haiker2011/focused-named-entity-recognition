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

            isInTitle = [0, 0]
            return isInTitle
      
      @staticmethod
      def nerFrequency(nerStringList, content):
            r"""获取每个命名实体的频次.
            :param nerStringList: 命名实体列表.
            :param content: 文章标题和正文，json格式.
            :return: 获取每个命名实体的频次
            :rtype: list int
            """

            nerFrequency = [10, 11]
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
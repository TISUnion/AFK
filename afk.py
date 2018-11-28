# -*- coding: utf-8 -*-

afklist = {}

helpmsg = '''------MCD AFK插件------
命令帮助如下:
!!afk help -显示帮助消息
!!afk list -获取挂机玩家名单以及显示注释
!!afk start [注释]-标注自己开始挂机
!!afk stop -标注自己停止挂机
!!afk kick [玩家] [注释] -踢出一个正在afk的玩家
--------------------------------'''

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!afk'):
      args = info.content.split(' ')
      if (len(args) == 1):
        for line in helpmsg.splitlines():
          server.tell(info.player, line)
      elif (args[1]=='start'):
        if (info.player in afklist):
          server.tell(info.player,'你已经在挂机中!')
        else:
          if (len(args) == 3):
            afklist[info.player] = args[2]
            server.tell(info.player,'成功标注自己挂机')
      elif (args[1] == 'stop'):
        if (info.player in afklist):
          afklist.pop(info.player)
          server.tell(info.player,'成功停止挂机')
        else:
          server.tell(info.player,'你不在挂机中')
      elif (args[1] == 'help'):
        for line in helpmsg.splitlines():
          server.tell(info.player, line)
      elif (args[1] == 'list'):
        if (len(afklist) > 0):
          for singleplayer in afklist:
            strmsg = singleplayer + ': ' + afklist[singleplayer]
            server.tell(info.player,strmsg)
        else:
          server.tell(info.player,'目前没人在挂机')
      elif (args[1] == 'kick'):
        if (len(args) != 4):
          server.tell(info.player,'参数格式不正确')
        else:
          if args[2] in afklist:
            server.execute('kick ' + args[2] + ' [AFK]:玩家' + info.player + '踢出了您,原因:' + args[3])
            afklist.pop(info.player)
          else:
            server.tell(info.player,'该玩家不在挂机状态!')
      
"""
手工生成日志，主要有两种方式：
一、使用python创建对象形式，如本程序所示。
二、如create_log.xes所示。
"""
from copy import deepcopy
from pm4py.objects.log.obj import EventLog, Trace, Event
from pm4py.objects.log.exporter.xes import exporter as xes_exporter


def creat_log():
    # 演示日志、迹、事件日志的创建和添加属性。
    L = EventLog()
    e1 = Event()
    e1["concept:name"] = "A"
    e2 = Event()
    e2["concept:name"] = "B"
    e3 = Event()
    e3["concept:name"] = "C"
    e4 = Event()
    e4["concept:name"] = "D"
    t = Trace()
    t.append(e1)
    t.append(e2)
    t.append(e3)
    t.append(e4)
    for i in range(5):
        L.append(deepcopy(t))
    print(len(L))
    print(L)
    from pm4py.objects.log.exporter.xes import exporter as xes_exporter
    xes_exporter.apply(L, 'exported_log.xes')


def abcnum2log(abcnum):
    """
    创建只有事件 concept:name属性的日志对象
    :param abcnum: ['abc*12','bcd*3',...]
    :return: object.log
    """
    dic = {}
    mapping = {}
    for item in abcnum:
        key = item.split('*')[0]
        value = item.split('*')[1]
        dic[key] = value
    print(dic)
    log = EventLog()  # 创建日志对象
    for item in dic.items():
        num = int(item[1])
        trace = Trace()  # 创建迹对象
        for i in list(item[0]):
            mapping['concept:name'] = i
            event1 = Event(mapping)  # 创建事件对象
            trace.append(event1)  # 事件添加到迹中
        for i in range(0, num):
            log.append(trace)  # 迹添加到日志中
    return log


if __name__ == '__main__':
    # creat_log()
    traces_origin = ['ABCDFEGH*2', 'ABCDEFGH*3', 'ABCH*5', 'ABCDEGFH*8', 'ABCDH*1', 'AH*1', 'ADEGH*1', 'ABFEGH*1',
                     'ADFH*1', 'AFCB*1', 'ACEFG*1', 'BFG*1']
    path = 'created_log.xes'
    log = abcnum2log(traces_origin)
    xes_exporter.apply(log, path)

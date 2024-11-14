## spring_unauthorizedPOC

Actuator模块提供了一个监控和管理生产环境的模块，可以使用http、jmx、ssh、telnet等来管理和监控应用。包括应用的审计（Auditing）、健康（health）状态信息、数据采集（metrics gathering）统计等监控运维的功能。同时，提供了可以扩展 Actuator端点（Endpoint）自定义监控指标。这些指标都是以JSON接口数据的方式呈现。借助于Actuator开发者可以很⽅便地对应⽤系统某些监控指标进⾏查看、统计等。在 Actuator 启⽤ 的情况下，如果没有做好相关权限控制，⾮法⽤户可通过访问默认的执⾏器端点 （endpoints）来获取应⽤系统中的监控信息，从⽽导致信息泄露甚⾄服务器被接管的事件发⽣。

## 安装

```
git clone https://github.com/xanszZZ/spring_unauthorizedPOC
cd spring_unauthorizedPOC
```

## 使用

因为本工具是根据pocsuite3框架的开发规范编写的poc

在使用前请下载pocsuite3

项目地址

```
https://github.com/knownsec/pocsuite3
```

环境

```
Python 3.7+
Works on Linux, Windows, Mac OSX, BSD, etc.
```

pip安装

```
pip3 install pocsuite3

# use other pypi mirror
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pocsuite3
```

poc

```
pocsuite -r pocs/spring_unauthorizedPOC.py -f xxx.txt
```



## 免责声明🧐

本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建测试环境。

在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
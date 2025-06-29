import os
import json
import requests
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
import asyncio
import time


vx_sign_data = {
    "cookie": "acw_tc=b65cfd3d17473628655091819e132bf9112a984c4e8566575c616b94c36baf",
    "token": "83c8b770b4c14951a073020a146a92c6",
    "x-lf-dxrisk-token": "68253980oGhhXUDYEQ7x0lUYKK3xiVqWdgKkagX1",
    "x-lf-bu-code": "C20400",
    "x-lf-channel": "C2",
    "x-lf-dxrisk-source": "5",
    "x-lf-usertoken": "83c8b770b4c14951a073020a146a92c6",
}

vx_lottery_data = {
    "cookie": "acw_tc=3ccdc14217472700342351816e6089403b6ab1f3e991b84235bbc646ed1671",
    "token": "83c8b770b4c14951a073020a146a92c6",
    "x-lf-dxrisk-token": "68253980oGhhXUDYEQ7x0lUYKK3xiVqWdgKkagX1",
    "x-lf-bu-code": "C20400",
    "x-lf-channel": "C2",
    "x-lf-dxrisk-source": "5",
    "x-lf-usertoken": "83c8b770b4c14951a073020a146a92c6",
}

app_sign_data = {
    "cookie": "acw_tc=b65cfd3317473566059447147e6a63599f133e4e0db4800f55401de0acdfbe",
    "token": "43ddd9d210f3485da606c261a60a4bd4",
    "x-lf-dxrisk-token": "68268db3sFoKEAA6C5vdOa0xklpTC2l2qBFa5QC1",
    "x-lf-bu-code": "L00602",
    "x-lf-channel": "L0",
    "x-lf-dxrisk-source": "2",
    "x-lf-usertoken": "43ddd9d210f3485da606c261a60a4bd4",
}

app_lottery_data = {
    "cookie": "zg_d5bd8e6372844af9b43b8ce5bb74b787=%7B%22sid%22%3A%201747100361151%2C%22updated%22%3A%201747100410221%2C%22info%22%3A%201747031624443%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Flongzhu.longfor.com%2Flongball-homeh5%2F%23%2FnewGrowthDetail%3FminiShare%3Dfalse%22%2C%22cuid%22%3A%20%22117380909%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201747100361151%7D; zg_did=%7B%22did%22%3A%20%22196c3330af7351a-06e90936f886b7-2127594d-51bf4-196c3330af83a78%22%7D; SERVERID=8487eaf0b2f3ef928d0f8a84feaf4f25|1747100409|1747100360; _dx_uzZo5y=b272ddb87d1d5e6a7485ca1a43d949f399c09e036618f375c9bab4f9f53d45194dfa66f6; acw_tc=ac11000117471003605465527e005600c0b5845e3f26a1c5d0853dbb994aee",
    "token": "43ddd9d210f3485da606c261a60a4bd4",
    "x-lf-dxrisk-token": "68009c0ayCvL40AicSqWthKL2tGHUD8PZREfPcv1",
    "x-lf-bu-code": "L00602",
    "x-lf-channel": "L0",
    "x-lf-dxrisk-source": "2",
    "x-lf-usertoken": "711a7433304b4655ba7719052e393a65",
}


# 配置日志
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class LHTJ:
    def __init__(self):
        self.base_url = ""
        self.is_debug = os.getenv("IS_DEBUG", "false").lower() == "true"
        self.do_flag = {"true": "✅", "false": "⛔️"}
        self.notify_msg = []
        self.ck_status = True
        self.title = ""
        self.avatar = ""

    def debug_log(self, data: Any, label: str = "debug") -> None:
        """调试日志"""
        if self.is_debug:
            logger.info(
                f"\n-----------{label}-----------\n{json.dumps(data, indent=2, ensure_ascii=False)}\n"
            )

    def get_datetime(self) -> str:
        """获取当前时间字符串"""
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    async def fetch(
        self, method: str, url: str, headers: Dict, data: Optional[Dict] = None
    ) -> Optional[Dict]:
        """发送 HTTP 请求"""
        try:
            full_url = self.base_url + url if url.startswith(("/", ":")) else url
            kwargs = {"headers": headers, "timeout": 10}
            if data:
                kwargs["json"] = data

            response = requests.request(method.upper(), full_url, **kwargs)
            response.raise_for_status()

            self.debug_log(response.json(), url.split("/")[-1])
            return response.json()
        except Exception as e:
            self.ck_status = False
            logger.error(f"⛔️ 请求失败: {str(e)}")
            return None

    async def signin(self, user: Dict) -> int:
        """执行签到"""
        try:
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
            res = await self.fetch("POST", url, headers, data)
            print(res)
            reward_num = (
                res.get("data", {}).get("reward_info", [{}])[0].get("reward_num", 0)
                if res and res.get("data", {}).get("is_popup") == 1
                else 0
            )
            status = (
                self.do_flag["true"]
                if res and res.get("data", {}).get("is_popup") == 1
                else self.do_flag["false"]
            )
            logger.info(
                f"{status} 每日签到: {'成功，获得' + str(reward_num) + '分' if reward_num else '今日已签到'}"
            )
            return reward_num
        except Exception as e:
            logger.error(f"⛔️ 签到失败: {str(e)}")
            return 0

    async def lottery_signin(self, user: Dict) -> None:
        """抽奖签到"""
        time.sleep(1)
        try:
            url = "https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/sign"
            headers = {
                "cookie": user["cookie"],
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003029) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
                "authtoken": user["token"],
                "x-lf-dxrisk-token": user["x-lf-dxrisk-token"],
                "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
                "bucode": user["x-lf-bu-code"],
                "channel": user["x-lf-channel"],
                "origin": "https://longzhu.longfor.com",
                "referer": "https://longzhu.longfor.com/",
                "x-lf-dxrisk-source": user["x-lf-dxrisk-source"],
                "x-lf-usertoken": user["x-lf-usertoken"],
            }
            data = {
                "component_no": "CR14T05T01P4HSSN",
                "activity_no": "AP25P053E0MQAECS",
            }
            # app端data数据
            if user["x-lf-bu-code"] == "L00602":
                data["component_no"] = "CS14S00348I5DW7H"
                data["activity_no"] = "AP25P05380JXUM6X"

            res = await self.fetch("POST", url, headers, data)
            status = (
                self.do_flag["true"]
                if res and res.get("code") == "0000"
                else self.do_flag["false"]
            )
            msg = (
                f"获得{res.get('data', {}).get('ticket_times', 0)}次机会"
                if res and res.get("code") == "0000"
                else res.get("message", "")
            )
            logger.info(f"{status} 抽奖签到: {msg}")
        except Exception as e:
            logger.error(f"⛔️ 抽奖签到失败: {str(e)}")

        time.sleep(1)
        """点击抽奖"""
        try:
            url = "https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/click"
            headers = {
                "cookie": user["cookie"],
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003029) NetType/4G Language/zh_CN miniProgram/wx50282644351869da",
                "authtoken": user["token"],
                "x-lf-dxrisk-token": user["x-lf-dxrisk-token"],
                "x-gaia-api-key": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
                "bucode": user["x-lf-bu-code"],
                "channel": user["x-lf-channel"],
                "origin": "https://longzhu.longfor.com",
                "referer": "https://longzhu.longfor.com/",
                "x-lf-dxrisk-source": user["x-lf-dxrisk-source"],
                "x-lf-usertoken": user["x-lf-usertoken"],
            }
            data = {
                "component_no": "CR14T05T01P4HSSN",
                "activity_no": "AP25P053E0MQAECS",
                "batch_no": "",
            }
            # app端data数据
            if user["x-lf-bu-code"] == "L00602":
                data["component_no"] = "CS14S00348I5DW7H"
                data["activity_no"] = "AP25P05380JXUM6X"

            res = await self.fetch("POST", url, headers, data)
            status = (
                self.do_flag["true"]
                if res and res.get("code") == "0000"
                else self.do_flag["false"]
            )
            msg = (
                f"奖励类型:{res.get('data', {}).get('reward_type', 0)}"
                f"获得{res.get('data', {}).get('reward_num', 0)}个奖励"
                if res and res.get("code") == "0000"
                else res.get("message", "")
            )
            logger.info(f"{status} 点击抽奖: {msg}")
        except Exception as e:
            logger.error(f"⛔️ 点击抽奖失败: {str(e)}")

    async def run(self,type):
        """主运行逻辑"""
        if type==1:
            logger.info(f"🚀 开始处理微信端签到抽奖")
            try:
                reward_num = await self.signin(vx_sign_data)
                await self.lottery_signin(vx_lottery_data)

            except Exception as e:
                logger.error(f"账户处理异常: {str(e)}")

        if type==2:
            logger.info(f"🚀 开始处理app端签到抽奖")
            try:
                reward_num = await self.signin(app_sign_data)
                await self.lottery_signin(app_lottery_data)

            except Exception as e:
                logger.error(f"账户处理异常: {str(e)}")

            


if __name__ == "__main__":
    client = LHTJ()
    asyncio.run(client.run(1))
    time.sleep(5)
    client = LHTJ()
    asyncio.run(client.run(2))

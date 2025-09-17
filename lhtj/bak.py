import requests
import urllib3

# 自定义HTTPAdapter
class CustomSSLContextHTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)

#自定义ssl_context
ctx = urllib3.util.create_urllib3_context()
ctx.load_default_certs()
ctx.set_ciphers("DEFAULT@SECLEVEL=1")

#替换原有的https的adapters
session = requests.session()
session.adapters.pop("https://", None)
session.mount("https://", CustomSSLContextHTTPAdapter(ssl_context=ctx))



headers = {
    'Accept': 'image/webp,image/avif,image/jxl,image/heic,image/heic-sequence,video/*;q=0.8,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
    'Origin': 'https://longzhu.longfor.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 &MAIAWebKit_iOS_com.longfor.supera_1.17.2_202509090115_Default_3.2.4.9',
    'Referer': 'https://longzhu.longfor.com/',
    'Sec-Fetch-Dest': 'image',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
}

params = {
    'sid': '86a6421ddbfd93260aea4d31b2b1e1b6',
    'aid': 'dx-1758020363437-51278053-1',
    'ak': 'd1a43734fc59aeae9f1562dbd70fdf54',
    'type': '0',
    'c': '68c3d504rWXlhhiZFBuCQz4N2P2N77xMtJPqDW41',
    '_r': '0.1096275048273665',
}


response = requests.request(
    method= "POST",
    url='https://ly-ver.longhu.net/api/p1', params=params, headers=headers
)
print(response.content)

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.ocr.v20181119 import ocr_client, models 
import json
from config import SECRET_ID, SECRET_KEY

def requestOrc(params):
    try: 
        cred = credential.Credential(SECRET_ID, SECRET_KEY) 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile) 

        req = models.GeneralBasicOCRRequest()
        req.from_json_string(params)

        resp = client.GeneralBasicOCR(req)
        return json.loads(resp.to_json_string())
        # print 

    except TencentCloudSDKException as err: 
        print(err) 

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from exts.wechatpy.client.api.base import BaseWeChatAPI
from exts.wechatpy.utils import to_text


class WeChatBatch(BaseWeChatAPI):
    """
    https://work.weixin.qq.com/api/doc#90000/90135/90979

    异步批量接口用于大批量数据的处理，提交后接口即返回，企业微信会在后台继续执行任务。
    执行完成后，企业微信后台会通过任务事件通知企业获取结果。事件的内容是加密的，解密过程请参考 [消息的加解密处理][signure]，任务事件请参考异步任务完成事件推送。
    目前，仅为通讯录更新提供了异步批量接口
    """

    def sync_user(self, url, token, encoding_aes_key, media_id, to_invite=True):
        """
        增量更新成员

        https://work.weixin.qq.com/api/doc#90000/90135/90980

        :param url: 企业应用接收企业微信推送请求的访问协议和地址，支持http或https协议
        :param token: 用于生成签名
        :param encoding_aes_key: 用于消息体的加密，是AES密钥的Base64编码
        :param media_id: 上传的csv文件的media_id
        :param to_invite: 是否邀请新建的成员使用企业微信（将通过微信服务通知或短信或邮件下发邀请，每天自动下发一次，最多持续3个工作日），默认值为true。
        :return: 返回的 JSON 数据包
        """
        return self._post(
            "batch/syncuser",
            data={
                "media_id": media_id,
                "to_invite": to_invite,
                "callback": {
                    "url": url,
                    "token": token,
                    "encodingaeskey": encoding_aes_key,
                },
            },
        )

    def replace_user(self, url, token, encoding_aes_key, media_id, to_invite=True):
        """
        全量覆盖成员

        https://work.weixin.qq.com/api/doc#90000/90135/90981

        :param url: 企业应用接收企业微信推送请求的访问协议和地址，支持http或https协议
        :param token: 用于生成签名
        :param encoding_aes_key: 用于消息体的加密，是AES密钥的Base64编码
        :param media_id: 上传的csv文件的media_id
        :param to_invite: 是否邀请新建的成员使用企业微信（将通过微信服务通知或短信或邮件下发邀请，每天自动下发一次，最多持续3个工作日），默认值为true。
        :return: 返回的 JSON 数据包
        """
        return self._post(
            "batch/replaceuser",
            data={
                "media_id": media_id,
                "to_invite": to_invite,
                "callback": {
                    "url": url,
                    "token": token,
                    "encodingaeskey": encoding_aes_key,
                },
            },
        )

    def replace_party(self, url, token, encoding_aes_key, media_id):
        """
        全量覆盖部门

        https://work.weixin.qq.com/api/doc#90000/90135/90982

        :param url: 企业应用接收企业微信推送请求的访问协议和地址，支持http或https协议
        :param token: 用于生成签名
        :param encoding_aes_key: 用于消息体的加密，是AES密钥的Base64编码
        :param media_id: 上传的csv文件的media_id
        :return: 返回的 JSON 数据包
        """
        return self._post(
            "batch/replaceparty",
            data={
                "media_id": media_id,
                "callback": {
                    "url": url,
                    "token": token,
                    "encodingaeskey": encoding_aes_key,
                },
            },
        )

    def get_result(self, job_id):
        """
        获取异步任务结果

        https://work.weixin.qq.com/api/doc#90000/90135/90983

        :param job_id: 异步任务id，最大长度为64字符
        :return: 返回的 JSON 数据包
        """
        return self._get("batch/getresult", params={"jobid": job_id})

    def invite(self, user=None, party=None, tag=None):
        """
        邀请成员

        https://work.weixin.qq.com/api/doc#90000/90135/90975

        企业可通过接口批量邀请成员使用企业微信，邀请后将通过短信或邮件下发通知。

        :param user: 成员ID列表, 最多支持1000个。
        :param party: 成员ID列表, 最多支持100个。
        :param tag: 成员ID列表, 最多支持100个。
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(user=user, party=party, tag=tag)
        return self._post("batch/invite", data=data)

    def invite_user(
        self,
        url,
        token,
        encoding_aes_key,
        user_ids=None,
        party_ids=None,
        tag_ids=None,
        invite_tips=None,
    ):
        """
        邀请成员关注(deprecated)
        https://qydev.weixin.qq.com/wiki/index.php?title=异步任务接口

        :param url: 企业应用接收企业微信推送请求的访问协议和地址，支持http或https协议
        :param token: 用于生成签名
        :param encoding_aes_key: 用于消息体的加密，是AES密钥的Base64编码
        :param user_ids: 可选，成员ID列表，多个接收者用‘|’分隔，最多支持1000个。
        :param party_ids: 可选，部门ID列表，多个接收者用‘|’分隔，最多支持100个。
        :param tag_ids: 可选，标签ID列表，多个接收者用‘|’分隔。
        :param invite_tips: 可选，推送到微信上的提示语
        :return: 返回的 JSON 数据包
        """
        data = optionaldict()
        data["callback"] = {
            "url": url,
            "token": token,
            "encodingaeskey": encoding_aes_key,
        }
        if isinstance(user_ids, (tuple, list)):
            user_ids = "|".join(map(to_text, user_ids))
        if isinstance(party_ids, (tuple, list)):
            party_ids = "|".join(map(to_text, party_ids))
        if isinstance(tag_ids, (tuple, list)):
            tag_ids = "|".join(map(to_text, tag_ids))
        data["touser"] = user_ids
        data["toparty"] = party_ids
        data["totag"] = tag_ids
        data["invite_tips"] = invite_tips
        return self._post("batch/inviteuser", data=data)

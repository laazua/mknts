"""
2024-01-19
"""
import os
import time
import datetime
import calendar
import shutil
import smtplib
import email.encoders as email_encode
import email.mime.base as email_base
import email.mime.text as email_text
import email.mime.multipart as email_mltpart

from src.count_es.log import Logger
from src.count_es.config import config


def remove_xlsx_files(path):
    """remove xlsx files"""
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)


def send_email(title, people=None):
    """将数据发送个指定的收件人"""
    receiver = config.get("email", "receivers")
    email_server = smtplib.SMTP_SSL(config.get("email", "address"), config.get("email", "port"))
    email_server.login(config.get("email", "username"), config.get("email", "password"))
    Logger.info("登陆成功,开始发送邮件")
    sender = config.get("email", "username")
    try:
        if people:
            message = pack_data(people, title)
            email_server.sendmail(sender, f"{people}@zxy.com", message.as_bytes())
            Logger.info(f"发送邮件给{people}成功")
            return True
        if "," not in receiver:
            message = pack_data(receiver, title)
            email_server.sendmail(sender, f"{receiver}@zxy.com", message.as_bytes())
            Logger.info(f"发送邮件给{receiver}成功")
        else:
            receivers = receiver.split(",")
            for receiver in receivers:
                if receiver:
                    message = pack_data(receiver, title)
                    email_server.sendmail(sender, f"{receiver}@zxy.com", message.as_bytes())
                    Logger.info(f"发送邮件给{receiver}成功")
        return True
    except Exception as e:
        Logger.error("邮件发送失败: ", e)
        return False
    

def pack_data(receiver, title):
    """邮件附件打包"""
    xlsx_path = config.get("app", "xlsxpath")
    all_tables = os.listdir(xlsx_path)
    message = email_mltpart.MIMEMultipart()
    message['From'] = config.get("email", "username")
    message['To'] = receiver
    message['Subject'] = title
    body = "Hi ALL: \n\r 此邮件为业务线的站点数据统计情况, 统计了站点的访问数据情况, 包含: \n\r \t1. 站点的访问次数. \n\r \t2. 站点状态码响应情况. \n\r \t3. 站点的各个路由访问次数及该路由下的响应状态码. \n\r \t4. 站点的各个地区访问情况. \n\r \t5. 站点的客户端IP访问情况. \n\r \t6. 站点的各个路由访问时的请求时间. \n\r \t7.以上各个统计项,只统计了该项排名前20的数据。"
    message.attach(email_text.MIMEText(body, 'plain'))
    # 添加附件
    for filename in all_tables:
        try:
            with open(f"{xlsx_path}/{filename}", 'rb') as attachment:
                part = email_base.MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                email_encode.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            message.attach(part)
            Logger.info(f"添加附件{filename}成功.")
        except Exception as e:
            Logger.error("添加附件失败: ", e)
    return message


def back_xlsx(bakType):
    """
    备份xlsx文件
    """
    back_path = config.get("app", "backpath")
    xlsx_path = config.get("app", "xlsxpath")
    now_date = time.strftime("%Y-%m-%d")
    nback = f"{back_path}/{bakType}-{now_date}"
    if not os.path.exists(nback):
        os.makedirs(nback)
    try:
        for file in os.listdir(xlsx_path):
            src_file = os.path.join(xlsx_path, file)
            dst_file = os.path.join(nback, file)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)
    except Exception as e:
        Logger.error("备份xlsx文件失败: ", e)

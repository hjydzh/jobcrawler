#coding:utf-8
import common.Const as const

const.MSG_SELECT = """
SELECT
		id as msgId,
		msg as msg,
		class_name as class_name,
		re_msg as re_msg,
		type as type,
		status as status

"""

const.INSERT_JOBS = """
insert JOBS
(JOB,COMPANY_NAME,PUBLISH_DATE)
values
(%s,%s,%s)
"""

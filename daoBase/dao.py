#coding:utf-8
from daoBase import insert
from common.sqlconstants import *
from utils import dmoUtils

def insert_jobs(jobs):
    pars = map(lambda job : dmoUtils.job_dmo_to_pars(job),jobs)
    insert(const.INSERT_JOBS,pars)
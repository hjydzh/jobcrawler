#coding=utf-8
import sys
sys.path.append('/home/workspace/jobcrawler')
from utils import HttpUtil
from BeautifulSoup import BeautifulSoup
from dmo.job import Job
from utils import DateUtil
from daoBase import dao

class Crawler:

    def __init__(self, date):
        self.date = date

    def sample(self):
        self.__zl_sample()

    def __zl_sample(self):
        page = 1
        while page < 50:
            print '第%s页' % page
            self.__zl_handler(page)
            page=page+1

    def __zl_handler(self, page):
        html = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8D%97%E4%BA%AC&kw=java&sm=0&p=' + str(page)
        response = HttpUtil.request(html)
        soup = BeautifulSoup(response)
        job_list = soup.find(id='newlist_list_content_table').findAll('table' ,attrs={"class": "newlist"})[1:]
        self.__insert_jobs(map(self.__get_zljob_detail, job_list))

    def __get_zljob_detail(self, job_soup):
        job = Job()
        job.job = job_soup.find(attrs={"class": "zwmc"}).text.encode('utf-8')
        job.company_name = job_soup.find(attrs={"class": "gsmc"}).text.encode('utf-8')
        job.publish_date = self.__zldate_parse(job_soup.find(attrs={"class": "gxsj"}).text.encode('utf-8'))
        job.salary = job_soup.find(attrs={"class": "zwyx"}).text.encode('utf-8')
        return job

    def __zldate_parse(self, date):
        date_str = '2016-'+date
        return DateUtil.str_to_time(date_str, '%Y-%m-%d')

    def __job51_handler(self, html):
        print html
        soup = BeautifulSoup(html)
        job_list = soup.find(id="resultList").find('div' ,attrs={"class": "el"})
        return map(self.__get_51job_detail, job_list)

    def __get_51job_detail(self, job_soup):
        job = Job()
        job.job = job_soup.find('p' ,attrs={"class": "t1"}).text
        job.company_name = job_soup.find('p' ,attrs={"span": "t2"}).text
        job.publish_date = job_soup.find('p' ,attrs={"span": "t5"}).text
        job.source = 'ZL'

    def __insert_jobs(self, jobs):
        for i,job in enumerate(jobs):
            if job.publish_date <self.date:
                dao.insert_jobs(jobs[:i-1])
                raise Exception
        dao.insert_jobs(jobs)
if __name__ == '__main__':
    date = DateUtil.substract_day(DateUtil.now(), 1)
    crawler = Crawler(date)
    crawler.sample()
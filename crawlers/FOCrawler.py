#coding=utf-8
import sys
sys.path.append('/home/workspace/jobcrawler')
from utils import HttpUtil
from BeautifulSoup import BeautifulSoup
from dmo.job import Job
from utils import DateUtil
from daoBase import dao



class FOCrawler:

    def __init__(self, date):
        self.date = date

    def sample(self):
        page = 1
        url='http://search.51job.com/list/070200%252C00,000000,0000,00,9,99,java,0,1.html?lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&confirmdate=9&dibiaoid=0'
        opener = HttpUtil.init_opener()
        HttpUtil.opener_request(url, opener)
        while page < 50:
            print '第%s页' % page
            self.__research(page, opener)
            page=page+1

    def __research(self, page, opener):
        html = 'http://search.51job.com/jobsearch/search_result.php?jobarea=070200%2C00&keyword=java&curr_page=' + str(page)
        response = HttpUtil.opener_request(html, opener)
        soup = BeautifulSoup(response)
        job_list = soup.find(id='resultList').findAll('div' ,attrs={"class": "el"})[1:]
        self.__insert_jobs(map(self.__get_51job_detail, job_list))


    def __get_51job_detail(self, job_soup):
        job = Job()
        job.job = job_soup.find('p' ,attrs={"class": "t1"}).text
        job.company_name = job_soup.find('span' ,attrs={"class": "t2"}).text
        job.publish_date = self.__zldate_parse(job_soup.find('span' ,attrs={"class": "t5"}).text)
        job.source = '51'
        return job

    def __zldate_parse(self, date):
        date_str = '2016-'+date
        return DateUtil.str_to_time(date_str, '%Y-%m-%d')

    def __insert_jobs(self, jobs):
        for i,job in enumerate(jobs):
            if job.publish_date <self.date:
                dao.insert_jobs(jobs[:i-1])
                raise Exception

        dao.insert_jobs(jobs)

if __name__ == '__main__':
    date = DateUtil.substract_day(DateUtil.now(), 1)
    crawler = FOCrawler(date)
    crawler.sample()
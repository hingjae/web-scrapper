from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = indeed_jobs + so_jobs
# print(indeed_jobs)
# print(so_jobs)
save_to_file(jobs)
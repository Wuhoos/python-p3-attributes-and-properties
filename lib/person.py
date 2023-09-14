#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Guido", job ="Legal") -> None:
        self.name = name
        self.job = job
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if (type(name_parameter) is str) and (1 <= len(name_parameter) <= 25):
            self._name = (name_parameter).title()
        else:
            print('Name must be string between 1 and 25 characters.')

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job_parameter):
        if job_parameter not in APPROVED_JOBS:
            print('Job must be in list of approved jobs.')
        else: 
            self._job = job_parameter

# p= Person(job="Benevolent dictator for life")
# print(p.job)
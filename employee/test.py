import json
import requests
import sys


class Lead():

    def get(self, url):
        url_type = 'person_url'
        input_json = json.loads(requests.get(url).text)
        if type(input_json)==list:
            url_type = 'list_of_persons_url'
        return self._format_json(input_json, url_type)

    def _format_json(self, input_json, url_type):
        if url_type == "person_url":
            return {
                "full_name": input_json['full_name'],
                "job_title": input_json['job_title'],
                "profile_url": input_json["profile_url"],
                "location": input_json['location'],
                "email": input_json['email'],
                "phone_number": input_json['phone_number']
            }
        elif url_type == "list_of_persons_url":
            list_of_persons = []
            for person in input_json:
                list_of_persons.append({
                    "full_name": person['full_name'],
                    "profile_url": person['profile_url']
                })
            return list_of_persons


class Company():

    def get(self, url):
        url_type = 'company_url'
        input_json = json.loads(requests.get(url).text)
        if type(input_json) == list:
            url_type = 'list_of_companies_url'
        return self._format_json(input_json, url_type)

    def _format_json(self, input_json, url_type):
        if url_type == "company_url":
            leads = []
            for item in input_json['employees']:
                url = 'http://127.0.0.1:8000/employee/' + str(item)
                lead = Lead()
                result = lead.get(url)
                leads.append(result)
            return {
                "name": input_json['name'],
                "company_url": input_json['company_url'],
                "location": input_json["location"],
                "revenue": input_json['revenue'],
                "leads": leads
            }
        elif url_type == "list_of_companies_url":
            list_of_companies = []
            for person in input_json:
                list_of_companies.append({
                    "name": person['name'],
                    "company_url": person['company_url']
                })
            return list_of_companies

if __name__ == '__main__':
    url = sys.argv[1]
    if 'employee' in url:
        lead = Lead()
        result = lead.get(url)
        print (result)
    elif 'company' in url:
        company = Company()
        result = company.get(url)
        print (result)



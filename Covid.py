import urllib.parse
import requests
import json

print('COVID-19 alert')
country_name = input('Enter country name : ').capitalize()
iso3_name = input('Enter the iso country name : ').lower()  # can, aus, tha

# Covid-19 Update

url_update = 'https://covid-19-data.p.rapidapi.com/country'

headers = {
    'x-rapidapi-key': 'e6a1bed72dmshbffa66c61907947p1ca1fejsn6d5bfdf20e76',
    'x-rapidapi-host': 'covid-19-data.p.rapidapi.com'
}

response = requests.request(
    'GET', url_update, headers=headers, params={'name': country_name})
result_update = response.json()
# print(result_update)


# print('---'*10)
# Covid-19 Vaccine

url_vaccine = 'https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/'+country_name+'/'+iso3_name
headers = {
    'x-rapidapi-key': 'e6a1bed72dmshbffa66c61907947p1ca1fejsn6d5bfdf20e76',
    'x-rapidapi-host': 'vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com'
}

response = requests.request('GET', url_vaccine, headers=headers)
result_vaccine = response.json()
# print(result_vaccine)
# print('---'*10)
# # Before vaccine
confirm_infected = result_update[0]['confirmed']
confirm_death_before = result_update[0]['deaths']

# # After Vaccine
amount_of_test = result_vaccine[0]['TotalTests']
confirm_death_after = result_vaccine[0]['NewDeaths']

print('---'*10)
print('Covid-19 Update')
print('%s currently has a total of %d people infected.' %
      (country_name, confirm_infected))
print('Prior to the vaccine, %s had a total of %d deaths.' %
      (country_name, confirm_death_before))

print('Perform a total of %d vaccinations.' % int(amount_of_test))

print('%s currently has a total of %d people deaths.' %
      (country_name, confirm_death_after))

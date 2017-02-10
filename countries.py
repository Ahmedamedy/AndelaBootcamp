import requests

def get_data(get_url, isocode):
	try:
		c = requests.get(get_url +str(isocode))
		return c
	except Exception e:
		print("ISO code")
		raise(e)
	return "* Nothing to show *"


def main():
	print("\n\t*** Andela BootCamp Day 3  ***\n\t%s\n" %("-"*31))
	print("***   Python HTTP API command line app  ***")
	print("Let's get a country through iso2code or two characters")
	url = "http://services.groupkt.com/country/search?text="
	isocode = input("ISO CODE eg.UG: ")
	print("\n\tGetting your Country...\n")
	get_c = get_data(url,isocode)
	countries = get_c.text

	countryall = countries.split("{}")
	country = countryall[0][176:-8]
	
	print country

if __name__ == '__main__':
	main()

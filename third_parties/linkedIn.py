import requests
import os
import dotenv

dotenv.load_dotenv()


def scrape_linkedIn_profile(url: str, moke: bool = False):
    """ Scrape Information from linkedIN profile"""
    response =  requests.get(url)

    response = {
        key: value for key, value in response.json().items() if value not in ["None", "", "", []]
        and key not in ["people_also_viewed", "certifications"]
    }
    keys = response.keys()
    print(f"Keys: {len(keys)}")
    return response




if __name__ == "__main__":
    url = "https://gist.githubusercontent.com/Aousaf90/4dff7a0e726b80a1ad77419a640aeb50/raw/daf0d6d4c981df9630c4929bd07997f56658fa76/gistfile1.txt"
    result = scrape_linkedIn_profile(url)
    # print(result)
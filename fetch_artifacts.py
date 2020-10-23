
import sys
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_input_from_user():

    repo_name = input("Enter the repo (release, master, prod):")
    lastbuildstartdaysbefore = input("Build created when (5minutes,10minutes,1d):")
    if repo_name not in ("release", "master", "prod"):
        print("Wrong input")
        sys.exit(1)
    else:
        return repo_name, lastbuildstartdaysbefore


def construct_query(repo_name, lastbuildstartdaysbefore):
    data = list()
    with open(r'configs/artif_other_config.json', 'r') as file:
        config = json.load(file)

    for c in config['files']:
        data.append('items.find({"repo":{"$match":"' + config['prefix'] + repo_name + '"},"name":{"$match":"' + c + '"},"created":{"$last":"' + lastbuildstartdaysbefore + '"}}).include("name","path","repo","created","actual_sha1","original_sha1")')

    data.append('items.find({"repo":{"$match":"' + config['prefix_image'] + repo_name + '"},"name":{"$match":"' + config["files_image"] + '"},"created":{"$last":"' + lastbuildstartdaysbefore + '"}}).include("name","path","repo","created","actual_sha1","original_sha1")')
    return data


def fetch_files(data):

    with open(r'configs/artif_config.json', 'r') as fd:
        config = json.load(fd)

    for datum in data:
        response = requests.post(config["url"], auth=(config["username"], config["password"]), headers=headers, data=datum, verify=False)
        response_json = response.json()
        response_list = response_json['range']['total']
        if response_list != 0:
            for my_list_index in range(int(response_list)):
                print(response_json['results'][my_list_index]['name'], " ", response_json['results'][my_list_index]['created'], " ", response_json['results'][my_list_index]['actual_sha1'])
            print("-----------------" * 2)


if __name__ == "__main__":
    headers = {
        'content-type': 'text/plain',
    }
    my_repo, my_sinceday = get_input_from_user()
    query = construct_query(my_repo, my_sinceday)
    fetch_files(query)
    input("Press any key to continue...")

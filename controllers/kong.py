from flask import Flask, make_response, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_urls = os.getenv('API_URLS').split(',')
api_urls_routes = [url + '/routes' for url in api_urls]
print(api_urls_routes)


def get_paths():
    all_data = []
    for api_url in api_urls_routes:
        data = fetch_data(api_url,'/routes')
        if data:
            for entry in data:
                paths = entry.get('paths', [])
                svc   = entry.get('name', [])
#                name  = entry.get('core-svc-bo',[])
                if paths is None:
                    continue
                for path in paths:
                    ports_url = api_url.split('/routes')[0] + f"/upstreams/{entry['name']}/targets"
                    print(ports_url)
                    try:
                        ports = get_ports(ports_url) 
                        all_data.append({'url': api_url,'svc': svc, 'path': path, 'port': ports})
                    except:
                        all_data.append({'url': api_url,'svc': svc, 'path': path, 'port': 'null' })
    resp = make_response(jsonify(all_data))
    return resp


def fetch_data(api_url,api_path):   
    all_data = []
    next_url = api_url

    while next_url:
        try:
            response = requests.get(next_url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            json_response = response.json()
            data = json_response.get('data', [])
            if data is not None:
                all_data.extend(data)
            next_url = json_response.get('next', None)
            if next_url:
                # Construct the full URL for the next page if it is not already a full URL
                if not next_url.startswith('http'):
                    next_url = api_url.split(api_path)[0] + next_url
                    print(next_url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {api_url}: {e}")
            break
    return all_data

def get_ports(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        json_response = response.json()
        targets = json_response.get('data', [])
        if not targets:  # If the 'data' list is empty, return null (None in Python)
            return None
        
        port = []
        for target in targets:
            target_str = target.get('target', '')
            # Extract the port using split
            if ':' in target_str:
                port = target_str.split(':')[1]
                # ports.append(port)
        return port if port else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return []

def get_svc():
    path_filter = request.args.get('path')
    port_filter = request.args.get('port')
    
    all_data = []
    for api_url in api_urls_routes:
        data = fetch_data(api_url,'/routes')
        if data:
            for entry in data:
                paths = entry.get('paths', [])
                svc   = entry.get('name', [])
#                name  = entry.get('core-svc-bo',[])
                if paths is None:
                    continue
                for path in paths:
                    ports_url = api_url.split('/routes')[0] + f"/upstreams/{entry['name']}/targets"
                    print(ports_url)
                    ports = get_ports(ports_url)
                    all_data.append({'url': api_url,'svc': svc, 'path': path, 'port': ports})
    
    # Apply filters if provided
    if path_filter:
        all_data = [item for item in all_data if path_filter.lower() in item['path'].lower()]
    if port_filter:
        all_data = [item for item in all_data if port_filter in item['port']]
    
    return jsonify(all_data)
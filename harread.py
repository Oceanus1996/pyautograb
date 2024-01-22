import json
import os

def merge_har_to_txt(har_files_paths, output_file_path, exclude_host=None):
    processed_urls = set()  # 用于存储已处理的URL

    with open(output_file_path, 'w') as output_file:
        for har_file_path in har_files_paths:
            with open(har_file_path, 'r', encoding='utf-8-sig') as file:
                har_data = json.load(file)

            for entry in har_data['log']['entries']:
                request = entry['request']
                response = entry['response']
                url = request['url']
                host = None

                # 遍历请求头字典，查找主机信息
                for header in request['headers']:
                    if header['name'].lower() == 'host':
                        host = header['value']
                        break  # 找到主机后可以跳出循环

                # 检查筛选条件
                if (('authorize' in url or 'login' in url) and
                   (exclude_host is None or (host is not None and exclude_host not in host))):

                    # 检查URL是否已处理过，如果是则跳过
                    if url in processed_urls:
                        break  # 使用break跳出当前的循环

                    # 将URL添加到已处理的URL集合中
                    processed_urls.add(url)

                    output_file.write(f"URL: {url}\n")
                    output_file.write(f"Method: {request['method']}\n")
                    output_file.write(f"Status: {response['status']} {response['statusText']}\n")

                    output_file.write("Request Headers:\n")
                    for header in request['headers']:
                        output_file.write(f"  {header['name']}: {header['value']}\n")

                    output_file.write("Response Headers:\n")
                    for header in response['headers']:
                        output_file.write(f"  {header['name']}: {header['value']}\n")

                    output_file.write("\n")  # 在每个请求之间添加一个空行以便阅读


# 替换为您的HAR文件路径列表、输出TXT文件路径以及要排除的主机
har_files_paths = [
    '/Users/icfem/PycharmProjects/pythonProject3/folder/5.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/15.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/25.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/35.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/45.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/55.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/65.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/75.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/86.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/95.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/105.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/116.har',
'/Users/icfem/PycharmProjects/pythonProject3/folder/130.har',



]
output_file_path = '/Users/icfem/PycharmProjects/pythonProject3/output.txt'
exclude_host = 'excluded-host.com'  # 如果主机包含此数据，则排除，可以设为None以禁用

merge_har_to_txt(har_files_paths, output_file_path, exclude_host)
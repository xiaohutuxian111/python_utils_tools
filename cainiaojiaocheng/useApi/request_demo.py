"""
@FileName：request_demo.py
@Author：stone
@Time：2023/4/20 10:09
@Description:
"""
import pygal
import pylab
import requests
import matplotlib.pyplot as plt
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
resp = requests.get(url)

if resp.status_code == 200:

    #  将相应存储到处理节点中
    response_dict = resp.json()
    #  处理结果
    print(response_dict.keys())
    print("total n repositories:{}".format(response_dict["total_count"]))

    # 探索有关仓库信息
    repo_dicts = response_dict["items"]
    print("Repositories returned:", len(repo_dicts))

    # 研究第一个仓库
    # repo_dict = repo_dicts[0]
    # print("key:".format(len(repo_dict)))
    # for key in sorted(repo_dict.keys()):
    #     print(key)

    names = []
    starts = []

    print("\nSelected information about first repository:")
    for repo_dict in repo_dicts:
        print('Name:', repo_dict['name'])
        print('Owner:', repo_dict['owner']['login'])
        print('Stars:', repo_dict['stargazers_count'])
        print('Repository:', repo_dict['html_url'])
        print('Created:', repo_dict['created_at'])
        print('Updated:', repo_dict['updated_at'])
        print('Description:', repo_dict['description'])
        names.append(repo_dict['name'])
        starts.append(repo_dict['stargazers_count'])

    # 可视化
    # my_style = LS('#333366', base_style=LCS)
    # chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    # chart.title = 'Most-Starred Python Projects on GitHub'
    # chart.x_labels = names
    # chart.add("", starts)
    # chart.render_to_file("demo.svg")

    fig, ax = plt.subplots()
    ax.bar(names, starts, width=1, edgecolor="white", linewidth=0.7)
    plt.show()






import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from collections import Counter
import random
import pathlib


def get_one_page(url):
    response = requests.get(url)
    while response.status_code == 403:
        print('Response code:', response.status_code)
        time.sleep(500 + random.uniform(0, 500))
        response = requests.get(url)
    print('Response code:', response.status_code)
    if response.status_code == 200:
        return response.text
    return None


def process_raw():
    url = 'https://arxiv.org/list/cs/pastweek?show=1000'
    html = get_one_page(url)
    soup = BeautifulSoup(html, features='html.parser')
    content = soup.dl
    # date = soup.find('h3')
    list_ids = content.find_all('a', title='Abstract', href=True)
    list_title = content.find_all('div', class_='list-title mathjax')
    list_authors = content.find_all('div', class_='list-authors')
    list_subjects = content.find_all('div', class_='list-subjects')
    list_subject_split = []
    for subjects in list_subjects:
        subjects = subjects.text.split(': ', maxsplit=1)[1]
        subjects = subjects.replace('\n\n', '')
        subjects = subjects.replace('\n', '')
        subject_split = subjects.split('; ')
        list_subject_split.append(subject_split)
    return list_ids, list_title, list_authors,\
        list_subjects, list_subject_split


def get_collections(key_words, Key_words, paper, collections='default',
                    save_collections=True):
    '''key_word selection'''
    selected_papers = pd.DataFrame()
    for key_word in key_words:
        selected_paper = paper[paper['title'].str.contains(key_word,
                                                           case=False)]
        selected_papers = pd.concat([selected_papers, selected_paper], axis=0)
    for Key_word in Key_words:
        selected_papers_case = paper[paper['title'].str.contains(Key_word,
                               case=True)]
    for key_word in key_words:
        selected_paper_subjects = paper[paper['subjects'].str.contains(key_word,
                                                           case=False)]
        selected_papers = pd.concat([selected_papers, selected_papers_case, selected_paper_subjects], axis=0)
    if save_collections:
        path = 'data/arxiv_{}/'.format(collections)
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        selected_papers.to_json(path+time.strftime("%Y-%m-%d")+'_'
                                + str(len(selected_papers))+'.json',
                                orient='records')
    return selected_papers.to_dict(orient='records')


def get_sbj(list_subject_split, items):
    '''subject split'''
    subject_all = []
    for subject_split in list_subject_split:
        for subject in subject_split:
            subject_all.append(subject)
    subject_cnt = Counter(subject_all)
    # print(subject_cnt)
    subject_items = []
    for subject_name, times in subject_cnt.items():
        subject_items.append([subject_name, times])
    subject_items = sorted(subject_items,
                           key=lambda subject_items: subject_items[1],
                           reverse=True)
    name = ['name', 'times']
    subject_file = pd.DataFrame(columns=name, data=subject_items)
    # subject_file = pd.DataFrame.from_dict(subject_cnt, orient='index')
    path = './data/arxiv_sub_cnt/'
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    subject_file.to_json(path+time.strftime("%Y-%m-%d")+'_'
                         + str(len(items))+'.json')
    # subject_file.to_html('subject_file.html')


def get_arxiv_papers(save_papers=True, save_sbj=True, save_collections=True):
    list_ids, list_title, list_authors, list_subjects,\
        list_subject_split = process_raw()
    items = []
    for _, paper in enumerate(zip(list_ids, list_title, list_authors,
                                  list_subjects, list_subject_split)):
        items.append([paper[0].text, paper[1].text.replace('\nTitle: ', ''), paper[2].text.replace('\nAuthors: ', ''),
                      paper[3].text.replace('\nSubjects: ', ''), paper[4], "https://arxiv.org" + paper[0]['href']])
    name = ['id', 'title', 'authors', 'subjects', 'subject_split', 'link']
    paper = pd.DataFrame(columns=name, data=items)
    if save_papers:
        path = './data/arxiv_daily/'
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        paper.to_json(path+time.strftime("%Y-%m-%d")+'_'
                      + str(len(items))+'.json')
    if save_sbj:
        get_sbj(list_subject_split, items)

    key_words = ['optimal control', 'non-linear control', 'nonlinear control', 'robotics', 'Systems and Control', 'Optimization and Control']
    Key_words = ['Koopman', 'Systems and Control']

    # key_words = ['track', 'occlu', 'multiple object', 'multiple target',
    #              'multi-object', 'multi-target', 'people', 'person',
    #              'pedestrian', 'human', 'siam']
    # Key_words = ['MOT', 'SOT']
    # key_words2 = ['quantization', 'compress', 'prun']
    # Key_words2 = ['MOT']

    # return {
    #     'MOT': get_collections(key_words, Key_words, paper, 'Det',
    #                            save_collections=save_collections),
    #     'SOT': get_collections(key_words2, Key_words2, paper, 'MOT',
    #                            save_collections=save_collections)}
    return {'meta':get_collections(key_words, Key_words, paper, 'Det',
            save_collections=save_collections),}

def main():
    get_arxiv_papers()


if __name__ == '__main__':
    main()

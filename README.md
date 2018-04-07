# sentiment-analysis-webapp

[![Python](https://img.shields.io/badge/python-3.5%2B-green.svg)]()
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/bighuang624/sentiment-analysis-webapp/blob/master/LICENSE)

中文短文本情感分析 web 应用 | A web app about Chinese sentences sentiment analysis

![example.png](https://raw.githubusercontent.com/bighuang624/sentiment-analysis-webapp/master/docs/example.png)

## Installation

### Clone the repo

```shell
$ git clone git@github.com:bighuang624/sentiment-analysis-webapp.git
```

### Enter the directory

```shell
$ cd sentiment-analysis-webapp
```

### Install requirements

```shell
$ pip install -r requirements.txt
```

### Run with Python

Only support Python 3.5+ temporarily.

```shell
$ python app.py
```

### Play

Open index.html and have fun.  :smiley:

## Structure

```
.
├── LICENSE
├── README.md
├── app.py
├── index.html
├── models
│   ├── douban_comment.pkl
│   └── restaurant_comment.pkl
├── requirements.txt
├── static
└── training
    ├── douban-comment.csv
    ├── douban_comment_trainning.py
    ├── restaurant-comment.csv
    └── restaurant_comment_trainning.py
```

The source code of the frontend can be found in [sentiment-analysis-webapp-frontend](https://github.com/bighuang624/sentiment-analysis-webapp-frontend), which is powered by Vue.js.

## Contributors

This work is doing by Siteng Huang, Muzhe Zhou, Ziyi Wu, Zhongchao Cai, Xu Zheng and Suyang Hu.

## Thanks

Inspired by [mtobeiyf / keras-flask-deploy-webapp](https://github.com/mtobeiyf/keras-flask-deploy-webapp).

## License

Licensed under the [MIT License](https://github.com/bighuang624/sentiment-analysis-webapp/blob/master/LICENSE).
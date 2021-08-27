import json
from datetime import datetime, timedelta

import requests
from django.shortcuts import render

from astro.admin import Prev30


def home(request):
    carousel = {
        'image': '',
        'caption_title': '',
        'caption_info': ''
    }
    carousels = [{
        'images': {
            'pc': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/im1.jpg?raw=true',
            'mob': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/im1m.jpg?raw=true'
        },
        'caption_title': 'We are Astro Club,VNIT',
        'caption': 'Are you one of those Space buffs? Wanna hone you amateur skills in Astronomy? Look no'
                   ' further you have reached your destination! Welcome to Astro Club VNIT!'
    }, {
        'images': {
            'pc': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/im2.jpg?raw=true',
            'mob': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/im2m.jpg?raw=true'
        },
        'caption_title': 'Sky is the limit',
        'caption': 'Have a look at this beautiful image🤩, capturing the Star trails, taken by our club '
                   'member Ojas Sharma.'
    },
        {
            'images': {
                'pc': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/im4.jpg?raw=true',
                'mob': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/im4m.jpg?raw=true'
            },
            'caption_title': '',
            'caption': 'Astronomy Club of VNIT, Ashlesha invites you to gaze upon the heavens and beyond and see'
                       ' the unfolding of the cosmic miracle.'
        }
    ]
    context = {
        'carousels': carousels
    }
    context['carousels'][0]['active'] = 'active'
    return render(request, 'index.html', context)


def about(request):
    carousel = {
        'image': '',
        'caption_title': '',
        'caption_info': ''
    }
    context = {
        'carousels': [
            {
                'image': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/about%201.jpg?raw=true',
                'caption_title': '',
                'caption_info': ''
            },
            {
                'image': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/about%202.jpg?raw=true',
                'caption_title': '',
                'caption_info': ''
            }
            ,
            {
                'image': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/about%203.jpg?raw=true',
                'caption_title': '',
                'caption_info': ''
            }
            ,
            {
                'image': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/about%204.jpg?raw=true',
                'caption_title': '',
                'caption_info': ''
            }
            ,
            {
                'image': 'https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/about%205.jpg?raw=true',
                'caption_title': '',
                'caption_info': ''
            }
        ]
    }
    context['carousels'][0]['active'] = 'active'
    return render(request, 'about.html', context)


def events(request):
    event = {
        'title': '',
        'description': '',  # can use basic html here
        'main_link_desc': '',
        'main_link': '',  # write if any else blank
        'additional links': [

        ]  # has  dicts of format {'description' : '','link_addr' :''}

    }
    context = {
        'events': []
    }

    if len(context['events']) != 0:
        context['events'][0]['active'] = 'active'
        return render(request, 'events.html', context)
    else:
        return render(request, 'noevents.html')


def other_sources(request):
    context = {

    }
    return render(request, 'otherSources.html', context)


def apod(request):
    api_url = 'https://api.nasa.gov/planetary/apod'
    my_key = 'gE4OwsHm4NSF3efofSsGRvxcJeT3abrR05xk3Usd'
    context = {
        'prev_30': [],  # array of objects of the form img_info
        'active': ''
    }

    if len(Prev30.objects.all()) == 0 or len(
            Prev30.objects.all().filter(date=(datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'))) == 0:
        todays_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        date_month_before = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
        print(date_month_before, todays_date)
        response = requests.get(f'{api_url}?start_date={date_month_before}&end_date={todays_date}&api_key={my_key}')
        context['prev_30'] = json.loads(response.text)[::-1]
        print(type(context['prev_30']))
        print(context['prev_30'])
        for obj in Prev30.objects.all():
            obj.delete()
        for i in context['prev_30']:
            entry = Prev30()
            print(i)
            entry.url = i['url']
            entry.date = i['date']
            entry.title = i['title']
            entry.explanation = i['explanation']
            entry.save()

    else:
        todays_date = datetime.today() - timedelta(days=1)
        for day_back in range(0, 29):
            try:
                entry = Prev30.objects.all().filter(date=(todays_date - timedelta(day_back)).strftime('%Y-%m-%d'))[0]
                new_context_data = dict()
                new_context_data['url'] = entry.url
                new_context_data['date'] = entry.date
                new_context_data['title'] = entry.title
                new_context_data['explanation'] = entry.explanation
                context['prev_30'].append(new_context_data)
            except:
                print('not found for today')
    context['prev_30'][0]['active'] = 'active'
    return render(request, 'apod.html', context)


def articles(request):
    context = {
        "articles": [],

    }
    article1 = {
        "id": 1,
        "link": "/article/1",
        "drive_link": "https://drive.google.com/file/d/1NY32LkuJgIDEJYgko3z5GzzQ-B7mOfhx/view?usp=sharing",
        "title": "STELLAR CLASSIFICATION",
        "summary": '''&emsp;Stellar classification is the classification of stars according to their size,
temperature and spectral characteristics. According to the much used MorganKeenan table, the classification of stars has evolved into seven different classes or
groups. This system was created by Annie Jump Cannon, an American
Astronomer. Cannon developed this system on the basis of Balmer spectral lines,
later characterization according to size and temperature were approached. The
seven groups are O, B, A, F, G, K and M.''' + '<br/><br/>' + '''&emsp;Stars classified in the 'O' group are the most massive and hottest, with
temperatures exceeding 30,000°C, while those in the 'M' group are the smallest
and coolest, with temperatures less than 3,000°C.
A star with a really high temperature is a Blue star while those quite the smallest
ones are Red stars. Hence colour of the star is dependent on its Size and
Temperature. This is similar to what we observe with the black bodies at very high
temperatures. Usually most blue stars are very hot and are therefore classed as
'O' stars, while the coolest are red stars, and are classified into the 'M' class.''',
        "cover_image": "https://raw.githubusercontent.com/Darshan110801/VNIT-Astronomy-Club-Website/master/static/images/800px-Morgan-Keenan_spectral_classification.png",
        "images": [
            "https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/Stellar%20Classification%20Coverpage.jfif?raw=true",
            "https://raw.githubusercontent.com/Darshan110801/VNIT-Astronomy-Club-Website/master/static/images/800px-Morgan-Keenan_spectral_classification.png",
            "https://github.com/Darshan110801/VNIT-Astronomy-Club-Website/blob/master/static/images/hr-diagram-credit-nso.png?raw=true",

        ],
        "date": "July 27, 2021"

    }
    context['articles'].append(article1)
    return render(request, "articles.html", context)


def article(request, num):
    articles_table = {
        1: "Articles/stellar_Classification_final.html"

    }
    return render(request, articles_table[num])

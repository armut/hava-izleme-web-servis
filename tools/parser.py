import requests
import mechanicalsoup
from bs4 import BeautifulSoup

URL = 'http://havaizleme.gov.tr/frmStationReport.aspx'

station_dict = {
   '3': 'Adana - Çatalan',
   '2': 'Adana - Doğankent',
   '1': 'Adana - Meteoroloji',
   '4': 'Adana - Valilik',
   '5': 'Adıyaman',
   '6': 'Afyon',
   '7': 'Ağrı',
   '225': 'Ağrı - Doğubeyazıt',
   '224': 'Ağrı - Patnos',
   '87': 'Aksaray',
   '8': 'Amasya',
   '193': 'Amasya - Merzifon',
   '199': 'Amasya - Suluova',
   '198': 'Amasya - Şehzade',
   '9': 'Ankara - Bahçelievler',
   '16': 'Ankara - Cebeci',
   '10': 'Ankara - Demetevler',
   '11': 'Ankara - Dikmen',
   '12': 'Ankara - Kayaş',
   '13': 'Ankara - Keçiören',
   '14': 'Ankara - Sıhhıye',
   '15': 'Ankara - Sincan',
   '17': 'Antalya',
   '94': 'Ardahan',
   '18': 'Artvin',
   '219': 'Artvin - Hopa',
   '19': 'Aydın',
   '20': 'Balıkesir',
   '168': 'Balıkesir - Bandırma-MTHM',
   '169': 'Balıkesir - Erdek-MTHM',
   '255': 'Balıkesir - Erdemit - MTHM',
   '254': 'Balıkesir - Merkez - MTHM',
   '93': 'Bartın',
   '91': 'Batman',
   '88': 'Bayburt',
   '21': 'Bilecik',
   '160': 'Bilecik - Bozoyuk-MTHM',
   '22': 'Bingöl',
   '23': 'Bitlis',
   '24': 'Bolu',
   '25': 'Burdur',
   '26': 'Bursa',
   '164': 'Bursa - Beyazıt Cad.-MTHM',
   '167': 'Bursa - İnegöl-MTHM',
   '163': 'Bursa - Kültür Park-MTHM',
   '165': 'Bursa - Uludağ Üniv.-MTHM',
   '27': 'Çanakkale',
   '120': 'Çanakkale - Biga İçdaş',
   '175': 'Çanakkale - Can-MTHM',
   '174': 'Çanakkale - Lapseki-MTHM',
   '28': 'Çankırı',
   '29': 'Çorum',
   '196': 'Çorum - Bahabey ',
   '192': 'Çorum - Mimar Sinan',
   '30': 'Denizli - Bayramyeri',
   '31': 'Denizli - Merkezefendi',
   '32': 'Diyarbakır',
   '100': 'Düzce',
   '33': 'Edirne',
   '170': 'Edirne - Karaağaç-MTHM',
   '171': 'Edirne - Keşan-MTHM',
   '34': 'Elazığ',
   '130': 'EMEP - Ankara Çubuk',
   '133': 'EMEP - İzmir Seferihisar',
   '134': 'EMEP - Kırklareli Vize',
   '35': 'Erzincan',
   '213': 'Erzincan - Trafik',
   '36': 'Erzurum',
   '215': 'Erzurum - Aziziye',
   '212': 'Erzurum - Palandöken',
   '217': 'Erzurum - Pasinler',
   '214': 'Erzurum - Taşhan',
   '37': 'Eskişehir',
   '38': 'Gaziantep',
   '39': 'Giresun',
   '185': 'Giresun - Gemilercekeği',
   '40': 'Gümüşhane',
   '41': 'Hakkari',
   '42': 'Hatay - Antakya',
   '43': 'Hatay - İskenderun',
   '95': 'Iğdır',
   '216': 'Iğdır - Aralık',
   '44': 'Isparta',
   '45': 'İçel',
   '102': 'İstanbul - Aksaray',
   '108': 'İstanbul - Alibeyköy',
   '204': 'İstanbul - Avcılar',
   '144': 'İstanbul - Başakşehir-MTHM',
   '110': 'İstanbul - Besiktaş',
   '131': 'İstanbul - Büyükada',
   '205': 'İstanbul - Çatladıkapı',
   '103': 'İstanbul - Esenler',
   '143': 'İstanbul - Esenyurt-MTHM',
   '135': 'İstanbul - Göztepe',
   '101': 'İstanbul - Kadiköy',
   '132': 'İstanbul - Kağıthane',
   '141': 'İstanbul - Kağıthane-MTHM',
   '136': 'İstanbul - Kandilli',
   '149': 'İstanbul - Kandilli-MTHM',
   '105': 'İstanbul - Kartal',
   '207': 'İstanbul - Kumköy',
   '137': 'İstanbul - Maslak',
   '146': 'İstanbul - Mecidiyeköy-MTHM',
   '106': 'İstanbul - Sarıyer',
   '206': 'İstanbul - Selimiye',
   '139': 'İstanbul - Silivri-MTHM',
   '142': 'İstanbul - Sultanbeyli-MTHM',
   '140': 'İstanbul - Sultangazi-MTHM',
   '138': 'İstanbul - Şile-MTHM',
   '147': 'İstanbul - Şirinevler-MTHM',
   '107': 'İstanbul - Ümraniye',
   '145': 'İstanbul - Ümraniye-MTHM',
   '104': 'İstanbul - Üsküdar',
   '148': 'İstanbul - Üsküdar-MTHM',
   '109': 'İstanbul - Yenibosna',
   '114': 'İzmir - Alsancak',
   '117': 'İzmir - Bayrakli',
   '112': 'İzmir - Bornova',
   '115': 'İzmir - Çigli',
   '46': 'İzmir - Gaziemir',
   '113': 'İzmir - Güzelyalı',
   '111': 'İzmir - Karşıyaka',
   '116': 'İzmir - Sirinyer',
   '61': 'Kahramanmaraş',
   '62': 'Kahramanmaraş - Elbistan',
   '97': 'Karabük',
   '128': 'Karabük - Kardemir 1',
   '129': 'Karabük - Kardemir 2',
   '89': 'Karaman',
   '47': 'Kars - İstasyon Mah.',
   '223': 'Kars - Trafik',
   '48': 'Kastamonu',
   '50': 'Kayseri - Hürriyet',
   '49': 'Kayseri - Melikgazi',
   '51': 'Kayseri - OSB',
   '90': 'Kırıkkale',
   '52': 'Kırklareli',
   '172': 'Kırklareli - Limanköy-MTHM',
   '173': 'Kırklareli - Lüleburgaz-MTHM',
   '53': 'Kırşehir',
   '98': 'Kilis',
   '118': 'Kocaeli',
   '152': 'Kocaeli - Alikahya-MTHM',
   '54': 'Kocaeli - Dilovası',
   '209': 'Kocaeli - Dilovası-İMES OSB 1-MTHM',
   '211': 'Kocaeli - Dilovası-İMES OSB 2-MTHM',
   '250': 'Kocaeli - Gebze - MTHM',
   '251': 'Kocaeli - Gebze OSB - MTHM',
   '153': 'Kocaeli - Gölcük-MTHM',
   '150': 'Kocaeli - İzmit-MTHM',
   '155': 'Kocaeli - Kandıra-MTHM',
   '151': 'Kocaeli - Körfez-MTHM',
   '55': 'Kocaeli - OSB',
   '154': 'Kocaeli - Yeniköy-MTHM',
   '56': 'Konya - Meram',
   '57': 'Konya - Selçuklu',
   '179': 'Konya-Karatay-Belediye',
   '178': 'Konya-Selçuklu-Belediye',
   '58': 'Kütahya',
   '59': 'Malatya',
   '60': 'Manisa',
   '126': 'Manisa - Soma',
   '63': 'Mardin',
   '64': 'Muğla - Musluhittin',
   '65': 'Muğla - Yatağan',
   '66': 'Muş',
   '67': 'Nevşehir',
   '68': 'Niğde',
   '187': 'Ordu - Fatsa',
   '186': 'Ordu - Karşıyaka',
   '69': 'Ordu - Stadyum',
   '188': 'Ordu - Ünye',
   '99': 'Osmaniye',
   '70': 'Rize',
   '218': 'Rize - Ardeşen',
   '71': 'Sakarya',
   '256': 'Sakarya - Hendek OSB - MTHM',
   '158': 'Sakarya - Merkez-MTHM',
   '159': 'Sakarya - Ozanlar-MTHM',
   '190': 'Samsun - Atakum',
   '191': 'Samsun - Bafra',
   '189': 'Samsun - Canik',
   '72': 'Samsun - İlkadım Hastane',
   '73': 'Samsun - Tekkeköy',
   '197': 'Samsun - Yüzüncüyıl',
   '121': 'Seyyar - 1 (06 THL 77) - Kayseri Şeker Fabrikası',
   '122': 'Seyyar - 2 (06 THL 79) - İzmir Pınarbaşı',
   '127': 'Seyyar - 4 (06 DV 9975) - Zonguldak Çatalazğı',
   '74': 'Siirt',
   '75': 'Sinop',
   '202': 'Sinop - Boyabat',
   '200': 'Sinop - Erfelek',
   '201': 'Sivas - Başöğretmen',
   '194': 'Sivas - İstasyonkavşağı',
   '76': 'Sivas - Meteoroloji',
   '82': 'Şanlıurfa',
   '92': 'Şırnak',
   '77': 'Tekirdağ',
   '157': 'Tekirdağ - Çerkezköy-MTHM',
   '252': 'Tekirdağ - Çorlu - MTHM',
   '253': 'Tekirdağ - Çorlu OSB - MTHM',
   '156': 'Tekirdağ - Merkez-MTHM',
   '78': 'Tokat',
   '184': 'Tokat - Erbaa',
   '195': 'Tokat - Meydan',
   '183': 'Tokat - Turhal',
   '221': 'Trabzon - Akçaabat',
   '220': 'Trabzon - Beşirli',
   '222': 'Trabzon - Fatih',
   '80': 'Trabzon - Meydan',
   '226': 'Trabzon - Uzungöl',
   '79': 'Trabzon - Valilik',
   '81': 'Tunceli',
   '83': 'Uşak',
   '84': 'Van',
   '96': 'Yalova',
   '161': 'Yalova - Altınova-MTHM',
   '162': 'Yalova - Armutlu-MTHM',
   '85': 'Yozgat',
   '86': 'Zonguldak',
   '258': 'Zonguldak - Eren Enerji Lise',
   '249': 'Zonguldak - Eren Enerji Santral',
   '257': 'Zonguldak - Eren Enerji Tepeköy',
   '119': 'Zonguldak - Karadeniz Ereğli',
}

def get_stations():
    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
    )

    browser.open(URL)
    page = browser.get_current_page()
    s = page.find('select', attrs={'id': 'ddlStation'})
    ops = s.find_all('option')
    return [(op['value'], op.string) for op in ops]

def parser(station, date, valid_metrics=['PM10', 'SO2', 'NO2', 'CO', 'O3']):
    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
    )

    browser.open(URL)
    form = browser.select_form('#form1')
    form.set('RadioButtonList1', '0')
    form.set('RadioButtonList2', '0')
    #form.set_select({'ddlPurpose': '-1'})
    form.set_select({'ddlRegion': '-1'})
    form.set_select({'ddlStation': str(station)})
    form.set('BasicDatePicker1$TextBox', date)
    r = browser.submit_selected()

    html_table = r.text
    page = browser.get_current_page()
    data = []
    table = page.find('table', attrs={'id': 'C1WebGrid1'})
    rows = table.find_all('tr')

    valid_metrics = valid_metrics
    available_metrics = {}
    headers = rows[0].find_all('td')
    for i, header in enumerate(headers):
        if header.string in valid_metrics:
            available_metrics[i] = header.string

    result = {
        'station_no': station,
        'station_name': station_dict.get(station),
        'date': date,
    }
    
    measurements = []
    for row in rows[2:]:
        metrics = {}
        values = row.find_all('td')
        for i, value in enumerate(values):
            if i == 0:
                metrics['time'] = value.string.split(' ')[1]

            if available_metrics.get(i):
                metrics[available_metrics.get(i)] = value.string
        measurements.append(metrics)
    
    result['measurements'] = measurements
    return result

def generate_station_dict():
    stations = get_stations()
    for station in stations:
        with open('stations', 'a') as f:
            f.write('\'' + station[0] + '\': \'' + station[1] + '\',\n')


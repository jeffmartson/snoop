#! /usr/bin/env python3
# Copyright (c) 2020 Snoop Project <snoopproject@protonmail.com>
"Text_banner_logo_help"

import base64
import click
import json
import locale
import os
import platform
import sys
import time
import webbrowser

from colorama import Fore, Style, init
from rich.panel import Panel
from rich.style import Style as STL
from rich.console import Console
from rich.table import Table

locale.setlocale(locale.LC_ALL, '')
init(autoreset=True)
console = Console()


## Логирование ошибок.
def err_all(err_="low"):
    if err_ == "high":
        err_log = ("⚠️ [bold red][RU] Внимание! Критическая ошибка, просьба сообщить об этом разработчику.\n" + \
                   "[EN] Attention! Critical error, please report it to the developer.\nhttps://github.com/snooppr/snoop/issues[/bold red]")
    elif err_ == "low":
        err_log = ("⚠️ [bold yellow][RU] Ошибка | [EN] Error[/bold yellow]")
    return err_log


## БД.
def DB(db_base):
    try:
        with open(db_base, "r", encoding="utf8") as f_r:
            db = f_r.read()
            db = db.encode("UTF-8")
            db = base64.b64decode(db)
            db = db[::-1]
            db = base64.b64decode(db)
            trinity = json.loads(db.decode("UTF-8"))
            return trinity
    except Exception:
        print(Style.BRIGHT + Fore.RED + "Упс, что-то пошло не так..." + Style.RESET_ALL)
        sys.exit()


## Пожертвование.
def donate():
    print("")
    console.print(Panel(f"""[cyan]
╭donate/Buy:
├──Яндекс.Деньги (Юmoney):: [white]4100111364257544[/white]
├──Visa/Сберкарта:: [white]4276100015931808[/white]
├──Qiwi:: [white]https://qiwi.com/n/SNOOPPROJECT[/white]
└──PayPal:: [white]snoopproject@protonmail.com[/white]

[bold green]Если пользователя заинтересовало ПО [red]Snoop demo version[/red], то он может официально приобрести [cyan]Snoop full version[/cyan], поддержав развитие IT-проекта[/bold green] [bold cyan]20$[/bold cyan] [bold green]или[/bold green] [bold cyan]1400р.[/bold cyan]
[bold green]При пожертвовании/покупке в сообщении укажите информацию в таком порядке:[/bold green]

    [cyan]"Пожертвование на развитие Snoop Project: 20$ ваш e-mail
    full version for Windows RU или full version for Linux RU,
    статус пользователя: Физ.лицо; ИП; Юр.лицо (если покупка ПО)"[/cyan]

[bold green]В ближайшее время на email пользователя придёт чек и ссылка для скачивания Snoop full version готовой сборки то есть исполняемого файла, для Windows — это 'snoop_cli.exe', для GNU/Linux — 'snoop_cli'.

Snoop в исполняемом виде (build-версия) предоставляется по лицензии, с которой пользователь должен ознакомиться перед покупкой ПО.
Лицензия для Snoop Project в исполняемом виде находится в rar-архивах демо версий Snoop по ссылке: [/bold green]
[cyan]https://github.com/snooppr/snoop/releases[/cyan][bold green], также лицензия доступна по команде '[/bold green][cyan]snoop_cli -V[/cyan][bold green]' или '[/bold green][cyan]snoop_cli.exe -V[/cyan][bold green]' у исполняемого файла.

Если Snoop требуется вам для служебных или образовательных задач, напишите письмо на e-mail разработчика в свободной форме.
Студентам ПО Snoop full version предоставляется с 50% скидкой.

Snoop full version: плагины без ограничений; {len(DB('BDflag')) // 100}00+ Websites;
поддержка и обновление Database Snoop.
Подключение к Web_Database Snoop (online), которая расширяется/обновляется.[/bold green]
[bold red]Ограничения demo version: Websites (Database Snoop сокращена в > 15 раз);
отключены некоторые опции/плагины; необновляемая Database_Snoop.[/bold red]

[bold green]Email:[/bold green] [cyan]snoopproject@protonmail.com[/cyan]
[bold green]Исходный код:[/bold green] [cyan]https://github.com/snooppr/snoop[/cyan]

❗️[bold yellow] Обратите внимание, что из-за цензуры письма с 'mailru' и 'yandex' не доходят до 'protonmail'. Для пользователей mailru/yandex пишите запросы на запасную почту.[/bold yellow]
[bold green]Email: [/bold green][cyan]snoopproject@ya.ru[/cyan]""",
                        title="[bold red]demo: (Публичная оферта)",
                        border_style="bold blue"))

    try:
        if "arm" not in platform.platform(aliased=True, terse=0) and "aarch64" not in platform.platform(aliased=True, terse=0):
            webbrowser.open("https://qiwi.com/n/SNOOPPROJECT")
            webbrowser.open("https://sobe.ru/na/snoop_project_2020")
        else:
            click.pause(Style.DIM + Fore.CYAN + "\nНажмите любую клавишу для открытия web browser\n")
            click.launch(f"https://sobe.ru/na/snoop_project_2020")
            click.launch(f"https://qiwi.com/n/SNOOPPROJECT")
    except Exception:
        print("\033[31;1mНе удалось открыть браузер\033[0m")

    print(Style.BRIGHT + Fore.RED + "Выход")
    sys.exit()


## Лого.
def logo(text):
    if sys.platform != 'win32':
        with console.screen():
            console.print("""[cyan]
 ____                                      
/\  _`\                                    
\ \,\L\_\    ___     ___     ___   _____   
 \/_\__ \  /' _ `\  / __`\  / __`\/\ '__`\\
   /\ \L\ \/\ \/\ \/\ \_\ \/\ \_\ \ \ \L\ \\
   \ `\____\ \_\ \_\ \____/\ \____/\ \ ,__/
    \/_____/\/_/\/_/\/___/  \/___/  \ \ \/ 
                                     \ \_\\
      __                              \/_/ 
     /\ \                              
     \_\ \     __    ___ ___     ___   
     /'_` \  /'__`\/' __` __`\  / __`\\
    /\ \_\ \/\  __//\ \/\ \/\ \/\ \_\ \\
    \ \___,_\ \____\ \_\ \_\ \_\ \____/
     \/__,_ /\/____/\/_/\/_/\/_/\/___/ 
""")
            time.sleep(1.4)
    for i in text:
        time.sleep(0.04)
        print(f"\033[31;1m{i}", end='', flush=True)
    print("\033[31;1m\n\nВыход")
    sys.exit()


# snoop.py Справка Модули 'if mod == 'help'.
def help_module_1():
    print("""\033[32;1m└──[Справка]\033[0m

\033[32;1m========================
| Плагин GEO_IP/domain |
========================\033[0m \033[32m\n
1) Реализует онлайн одиночный поиск цели по IP/url/domain и предоставляет статистическую информацию: IPv4/v6; GEO-координаты/ссылку; локацию.
(Лёгкий ограниченный поиск).

2) Реализует онлайн поиск цели по списку данных: и предоставляет статистическую и визуализированную информацию: IPv4/v6; GEO-координаты/ссылки; страны/города; отчеты в CLI/txt/csv форматах; предоставляет визуализированный отчет на картах OSM.
(Умеренный небыстрый поиск: ограничения запросов:: 15к/час; не предоставляет информацию о провайдерах).

3) Реализует офлайн поиск цели по списку данных, используя БД: и предоставляет статистическую и визуализированную информацию: IPv4/v6; GEO-координаты/ссылки; локации; провайдеры; отчеты в CLI/txt/csv форматах; предоставляет визуализированный отчет на картах OSM.
(Сильный и быстрый поиск).

Результаты по 1 и 2 методу могут отличаться и быть неполными - зависит от персональных настроек DNS/IPv6 пользователя.
Список данных — текстовый файл (в кодировке utf-8), который пользователь указывает в качестве цели, и который содержит ip, domain или url (или их комбинации).

\033[32;1m============================
| Плагин Reverse Vgeocoder |
============================\033[0m\n
\033[32mОбратный геокодер для визуализации координат на карте OSM и статистическим анализом в csv/txt форматах.

Плагин умеет извлекать и обрабатывать координаты из любых зашумлённых текстовых файлов. Плагин реализует оффлайн поиск цели по заданным геокоординатам и предоставляет статистическую и визуализированную информацию.

С помощью данного плагина пользователь способен извлечь, визуализировать и проанализировать информацию о тысячах геокоординатах за несколько секунд.
Предназначение плагина — CTF.\033[0m

\033[32;1m========================
| Плагин Yandex_parser |
========================\033[0m\n
\033[32mПлагин позволяет получить информацию о пользователях Яндекс-сервисов:
Я_Отзывы; Я_Кью; Я_Маркет; Я_Музыка; Я_Дзен; Я_Диск; E-mail, Name.
И связать полученные данные между собой с высокой скоростью и масштабно.
Предназначение — OSINT.

Плагин разработан на идее и материалах уязвимости, отчёты были отправлены Яндексу в рамках программы «Охота за ошибками».
Попал в зал славы, получил финансовое вознаграждение, а Яндекс исправил 'ошибки' по своему усмотрению.

Подробнее о плагинах см. 'Общее руководство Snoop Project.pdf'.\033[0m""")
    console.rule("[bold red]Конец справки")


# snoopplugins.py Справка Модуль Reverse Vgeocoder 'elif Vgeo == "help"'.
def help_vgeocoder_vgeo():
    print("""\033[32;1m└──[Справка]\033[0m
\033[32m
В Snoop Project поддерживается два режима геокодирования:
[*] Метод '\033[32;1mПростой\033[0m\033[32m':: На карте OSM расставляются маркеры по координатам. Все маркеры подписаны геометками.
Для данного метода доступны сокращенные отчёты с геометками в html формате и статистической информацией в txt формате.

[*] Метод '\033[32;1mПодробный\033[0m\033[32m':: На карте OSM расставляются маркеры по координатам. Все маркеры подписаны геометками; странами; округами и городами.
Статистические отчёты (с расширенной геоинформацией, а также расчётом количественной информацией процентного соотношения) сохраняются с подробностями в [txt.html.csv] форматах.
Данный метод довольно точно расставляет маркеры с геометками, но подписывает их адресом к ближайшим населенным пунктам от 2000 человек.
Например, если пользователь загрузит для обработки, координаты указывающие в 500 метрах от г. Выкса (лес), то маркер на карте OSM встанет точно (в лесу), а подписан он будет примерно так: Координаты:55.3301 -42.2604::Страна:RU::Городской_округ_1:Nizjnij Novgorod::Городской_округ_2:Vyksa'. То есть метод работает на основе — 'Евклидово дерево'.

\033[32;1mПлагин Reverse Vgeocoder\033[0m \033[32m- работает в оффлайн режиме и укомплектован гео-БД (БД предоставляются под свободной лицензией от download.geonames.org/export/dump/). То есть для работы плагина не требуется сетевое соединение.

Для визуализации данных на карте OSM укажите (при запросе) текстовый файл с координатами в кодировке utf-8 (с расширением .txt или без расширения). Каждая точка координат (широта, долгота) с новой строки в файле (желательно).
Snoop довольно умён: распознаёт и выбирает геокоординаты через запятую, пробел'ы или делает интеллектуальную выборку, вычищая случайные строки.
Пример файла с координатами (как должен выглядеть файл с координатами, который необходимо указывать):
\033[36m
51.352, 108.625
55.466,64.776
52.40662,66.77631
53.028 -104.680
54.505    73.773
Москва55.75, 37.62 Калининград54.71, 20.51 Ростов-на-Дону47.23, 39.72
случайная_строка1, которая_будет обработана Казань 55.7734/49.1436
случайная строка2, которая не будет обработана
\033[0m\033[32m
По окончанию рендеринга откроется webrowser с визуальным результатом.
Все результаты сохраняются в '~/snoop/results/plugins/ReverseVgeocoder/*[.txt.html.csv]'.
Для статистической обработки информации (сортировка по странам/координатам/raw_данным) пользователь должен изучить отчёт в csv-формате.

Это удобный плагин, если пользователю необходимо, например, не только обработать геокоординаты, но и найти хаотичные данные - или наоборот.""")


# snoopplugins.py Справка Модуль Reverse Vgeocoder 'elif Ya == "help"'.
def help_yandex_parser():
    print("""\033[32;1m└──[Справка]

Однопользовательский режим\033[0m
\033[32m[*] Логин — левая часть до символа '@', например, bobbimonov@ya.ru, логин
'\033[36mbobbimonov\033[0m\033[32m'.
[*] Публичная ссылка на Яндекс.Диск — это ссылка для скачивания/просмотра материалов, которую пользователь выложил в публичный доступ, например,
'\033[36mhttps://yadi.sk/d/7C6Z9q_Ds1wXkw\033[0m\033[32m' или '\033[36mhttps://disk.yandex.ru/d/7C6Z9q_Ds1wXkw\033[0m\033[32m'.
[*] Идентификатор — хэш, который указан в url на странице пользователя, например, в сервисе Я.Район: 'https://local.yandex.ru/users/tr6r2c8ea4tvdt3xmpy5atuwg0/' идентификатор — '\033[36mtr6r2c8ea4tvdt3xmpy5atuwg0\033[0m\033[32m'.
По окончанию успешного поиска выводится отчёт в CLI и открываются Яндекс-страницы пользователя в браузере.
Плагин Yandex_parser выдает меньше информации по идентификатор-у пользователя (в сравнении с другими методами), причина — fix уязвимости от Яндекса.

\033[32;1mМногопользовательский режим\033[0m
\033[32m[*] Файл с именами пользователей — файл (в кодировке UTF-8 с расширением .txt или без него), в котором записаны логины.
Каждый логин в файле должен быть записан с новой строки, например:

\033[36mbobbimonov
username
username2
username3
случайная строка
bobbimonov@ya.ru
bobbimonov@ya.ru
bobbimonov@ya.ru\033[0m

\033[32mПри использовании многопользовательского режима по окончанию поиска (быстро) выводится расширенный отчёт в CLI, сохраняется txt-отчёт о Яндекс-пользователях (с расширенными, структурированными данными) и открывается браузер с мини-отчётом (сгруппированные данные).

Плагин генерирует, но не проверяет 'доступность' персональных страниц пользователей по причине: частая защита страниц Я.капчей.

Все результаты сохраняются в '\033[36m~/snoop/results/plugins/Yandex_parser/*\033[0m\033[32m'\033[0m

\033[31;1mВ конце ноября 2022 года Яндекс закрыл публичный api, и возможно, данный плагин больше не заработает...\033[0m
""")


# snoopplugins.py Справка Модуль GEO_IP/domain 'elif dipbaza'.
def geo_ip_domain():
    print("\033[32;1m└──Справка\033[0m\n")
    print("""\033[32m[*] Режим '\033[32;1mOnline поиск\033[0m\033[32m'. Модуль GEO_IP/domain от Snoop Project использует публичный api и создает статистическую и визуализированную информацию по ip/url/domain цели (массиву данных).
Ограничения: запросы ~15к/час, невысокая скорость обработки данных, отсутствие информации о провайдерах.
Преимущества использования 'Online поиска': в качестве входных данных можно использовать не только ip-адреса, но и domain/url.
Пример файла с данными (список.txt):

\033[36m1.1.1.1
2606:2800:220:1:248:1893:25c8:1946
google.com
https://example.org/fo/bar/7564
случайная строка\033[0m

\033[32m[*] Режим '\033[32;1mOffline поиск\033[0m\033[32m'. Модуль GEO_IP/domain от Snoop Project использует специальные базы данных и создает статистическую и визуализированную информацию только по ip цели (массиву данных).
Преимущества использования 'Offline поиска': скорость (обработка тысяч ip без задержек), стабильность (отсутствие зависимости от интернет соединения и персональных настроек DNS/IPv6 пользователя), масштабный охват/покрытие (предоставляется информация об интернет-провайдерах).

[*] Режим '\033[32;1mOffline_тихий поиск\033[0m\033[32m'. Тот же режим, что и режим 'Offline', но не выводит на печать в CLI промежуточные таблицы с данными. Режим даёт прирост производительности в несколько раз.
Пример файла с данными (список.txt):

\033[36m8.8.8.8
93.184.216.34
2606:2800:220:1:248:1893:25c8:1946
случайная строка\033[0m

\033[32mSnoop довольно умён и способен определять и различать во входных данных: IPv4/v6/domain/url, вычищая ошибки и случайные строки.
По окончанию обработки данных пользователю предоставляются:
статистические отчеты в [txt/csv и визуализированные данные на карте OSM].

Примеры для чего можно использовать модуль GEO_IP/domain от Snoop Project.
Например, если у пользователя имеется список ip адресов от DDoS атаки,
он может проанализировать откуда исходила  max/min атака и от кого (провайдеры).
Решая квесты-CTF, где используются GPS/IPv4/v6.
В конечном итоге юзать плагин в образовательных целях или из естественного любопытства (проверить любые ip-адреса и их принадлежность к провайдеру и местности).\033[0m""")

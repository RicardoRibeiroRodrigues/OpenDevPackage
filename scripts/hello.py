#!/usr/bin/env python3
from dev_aberto import hello
from babel.dates import format_date
from datetime import datetime

if __name__ == '__main__':
    import gettext
    gettext.bindtextdomain('package', 'locale')
    gettext.textdomain('package')
    _ = gettext.gettext

    date, name = hello()
    date = datetime.strptime(date, r'%Y-%m-%dT%H:%M:%SZ')
    print(_('Último commit feito em:'), format_date(date, 'full'), _(' por'), name)

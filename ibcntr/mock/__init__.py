redis_mock = {'bat:000000004': {'id': 'mc_zup_tst',
                   'bat': '55',
                   'load': 'off',
                   'name': 'КЗП',
                   'changed': '2022-01-16T14:24:44.286655',
                   'changedby': '',
                   'loaded_times': '0'},
 'bat:000000001': {'id': 'mc_bnu_tst',
                   'bat': '51',
                   'load': 'off',
                   'name': 'Склад',
                   'changed': '2022-01-16T14:24:44.286543',
                   'changedby': '',
                   'loaded_times': '0'},
 'bat:000000002': {'id': 'mc_bnu_two',
                   'bat': '56',
                   'load': 'on',
                   'name': 'Склад-2',
                   'changed': '2022-01-16T14:24:44.286638',
                   'changedby': '',
                   'loaded_times': '0'},
 'bat:000000005': {'id': 'mc_zup_two',
                   'bat': '54',
                   'load': 'on',
                   'name': 'КЗП-2',
                   'changed': '2022-01-16T14:24:44.286662',
                   'changedby': '',
                   'loaded_times': '0'},
 'bat:000000003': {'id': 'mc_uat_tst',
                   'bat': '53',
                   'load': 'off',
                   'name': 'Копия УАТ',
                   'changed': '2022-01-16T14:24:44.286650',
                   'changedby': '',
                   'loaded_times': '0'}
}

help= """<pre>
Endpoint             Methods  Rule                    Note
-------------------  -------  ----------------------- ------------------------
auth.login           GET      <a href="/login">/login</a>                  Страница входа
auth.login_post      POST     <a href="/login">/login</a>                  Запрос входа
auth.logout          GET      <a href="/logout">/logout</a>                 Запрос выхода
auth.signup          GET      <a href="/signup">/signup</a>                 Открывает страницу регистрации
auth.signup_post     POST     <a href="/signup">/signup</a>                 Выполняет регистрацию пользователя
bats.bat_off         GET      /off/{bat}              Выключение загрузки ИБ {bat}
bats.bat_on          GET      /on/{bat}               Включение загрузки ИБ {bat}
bats.help            GET      <a href="/help">/help</a>                   Эта справка
bats.help            GET      <a href="/info">/info</a>                   Эта справка
bats.index           GET      <a href="/bats">/bats</a>                   Страница со списком ИБ
bats.init_db         GET      <a href="/initialize_db_fast">/initialize_db_fast</a>     (пере)заполнение базы redis
bats.log_ib_loading  GET      /log/{bat}              Записывает дату загрузки ИБ {bat}
bats.rquery          GET      /q/{bat}                Состояние ИБ {bat} (on/off)
main.index           GET      <a href="/">/</a>                       Основная страница
main.profile         GET      <a href="/profile">/profile</a>                Профиль
static               GET      /static/{path:filename} Отдает файл из каталога static

23.06.2022
</pre>
"""
label run_down:
    stop music fadeout 5
    $ nfo_text = 'Загружаю'
    $ m_nfo_text = 'Ожидайте, происходит загрузка выбранного мода.\nСходите, чай заварите, например...'
    $ renpy.hide_screen('knz_git_dwnl_menu')
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (5, hard=True)
    python:
        t2 = Thread(target=knz_dnwl_mod_base, args=(knz_rpyc_p, knz_rpyc_f, knz_rpyc_l))
        t3 = Thread(target=knz_dnwl_mod, args=(knz_rpa_f, knz_rpa_l))
        t2.start()
        t3.start()
        t2.join()
        t3.join()
        try:
            file = open(git_destination + knz_rpa_f)
        except IOError as e:
            renpy.hide_screen('knz_info_screen')
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.show("git_es_rst")
            renpy.utter_restart()
        else:
            with file:
                renpy.hide_screen('knz_info_screen')
                nfo_text = 'Загружено!'
                m_nfo_text = 'Операция проведена успешно!'
                renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
                renpy.pause (5, hard=True)
                nfo_text = 'Перезагрузка'
                m_nfo_text = 'Ожидайте, пожалуйста.'
                renpy.hide_screen('knz_info_screen')
                renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
                renpy.pause (5, hard=True)
                renpy.utter_restart()

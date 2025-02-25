init:
    $ mods["knz_dwnl_git"]=u"Everlasting Summer GitHub Mods Loader"
    $ esgml_ver = '2.6b'

    transform git_img_b():
        on idle:
            easeout_back 0.75 zoom 1.0
        on hover:
            easein_back 0.75 zoom 1.25
        on update:
            easeout_back 0.75 zoom 1.0

        # on idle:
        #     easein 0.75 zoom 1.0
        # on hover:
        #     rotate_pad True
        #     easein 0.2 zoom 0.5
        #     easein 0.75 rotate 360
        #     easein 0.2 zoom 1
        # on update:
        #     easein 0.75 zoom 1.0

    image git_nfo = "res/git_nfo.png"
    $ nfo_text = ''
    $ m_nfo_text = ''



    $ style.esgml_mm = Style(style.default)
    $ style.esgml_mm.color = (255, 255, 255, 100)
    $ style.esgml_mm.hover_color = (255, 255, 255, 48)
    $ style.esgml_mm.size = 55
    $ style.esgml_mm.font = "res/esgml_new.otf"
    $ style.esgml_mm.text_align = 0.5

    $ style.esgml_bb = Style(style.esgml_mm)
    $ style.esgml_bb.text_align = 2
    $ style.esgml_bb.size = 72

    $ style.esgml_ii = Style(style.esgml_mm)
    $ style.esgml_ii.font = "res/esgml_descr.otf"
    $ style.esgml_ii.text_align = 0.5
    $ style.esgml_ii.size = 32
    $ style.esgml_ii.color = (255, 255, 255, 100)

    $ style.esgml_nn = Style(style.esgml_mm)
    $ style.esgml_nn.color = (255, 255, 255, 100)
    $ style.esgml_nn.size = 80

    $ style.esgml_nm = Style(style.esgml_nn)
    $ style.esgml_nm.size = 40

    $ style.esgml_mn = Style(style.esgml_nm)
    $ style.esgml_mn.size = 40
    $ style.esgml_mn.color = (255, 255, 255, 100)

    $ style.esgml_mmn = Style(style.esgml_mn)
    $ style.esgml_mmn.size = 80



    $ git_destination = renpy.config.basedir + '/../../workshop/content/331470/1515489831/'


    $ git_descr = {
        'evn' : {
                'desc':'',
                'scr1':'git_screens/evn (1).png',
                'scr2':'git_screens/evn (2).png',
                'scr3':'git_screens/evn (3).png'
                },
        'dwl' : {
                'desc':'Небольшой мод по одноимённому фанфику. События мода начинаются в седьмой день, когда Семён покидает Лену, думая лишь о том, чтобы поскорее вернуться домой. Но вернувшись в домик Лены, он видит, что Лена умирает...',
                'scr1':'git_screens/dwl (1).png',
                'scr2':'git_screens/dwl (2).png',
                'scr3':'git_screens/dwl (3).png'
                },
        'vkun' : {
                'desc':'Заблудившись в тумане, молодой солдат, находит вход в мифический, кишащий монстрами лагерь...',
                'scr1':'git_screens/vkun (1).png',
                'scr2':'git_screens/vkun (2).png',
                'scr3':'git_screens/vkun (3).png'
                },
        'ev' : {
                'desc':'Все мы уже давно хорошо знаем историю Семёна, переживавшего в "Совёнке" многочисленные циклы с разными исходами и результатами. Мы слышали множество вариантов предысторий и продолжений, альтернативных взглядов на старые события. И вот ещё один из них. Что будет, если в лагерь вместе с Семёном попадёт кто-то ещё? Человек, частично похожий на него, но при этом абсолютный ему антипод. Как он проживёт эти 7 дней и какое место займёт в них Семён? Узнаете, познакомившись с проектом "Бесконечные Каникулы". ',
                'scr1':'git_screens/ev (1).png',
                'scr2':'git_screens/ev (2).png',
                'scr3':'git_screens/ev (3).png'
                },
        'bm' : {
                'desc':'Мод повествует о жизни обычного московского студента Михаила, живущего скучной жизнью в своей небольшой квартире. Михаил часто прогуливает занятия и живет только сам для себя. Сможет ли нашего героя изменить к лучшему неделя в "Совёнке"? Он и сам этого не знает. Но, попав в лагерь, он начинает замечать странные вещи, которые всерьез его настораживают и даже пугают. Чем закончится его летнее приключение? Об этом вы узнаете из нашего мода. ',
                'scr1':'git_screens/bm (1).png',
                'scr2':'git_screens/bm (2).png',
                'scr3':'git_screens/bm (3).png'
                },
        'st' : {
                'desc':'Расскажет иную историю про парня по имени Семен. Который оказался не в самой обычной ситуации. - О чем мод? —-Об альтернативной реальности, в которую попал наш герой. Так же в моде есть множество отсылок из реальной жизни, с которым вы можете столкнуться. (И это не просто так, весь сценарий и исход событий будет зависеть от вас.) Оригинальный сценарий мода. Это стандартная семидневная смена в лагере Совёнок. В нем вы узнаете истинные помыслы главных героев игры. Выберитесь из цикла(С той которую вы выберите) А так же узнаете почему Семён потерял память.',
                'scr1':'git_screens/st (1).png',
                'scr2':'git_screens/st (2).png',
                'scr3':'git_screens/st (3).png'
                },
        'ls' : {
                'desc':'',
                'scr1':'git_screens/ls (1).png',
                'scr2':'git_screens/ls (2).png',
                'scr3':'git_screens/ls (3).png'
                },
        'la' : {
                'desc':'',
                'scr1':'git_screens/la (1).png',
                'scr2':'git_screens/la (2).png',
                'scr3':'git_screens/la (3).png'
                },
        'twat' : {
                'desc':'',
                'scr1':'',
                'scr2':'',
                'scr3':''
                },
        'v17' : {
                'desc':'',
                'scr1':'git_screens/v17 (1).png',
                'scr2':'git_screens/v17 (2).png',
                'scr3':'git_screens/v17 (3).png'
                },
        'emk1' : {
                'desc':'',
                'scr1':'git_screens/emk1 (1).png',
                'scr2':'git_screens/emk1 (2).png',
                'scr3':'git_screens/emk1 (3).png'
                },
    }


    $ mods_names = [
    ('evn', "Бесконечные кошмары", "evn_git_base.rpyc", "nightmares.rpa", "nightmares/", "https://github.com/tsunderekun/es_gitmods/raw/master/evn_git_base.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/Nightmares.rpa", git_destination),

    ('dwl', "Дни с Леной", "git_dayswithlena.rpyc", "git_dayswithlena_res.rpa", "dayswithlena/", "https://github.com/tsunderekun/es_gitmods/raw/master/git_dayswithlena.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/git_dayswithlena_res.rpa", git_destination),

    ('vkun', "Совенок в тумане", "git_vkun_fog.rpyc", "VKUN_MOD.rpa", "vkun_fog/", "https://github.com/tsunderekun/es_gitmods/raw/master/git_vkun_fog.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/VKUN_MOD.rpa", git_destination),

    ('ev', "Бесконечные Каникулы", "git_vacations_base.rpyc", "git_vacations.rpa", "git_vacations/", "https://master.dl.sourceforge.net/project/esmgl-mods/git_vacations_base.rpyc", "https://master.dl.sourceforge.net/project/esmgl-mods/git_vacations.rpa", git_destination),

    ('bm', "Большая Ошибка", "git_bm_base.rpyc", "git_bm.rpa", "git_bm/", "https://gitlab.com/tsunderekun/esgml_mods/raw/master/git_bm/git_bm_base.rpyc", "https://gitlab.com/tsunderekun/esgml_mods/raw/master/git_bm/git_bm.rpa", git_destination),

    ('st', "Время Лета", "git_sumtime_base.rpyc", "git_sumtime.rpa", "git_sumtime/", "https://gitlab.com/tsunderekun/esgml_mods/raw/master/git_sumtime/git_sumtime_base.rpyc", "https://gitlab.com/tsunderekun/esgml_mods/raw/master/git_sumtime/git_sumtime.rpa", git_destination),

    ('ls', "История Лены", "git_lena_story_base.rpyc", "git_lena_story.rpa", "git_lena_story/", "https://github.com/tsunderekun/es_gitmods/raw/master/git_lena_story_base.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/git_lena_story.rpa", git_destination),

    ('la' ,"Лена. Альтернативная концовка", "git_lena_alternate_base.rpyc", "git_lena_alternate.rpa", "git_lena_alternate/", "https://github.com/tsunderekun/es_gitmods/raw/master/git_lena_alternate_base.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/git_lena_alternate.rpa", git_destination),

    ('emk1', "Эпилог МК1", "emk1_base.rpyc", "emk1.rpa", "emk1/", "https://github.com/tsunderekun/es_gitmods/raw/master/emk1_base.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/emk1.rpa", git_destination),

    ('v17', "Где мои семнадцать лет?", "base_v17.rpyc", "git_v17.rpa", "v17/", "https://github.com/tsunderekun/es_gitmods/raw/master/base_v17.rpyc", "https://github.com/tsunderekun/es_gitmods/raw/master/git_v17.rpa", git_destination),
    ]




label knz_dwnl_git:
    $ config.mouse = {'default' : [("res/cursor.png", 0, 0)]}
    play music 'res/git_main.ogg' fadein 5
    call screen knz_git_dwnl_menu with dissolve

screen knz_info_screen(nfo_text, m_nfo_text):
    modal False
    add 'git_nfo'
    text nfo_text xalign 0.5 yalign 0.45:
        style "esgml_nn"
    text m_nfo_text xalign 0.5 yalign 0.54:
        style "esgml_nm"


screen knz_git_dwnl_menu:
    $ import os.path
    modal False
    window:
        xalign 0 yalign 0
        background "git_nfo"
        vbox xpos 0.0725 ypos 0.175 yfill:

            text "Everlasting Summer Git Mods Loader":
                        style "esgml_mmn"
            null height 10
            text "Свободный репозиторий модов для Бесконечного Лета":
                        style "esgml_mn"

    side "c r":
        area (0.05, 0.225, 0.9, 0.675)
        viewport id "git_mods_menu":
            draggable True
            mousewheel True
            scrollbars None

            has vbox
            for id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination in mods_names:
                hbox spacing 10 ypos:

                    if os.path.isfile(destination + rpa_f):
                        add 'res/git_dwl_inactive.png' xalign 0.01
                    else:
                        imagebutton auto 'res/git_dwl_%s.png' action [Function(knz_get_data, rpyc_p, rpyc_f, rpyc_l, rpa_f, rpa_l), Function(renpy.call_in_new_context, 'run_down')] at git_img_b xalign 0.01


                    if os.path.isfile(destination + rpa_f):
                        imagebutton auto 'res/git_del_%s.png' action [Function(knz_get_data, rpyc_p, rpyc_f, rpyc_l, rpa_f, rpa_l), Function(renpy.call_in_new_context, 'deleter')] at git_img_b xalign 0
                    else:
                        add 'res/git_del_inactive.png' xalign 0

                    textbutton name ypos -0.2125  action [Show('git_modnfo', dissolve, id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination)] at git_img_b:
                        style "esgml_mm"
                        text_style "esgml_mm"

    hbox yalign 0.975 xalign 0.5 spacing 144:
        if 'NLT_tl' in globals():
            textbutton 'NLT Modpack' action [Function(renpy.call_in_new_context, 'NLT_toolbox')] at git_img_b:
                        style "esgml_bb"
                        text_style "esgml_bb"
        else:
            textbutton 'NLT Modpack' action [OpenURL('steam://url/CommunityFilePage/847728687')] at git_img_b:
                        style "esgml_bb"
                        text_style "esgml_bb"

        textbutton 'Главное меню' action [SetField(config, "mouse", {'default' : [('images/misc/mouse/1.png', 0, 0)]}), Return("mm")] at git_img_b:
                    style "esgml_bb"
                    text_style "esgml_bb"


        textbutton 'Выход' action [Quit (confirm=False)] at git_img_b:
                    style "esgml_bb"
                    text_style "esgml_bb"

        textbutton '©' action [Function(renpy.call_in_new_context, 'go_to_git_authors')] at git_img_b:
                    style "esgml_bb"
                    text_style "esgml_bb"

label go_to_git_authors:
    if _return == "mm":
        return
    call screen git_authors with fade

screen git_authors:
    modal False
    add "git_nfo"
    vbox xpos 0.05 ypos 0.05 yfill:

        text "Everlasting Summer Git Mods Loader":
                    style "esgml_nn"

        null height 5

        hbox xpos 0.025:

            text "Версия:":
                        style "esgml_nm"

            null width 5

            text esgml_ver:
                        style "esgml_nm"


        null height 20

        text "Загрузчик удаленных модов для Бесконечного лета. \nСоздан для того, чтобы вы могли играть в удаленные моды. \nА также, вы всегда можете помочь нам с их добавлением \nперейдя в официальную группу." text_align 0.0 xpos 0.025:
                    style "esgml_nm"

        null height 20

        text "Ссылки:" xpos 0.025:
                    style "esgml_nm"


        textbutton "Официальная группа" xpos 0.05 action OpenURL('https://vk.com/esgml') at git_img_b:
                    style "esgml_nm"
                    text_style "esgml_nm"


        textbutton "GitHub проекта" xpos 0.05 action OpenURL('https://github.com/tsunderekun/esgml_steam') at git_img_b:
                    style "esgml_nm"
                    text_style "esgml_nm"

        null height 10

        text "Авторы:" xpos 0.025:
            style "esgml_nm"

        textbutton "Илья Кунц {i}aka Phos{/i}" xpos 0.05 action OpenURL('https://vk.com/id327507103') at git_img_b:
            style "esgml_nm"
            text_style "esgml_nm"

        textbutton "Константин Можейко {i}aka Лена{/i}" xpos 0.05 action OpenURL('https://vk.com/id18106410') at git_img_b:
            style "esgml_nm"
            text_style "esgml_nm"

        null height 20

        textbutton "Проект распространяется под лицензией CC BY-NC-SA 4.0" xpos 0.025 action OpenURL('https://creativecommons.org/licenses/by-nc-sa/4.0/') at git_img_b:
            style "esgml_nm"
            text_style "esgml_nm"

        null height 50

        textbutton 'Назад' ypos 0.8 action [Show('knz_git_dwnl_menu', dissolve), Hide('git_modnfo')] at git_img_b:
                style "esgml_bb"
                text_style "esgml_bb"



screen git_modnfo(id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination):
    modal False
    add "git_nfo"
    text name yalign 0.05 xalign 0.1:
        style "esgml_nn"
    hbox yalign 0.175 xalign 0.5 spacing 64:
        imagebutton idle im.Scale(git_descr[id]['scr1'], 480, 270) hover im.Scale(git_descr[id]['scr1'], 480, 270) action [Show('git_image', dissolve, git_descr[id]['scr1'], id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination)] at git_img_b
        imagebutton idle im.Scale(git_descr[id]['scr2'], 480, 270) hover im.Scale(git_descr[id]['scr2'], 480, 270) action [Show('git_image', dissolve, git_descr[id]['scr2'], id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination)] at git_img_b
        imagebutton idle im.Scale(git_descr[id]['scr3'], 480, 270) hover im.Scale(git_descr[id]['scr3'], 480, 270) action [Show('git_image', dissolve, git_descr[id]['scr3'], id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination)] at git_img_b
    text git_descr[id]['desc'] yalign 0.55 xmaximum 0.8 xalign 0.5:
        style "esgml_ii"
    hbox spacing 64 yalign 0.9 xalign 0.5:
            textbutton 'Назад' action [Show('knz_git_dwnl_menu', dissolve), Hide('git_modnfo')]:
                    style "esgml_bb"
                    text_style "esgml_bb"


            if os.path.isfile(destination + rpa_f):
                textbutton 'Удалить' action [Function(knz_get_data, rpyc_p, rpyc_f, rpyc_l, rpa_f, rpa_l), Function(renpy.call_in_new_context, 'deleter')]:
                        style "esgml_bb"
                        text_style "esgml_bb"
                textbutton 'Уже загружен':
                        style "esgml_bb"
                        text_style "esgml_bb"
            else:
                textbutton 'Загрузить' action [Function(knz_get_data, rpyc_p, rpyc_f, rpyc_l, rpa_f, rpa_l), Function(renpy.call_in_new_context, 'run_down')]:
                        style "esgml_bb"
                        text_style "esgml_bb"
                textbutton 'Не установлен':
                        style "esgml_bb"
                        text_style "esgml_bb"



screen git_image(img, id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination):
    add "git_nfo"
    add img:
        xalign 0.5
        yalign 0.5

    button:
        style 'blank_button'
        xpos 0
        ypos 0
        xfill True
        yfill True
        action [Hide('git_image'), Show('git_modnfo', dissolve, id, name, rpyc_f, rpa_f, rpyc_p, rpyc_l, rpa_l, destination)]



init 999 python:
    config.archives.append('res_git')



init python:
    from threading import Thread
    import os, shutil

    kprogress = None
    knz_rpyc_p = None
    knz_rpyc_f = None
    knz_rpyc_l = None
    knz_rpa_f = None
    knz_rpa_l = None

    def knz_get_data(rpyc_p, rpyc_f, rpyc_l, rpa_f, rpa_l):
        global knz_rpyc_p
        global knz_rpyc_f
        global knz_rpyc_l
        global knz_rpa_f
        global knz_rpa_l
        knz_rpyc_f = rpyc_f
        knz_rpyc_l = rpyc_l
        knz_rpyc_p = rpyc_p
        knz_rpa_f = rpa_f
        knz_rpa_l = rpa_l


    def knz_dnwl_mod_base(mfolder, baserpyc, rpyclink):

        # global f_percent
        destination = git_destination + mfolder
        os.mkdir(destination)
        from urllib2 import urlopen
        response = urlopen(rpyclink)
        CHUNK = 16 * 1024
        with open(baserpyc, 'wb') as f:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)
        os.rename(baserpyc, destination + baserpyc)

    def knz_dnwl_mod(baserpa, rpalink):

        from urllib2 import urlopen
        response = urlopen(rpalink)
        CHUNK = 16 * 1024
        with open(baserpa, 'wb') as f:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)
        os.rename(baserpa, git_destination + baserpa)


    def knz_git_mod_clean(baserpa, mfolder):
        shutil.rmtree(git_destination + mfolder, ignore_errors=True, onerror=None)
        renpy.hide_screen('knz_git_dwnl_menu')
        nfo_text = 'Удаление'
        m_nfo_text = 'Выполняется удаление указанного мода, ожидайте...'
        renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
        renpy.pause (1, hard=True)
        try:
            persistent.del_baserpa = git_destination + baserpa
            persistent.unbaserpa = baserpa[:-4]
            renpy.pause (2, hard=True)
            nfo_text = 'Перезагрузка'
            m_nfo_text = 'Ожидайте, пожалуйста.'
            renpy.hide_screen('knz_info_screen')
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (2, hard=True)
            renpy.utter_restart()
        except OSError, e:
            renpy.hide_screen('knz_info_screen')
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы c атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.utter_restart()


    ###MOD CHECKER###

init -10 python:
    def rpa_check_append(rpaf, rpan):
        import os
        destination = renpy.config.basedir + '/../../workshop/content/331470/1515489831/'
        try:
            file = open(destination + rpaf)
        except IOError as e:
            pass
        else:
            with file:
                config.archives.append(rpan)

    def rpa_check_varinst(git_mod_id, git_mod_name, rpaf):
        global mods
        import os
        destination = renpy.config.basedir + '/../../workshop/content/331470/1515489831/'
        try:
            file = open(destination + rpaf)
        except IOError as e:
            pass
        else:
            with file:
                mods[git_mod_id]=git_mod_name

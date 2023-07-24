LEXICON_RU: dict[str, str] = {
    '/start': '<b>Привет!</b>\nЭто чат бот по внесению и устранению рисков! '
              'Подробная информация по команде /help',
    '/help': 'Для отправки, устранения риска, отправьте мне фото риска! '
             'Необходимо нажать на нужную кнопку:'
             '\n\n<b>Отправка нового риска</b>'
             '\nПосле отправки фото нового риска, необходимо указать '
             '\nкоординаты риска: '
             '\nРяд, ось, отметка или принадлежность к оборудованию.'
             '\n\n<b>Устранение риска</b>'
             '\nПосле отправки фото устранения риска, '
             '\nнеобходимо укать номер риска в формате 1-23-2, где:'
             '\n1-номер зоны;'
             '\n23-номер риска;'
             '\n2-номер мероприятия (c 1 до 2).'
             '\n\nЕсли вы хотите прервать заполнение формы - '
             'отправьте команду /cancel',
    '/cancel_in_status': 'Вы не сохранили изменения для данного фото!\n\n'
                         'Чтобы  перейти к заполнению формы - '
                         'отправьте фото',
    '/cancel_without_status': 'Отменять нечего! Вы не отправляли фото.\n\n'
                              'Чтобы  перейти к заполнению формы - '
                              'отправьте фото',
    'new_risk_button': 'Новый риск',
    'elimination_risk_button': 'Устранение риска',
    'select_move_answer': 'Выберете действие',
    'text_err_input_move': 'Пожалуйста, пользуйтесь кнопками ниже\n '
                            'при выборе действия \n\n'
                            'Если вы хотите прервать '
                            'заполнение анкеты - отправьте команду /cancel',
    'enter_new_risk_answer': 'Введите координаты риска (ряд, ось, отметка или принадлежность к оборудованию)',
    'enter_new_risk_location_err_answer':'То, что вы отправили не похоже на координаты.\n\n'
                              'Пожалуйста, введите координаты в формате: '
                              '\n<b>ряд, ось, отметка или принадлежность к оборудованию.</b>'
                              '\nЕсли вы хотите прервать заполнение формы - '
                              'отправьте команду /cancel',
    'enter_elimination_risk_num_err_answer': 'То, что вы отправили не похоже на номер риска!\n\n'
                              'Пожалуйста, введите номер в формате: '
                              '\n<b>1-23-2 '
                              '\nгде: '
                              '\n1-номер зоны;'
                              '\n23-номер риска;'
                              '\n2-номер мероприятия.</b>'
                              '\nЕсли вы хотите прервать заполнение формы - '
                              'отправьте команду /cancel',
    'enter_num_risk_answer': 'Ведите номер риска в формате:  1-23-2',
    'accepted_review_answer': 'Риск принят на проверку.',
    'other_answer': 'Отправьте фото риска\n\n '
                    'для подробной информации отправьте команду /help'

    }
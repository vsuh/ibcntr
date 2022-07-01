# -*- coding: utf-8 -*-
"""
Основное приложение веб-сервера управления перезагрузкой тестовых ИБ
"""
import ibcntr
app = ibcntr.create_app()
app.secret_key = b'_5#y2L"F4Q23K8z\n\xecf5]/'

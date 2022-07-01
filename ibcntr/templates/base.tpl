<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Moscollector 1C pearls</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">

    <link rel="icon" href="/static/favicon.ico">

    <style>
         body {
            text-shadow: 0 .05rem .1rem rgba(0, 0, 0, .5);
            box-shadow: inset 0 0 5rem rgba(0, 0, 0, .5);
        }

        a,
        a:focus,
        a:active {
            text-decoration: none;
            color: rgb(108, 24, 24);
        }

 .card-bg-on {background-color: rgb(230, 250, 230);}
 .card-bg-off {background-color: rgba(250, 230, 230);}
        .nav-masthead .nav-link+.nav-link {
            margin-left: 1rem;
        }

        .nav-masthead .active {
            color: rgb(28, 43, 100);
            border-bottom-color: rgb(75, 40, 124);
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }
    </style>

</head>

<body>
    <!--style="border:navy 2px solid; width:100vw; height: 100vh;"-->
    <div class="container" style="width:100vw; min-height: 100vh;">
        <div class="row align-items-start">
            <header class="mb-auto col">
                <div class="col">
                    <h3 class="float-md-start mb-2">Управление перезагрузкой ИБ</h3>
                    <nav class="nav nav-masthead justify-content-right float-md-end">
                        {% if current_user.is_authenticated %}
                        <a href="{{ url_for('main.profile') }}" class="navbar-item">
                            Профиль
                            <i class="bi bi-wallet"></i>
                        </a> &nbsp;&nbsp;&nbsp;&nbsp;
                        {% endif %}

                        <a href="{{ url_for('bats.index') }}" class="navbar-item">
                            {% if current_user.is_authenticated %}
                            Управление ИБ
                            <i class="bi bi-star"></i>
                            {% else %}
                            Состояние ИБ
                            <i class="bi bi-circle-square"></i>
                            {% endif %}
                        </a> &nbsp;&nbsp;&nbsp;&nbsp;
                 

                        {% if not current_user.is_authenticated %}
                        <a href="{{ url_for('auth.login') }}" class="navbar-item">
                            Вход
                            <i class="bi bi-check2-circle"></i>
                        </a> &nbsp;&nbsp;&nbsp;&nbsp;
                        {% endif%}

                        {% if not current_user.is_authenticated %}
                        <a href="{{ url_for('auth.signup_post') }}" class="navbar-item">
                            Регистрация
                            <i class="bi bi-layout-text-window-reverse"></i>
                        </a> &nbsp;&nbsp;&nbsp;&nbsp;
                        {% endif %}
                        {% if current_user.is_authenticated %}
                        {{ current_user.name }}:&nbsp;
                        <a href="{{ url_for('auth.logout') }}" class="navbar-item is_info">
                            Выход
                            <i class="bi bi-power"></i>
                        </a>
                        {% endif %}
                    </nav>
                </div>
            </header>
        </div>
        
        <img src="static/images/1x1.gif" height="55">

        <div class="row align-items-center">
            <div class="col">

                {% block content %}
                {% endblock %}

            </div>
        </div>

        <!--img src="static/images/1x1.gif" height="85"-->

        <div style="position:fixed; bottom:0;min-width: 100%">
            <div class="row align-items-end">
                <div class="col float-md-start ">
                    <a href="https://github.com/vsuh/ibcntr.git">github</a>
                    &nbsp;<span style='color:gray;'>|</span>&nbsp;
                    Страница создана с использованием <a
                        href="https://getbootstrap.com/docs/5.0/getting-started/introduction/">Bootstrap5</a>
                </div>

                <div class="col float-md-end">
                    <a href="https://vsuh.github.io">VSCraft@2022</a>
                </div>
            </div>
        </div>

    </div>
</body>

</html>
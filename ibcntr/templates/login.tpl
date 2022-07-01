{% extends "base.tpl" %}

{% block content %}
<div class="column is-4 is-offset-4">
    <h3 class="title">Вход</h3>
    <div class="box">
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <div class="notification is-danger">
            {{ messages[0] }}
        </div>
        {% endif %}
        {% endwith %}
        <form method="POST" action="/login">
            <form method="POST" action="/login">
                <div class="field my-2">
                    <div class="control">
                        <input class="input is-large" type="email" name="email" placeholder="Электропочта" autofocus="">
                    </div>
                </div>

                <div class="field my-2">
                    <div class="control">
                        <input class="input is-large" type="password" name="password" placeholder="Имя">
                    </div>
                </div>
                <div class="field my-2">
                    <label class="checkbox">
                        <input type="checkbox">
                        Запомнить
                    </label>
                </div>
                <button class="button is-block is-info is-normal is-fullwidth">Войти</button>
            </form>
    </div>
</div>
{% endblock %}
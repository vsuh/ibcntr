{% extends "base.tpl" %}

{% block content %}
<div class="column is-4 is-offset-4">
    <h3 class="title">Регистрация</h3>
    <div class="box">
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <div class="notification is-danger">
            {{ messages[0] }}. Перейдите на <a href="{{ url_for('auth.login') }}">форму входа</a>.
        </div>
        {% endif %}
        {% endwith %}
        <form method="POST" action="/signup">
            <div class="field">
                <div class="control">
                    <input class="input is-large" type="email" name="email" placeholder="Электропочта" autofocus="">
                </div>
            </div>

            <div class="field my-2">
                <div class="control">
                    <input class="input is-large" type="text" name="name" placeholder="Имя" autofocus="">
                </div>
            </div>

            <div class="field my-2">
                <div class="control">
                    <input class="input is-large" type="password" name="password" placeholder="Пароль">
                </div>
            </div>
            <div class="field my-2">
                <label class="checkbox">
                    <input type="checkbox">
                    Запоминать меня всегда
                </label>
            </div>

            <button class="button is-block is-info is-normal is-fullwidth">Зарегистрировать</button>
        </form>
    </div>
</div>
{% endblock %}
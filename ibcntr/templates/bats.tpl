{% extends "base.tpl" %}


{% block content %}
<div class="row">
    <h5>
        <a href="/"><i class="bi bi-arrow-down-left"></i></a>&nbsp;{{ title }}
    </h5><br>
</div><br>

<!-- div class="row justify-content-md-center "-->
<div class="row justify-content-md-center row-cols-1 row-cols-md-3 row-cols-lg-4 g-3">
    {% for BatIb, bat in ibs.items() %}

        <div class="col-sm-3 mx-3">
            <div class="card mb-3">
                <div class="{{ 'card-bg-off' if bat['load']=='off' else 'card-bg-on' }}">
                    {% if current_user.is_authenticated %}
                    <a href="{{"/on/" if bat['load']=="off" else "/off/" }}{{ bat['id'] }}">
                    {% endif %}
                        <img style="background:#666;opacity:0.3; filter: grayscale(100%)"
                        src="static/images/{{ images[bat['id'][3:6]] }}" height=150 class="card-img-top" alt="УПП"
                        style="filter: grayscale(50%);">
                    <div class="card-header" style="position:relative;top:-5px">
                        <h5 class="card-title">{{ bat["name"] }}</h5>
                    </div>
                </div>
                <div class="card-text p-3 {{ 'card-bg-off' if bat['load']=='off' else 'card-bg-on' }}">
                    <p>{{ bat['id'] }}&nbsp;:&nbsp;{{ on_off(bat['load']) }}</p>
                </div>
                <div class="card-footer">
                    <small class="text-muted d-flex justify-content-start">Состояние изменено:&nbsp;
                        {{ format_date(bat['changed']) }} &nbsp;{{ bat['changedby'] }}</small>
                    <small class="text-muted d-flex justify-content-start">ИБ загружалась:&nbsp;
                        {{ format_date(bat['loaded_times']) }} </small>
                </div>
                {% if current_user.is_authenticated %}
                <a href="/on/{{ bat['id'] }}">
                {% endif %}
            </div>
            {% if current_user.is_authenticated %}
        </a>
        {% endif %}
            </div>

    {% endfor %}
</div>


<div class="row">
    <div class="col">
        <div id="log-placeholder"></div>
    </div>
</div>

{% endblock %}
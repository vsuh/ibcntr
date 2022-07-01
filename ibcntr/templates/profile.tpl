{% extends "base.tpl" %}

{% block content %}



<h1 class="title">
  Привет, <span style="color:navy;">{{ current_user.name }}</span>!
  {% if current_user.is_authenticated %}
      <br>Регистрация выполнена
  {% endif %}

</h1>

<script>
    setTimeout(function(){
        window.location.href = '{{ redirect_url }}';
    }, 5000);
</script>

{% endblock %}
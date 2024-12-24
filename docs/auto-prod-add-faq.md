# Частые вопросы

**Товары с сайта загрузились без картинок, с неверными ценами или совсем не загрузились**

 
:   Воспользуйтесь рекомендациями по разметке товаров по схеме, приведенной на странице [Информация о товарах](https://yandex.ru/support/webmaster/supported-schemas/goods-prices.html) или попробуйте загрузить [через YML‑фид](auto-prod-add-yml-fid.md).
    
    Проверить правильность разметки можно с помощью {% if tld == "ru" %}[валидатора](https://webmaster.yandex.ru/tools/microtest/){% endif %}{% if tld == "kz" %}[валидатора](https://webmaster.yandex.kz/tools/microtest/){% endif %}.

**Товары с Ozon не выгружаются автоматически**

 
:   Убедитесь, что в рекламной кампании указана верная ссылка и по ней находятся товары. Если со ссылкой все в порядке, подключите API‑ключ:
    
    1. Перейдите в раздел **Реклама** и выберите рекламную кампанию.
    1. Откройте вкладку **Рекламные материалы** и напротив маркетплейса нажмите **Настроить**.
    1. Выберите **Подключить Ozon API**.
    1. В поле **API‑ключ** введите ключ из Личного кабинета Ozon.
    1. Нажмите **Сохранить**.

**Как загрузить фид товаров для рекламы лендинга от Яндекс Бизнеса?**

 
:   В профиле компании в разделе **Товары и услуги** вы можете добавить [файл с YML‑фидом](manage/price-list.md#yml-file) — товары автоматически загрузятся в рекламный кабинет. Ссылку на YML‑фид добавить не получится.


<div class="table-style-none">

#|
||
<a href="https://yandex.ru/chat?context=%7B%22entrypoint%22%3A%22%7B%5C%22page_name%5C%22%3A%5C%22help%5C%22%2C%5C%22a_pageurl%5C%22%3A%5C%22https%3A%2F%2Fyandex.ru%2Fsupport%2Fbusiness-priority%2F%5C%22%7D%22%7D#/user/5cb78286-a944-4c0f-bf33-b5c282eae053?utm-source=chat-in-help">
  <span class="button">Чат с поддержкой</span>
</a>
|
<a href="https://forms.yandex.ru/surveys/13485724.a1310d38f50da2df17deb93bfdb4b514c5679847">
  <span class="button">Письмо в поддержку</span>
</a>
||
|#

</div>

{% include [edu-online-business](_includes/edu-online-business.md) %}

{% include [table-style-none](_includes/table-style-none.md) %}

{% include [button-style](_includes/yellow-button-styles.md) %}

{% include [border-style](_includes/border-style.md) %}

{% include [cut-button-style](_includes/cut-button-style.md) %}

{% include [footer](_includes/footer.md) %}

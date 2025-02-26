# Интеграция с Ozon Performance API


{% note warning "Ограничение" %}

Интеграция доступна только с кабинетом продавца (Ozon Seller).

{% endnote %}


Вы можете настроить обмен данными между вашим магазином на Ozon и Яндекс Бизнесом с помощью интеграции Ozon Performance API. Интеграция позволит:

- Яндекс Бизнесу лучше подбирать клиентов, которым понравятся ваши товары;
- получать в личном кабинете Ozon Seller больше статистики: сколько человек пришли по рекламе и совершили покупки или положили товары в корзину.

## Как настроить интеграцию {#configure}

1. Перейдите в раздел **Реклама**. Если вам доступна возможность интеграции, вы увидите баннер о преимуществах подключения API.
    
1. На баннере **Ваша реклама станет эффективнее** нажмите **Настроить**.
    
1. Получите и заполните [API‑ключи](*API‑ключи) для интеграции по предложенным шагам.
    
    {% cut "Подробнее о том, как получить АPI‑ключи в личном кабинете на Ozon" %}
    
    1. В разделе **Аналитика** выберите **Внешний трафик**. Скопируйте и сохраните значение поля **Префикс для метки UTM_CAMPAIGN** вида `vendor_org_*****`.
    1. В этом же разделе нажмите **Создать ссылки**. В открывшемся блоке **Сервисные аккаунты** нажмите **Создать аккаунт**.
    1. Нажмите **Добавить ключ**. Скопируйте значения столбцов **Client ID** и **Client Secret**.
    
    {% endcut %}
    
1. Нажмите **Сохранить**. Если все заполнено верно, вы увидите сообщение «Ozon Performance API настроен».

Яндекс Бизнес создаст рекламные объявления с вашими товарами и будет передавать статистику по переходам в личный кабинет Ozon Seller.


{% cut "Где посмотреть статистику" %}


1. В личном кабинете Ozon Seller в разделе **Аналитика** выберите **Внешний трафик**.
1. Нажмите **Сгенерировать отчет**.


{% endcut %}


## Как обновить АPI‑ключи {#update}

1. Перейдите в раздел **Реклама** на вкладку **Настройки**.
1. В блоке **Обмен Данными** напротив Ozon Performance API нажмите **Настроить**.
1. Внесите изменения и нажмите **Сохранить**.


<div class="table-style-none">

#|
||
<a href="https://yandex.ru/chat?context=%7B%22entrypoint%22%3A%22%7B%5C%22page_name%5C%22%3A%5C%22help%5C%22%2C%5C%22a_pageurl%5C%22%3A%5C%22https%3A%2F%2Fyandex.ru%2Fsupport%2Fbusiness-priority%2Forder.html%5C%22%7D%22%7D#/user/5cb78286-a944-4c0f-bf33-b5c282eae053?utm-source=chat-in-help">
  <span class="button">Чат с поддержкой</span>
</a>
|
<a href="troubleshooting/favplacement">
  <span class="button">Письмо в поддержку</span>
</a>
||
|#

</div>


{% include [edu-online-business](_includes/edu-online-business.md) %}

{% include [table-style-none](_includes/table-style-none.md) %}

{% include [button-style](_includes/yellow-button-styles.md) %}

{% include [border-style](_includes/border-style.md) %}

{% include [footer](_includes/footer.md) %}


[*API‑ключи]: Ключи доступа.

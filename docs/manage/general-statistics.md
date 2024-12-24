# Общая статистика

В разделе **Статистика**&nbsp;→ **Общая** вы увидите данные по всему рекламному трафику и кликам профиля компании в Картах, Поиске, Услугах и Кью.

В отчете указаны действия, которые пользователи совершили:

- в веб‑версии {% if tld == "ru" %}[Яндекс Карт](https://yandex.ru/maps/){% endif %}{% if tld == "kz" %}[Яндекс Карт](https://yandex.kz/maps/){% endif %}{% if tld == "uz" %}[Яндекс Карт](https://yandex.uz/maps/){% endif %}{% if tld == "com" %}[Яндекс Карт](https://yandex.com/maps/){% endif %}{% if tld == 'com.tr' %}[Яндекс Карт](https://yandex.com.tr/maps/){% endif %} для компьютеров и мобильных устройств;
- в мобильном приложении Яндекс Карты для {% if tld == "ru" or tld == "uz" %}[Android](https://mobile.yandex.ru/apps/android/maps){% endif %}{% if tld == "kz" %}[Android](https://mobile.yandex.kz/apps/android/maps){% endif %}{% if tld == "com" or tld == 'com.tr' %}[Android](https://mobile.yandex.com/apps/android/maps){% endif %} и {% if tld == "ru" or tld == "uz" %}[iOS](https://mobile.yandex.ru/apps/iphone/maps/){% endif %}{% if tld == "kz" %}[iOS](https://mobile.yandex.kz/apps/iphone/maps/){% endif %}{% if tld == "com" or tld == 'com.tr' %}[iOS](https://mobile.yandex.com/apps/iphone/maps/){% endif %};
- в мобильном приложении Яндекс Навигатор для {% if tld == "ru" or tld == "uz" %}[Android](https://mobile.yandex.ru/apps/android/navigator/){% endif %}{% if tld == "kz" %}[Android](https://mobile.yandex.kz/apps/android/navigator/){% endif %}{% if tld == "com" or tld == 'com.tr' %}[Android](https://mobile.yandex.com/apps/android/navigator/){% endif %} и {% if tld == "ru" or tld == "uz" %}[iOS](https://mobile.yandex.ru/apps/iphone/navigator/){% endif %}{% if tld == "kz" %}[iOS](https://mobile.yandex.kz/apps/iphone/navigator/){% endif %}{% if tld == "com" or tld == 'com.tr' %}[iOS](https://mobile.yandex.com/apps/iphone/navigator/){% endif %}.

Эта информация поможет выявить сервисы, на которых ваша аудитория наиболее активна, и проанализировать способы привлечения трафика.


## Основные показатели {#main-indicators}

Основные показатели, по которым оцениваются данные в разделе **Статистика**:

**Запросы по видам деятельности**

 
:   {% include [glossary-rubrics-query](../_includes/general/glossary/id-glossary/rubrics-query.md) %}

**Конкуренты**

 
:   {% include [glossary-competitor](../_includes/general/glossary/id-glossary/competitor.md) %}

**Прямые переходы**

 
:   {% include [glossary-direct-transition](../_includes/general/glossary/id-glossary/direct-transition.md) %}

**Дискавери-переходы**

 
:   {% include [glossary-discovery](../_includes/general/glossary/id-glossary/discovery.md) %}


## Период статистики {#date}

Выберите период, за который хотите посмотреть статистику: неделя, месяц, три месяца. Можно указать произвольный период. Выбранный период будет действовать для всех графиков статистики.

Вы можете изменить группировку: по дням, неделям или месяцам. Установить группировку по дням можно только для периода менее 1000 дней.

![](../_assets/period-stat.png){width=700}

## Отчеты и графики {#common}

**Сводная статистика**

 
:   Подраздел **Сводные данные** показывает сумму событий за выбранный период и процент изменений по сравнению с предыдущим периодом такой же продолжительности. Например, если вы выбрали период **Месяц** (22.01.2023–22.02.2023), то процент изменений будет рассчитан относительно предыдущего месяца (22.12.2022–22.01.2023).

    {% include notitle [common-stat](../_includes/assets.md#common-stat) %}

    - **Переходов в профиль компании** — общие данные по всем целевым событиям во всех сервисах Яндекса;
    - **Проложено маршрутов** — количество кликов по кнопке **Построить маршрут**;
    - **Нажатий «Позвонить»** — количество кликов по кнопке **Позвонить**;
    - **Переходов на сайт** — количество кликов по ссылке с названием сайта в профиле компании на Яндексе.


{% list tabs %}

- У меня одна компания

  
  Чтобы отслеживать целевые действия, для компании автоматически создается специальный счетчик Яндекс Метрики. С его помощью сервисы Яндекса передают в Метрику информацию о взаимодействии пользователей с вашей компанией. На основе этих данных формируются графики статистики.
  
  **Источники переходов в профиль компании**
  
   
  :   График показывает, откуда перешли в профиль компании, а также сумму и процент изменений по сравнению с предыдущим периодом такой же продолжительности.
  
  **Что делали в профиле компании**
  
   
  :   График показывает действия пользователей в профиле вашей компании. Вы можете настроить действия, которые хотели бы отслеживать, в Яндекс Метрике. См. подробнее в {% if tld == "ru" or tld == "kz" or tld == "uz" %}[Справке Яндекс Метрики](https://yandex.ru/support/metrica/content/events.html#events){% endif %}{% if tld == "com" %}[Справке Яндекс Метрики](https://yandex.com/support/metrica/content/events.html#events){% endif %}{% if tld == 'com.tr' %}[Справке Яндекс Метрики](https://yandex.com.tr/support/metrica/content/events.html#events){% endif %}.
  

- У меня филиал сети

  
  Чтобы отслеживать целевые действия, для компании автоматически создается специальный счетчик Яндекс Метрики. С его помощью сервисы Яндекса передают в Метрику информацию о взаимодействии пользователей с вашей компанией. На основе этих данных формируются графики статистики.
  
  Для сетевых компаний в Яндекс Метрике достаточно создать только один счетчик на всю сеть — и статистика будет собираться суммарно по всем филиалам. Вы можете посмотреть статистику для своего филиала, но только по данным Карт и Поиска.
  
  **Источники переходов в профиль филиала**
  
   
  :   График показывает, сколько раз пользователи с Карт, Поиска и Навигатора переходили в профиль вашего филиала или открывали его: [прямые переходы](*direct-transitions) и [дискавери](*discovery) в Картах.
      
      В Поиске учитываются только те показы, которые привели к кликам внутри карточки: просмотры отзывов, фото, телефона, построение маршрутов и подобные. Переход пользователя по ссылке из поисковой выдачи не учитывается.
  
  **Что делали в профиле филиала**
  
   
  :   График показывает действия пользователей в профиле вашей компании в Картах и Поиске. Дополнительные действия настроить нельзя.

{% endlist %}



## Выгрузка статистики в Excel {#export}

Вы можете выгрузить данные любого графика в файл в формате Excel. Для этого на нужном графике в правом верхнем углу нажмите ![](../_assets/icon-export.svg). В файл будут выгружены все данные графика, даже если вы при просмотре сняли отметки с некоторых типов событий или действий.

Данные графика будут выгружены с той же группировкой, что вы установили для просмотра статистики. Например, если на графике данные сгруппированы по месяцам, то в файл Excel они будут выгружены по месяцам.


{% include [support-buttons](../_includes/support-buttons-table.md) %}

{% include [table-style-none](../_includes/table-style-none.md) %}

{% include [button-style](../_includes/yellow-button-styles.md) %}

{% include [border-style](../_includes/border-style.md) %}

{% include [cut-button-style](../_includes/cut-button-style.md) %}

{% include [footer](../_includes/footer.md) %}



[*direct-transitions]: {% include notitle [direct-transitions](../_includes/popup.md#direct-transitions) %}

[*discovery]: {% include notitle [discovery](../_includes/popup.md#discovery) %}

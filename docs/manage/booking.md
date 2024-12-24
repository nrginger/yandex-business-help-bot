# Онлайн‑запись и бронирование в профиле компании

В профилях компаний с [определенными видами деятельности](categories-all.md) можно добавить одну из кнопок действия: [Записаться онлайн](*Записаться-онлайн) или [Заказать доставку](*Заказать-доставку). Вы можете сделать это двумя способами:

- подключить компанию к сервису онлайн‑записи Яндекса через API;
- заключить договор с сервисом, который является партнером Яндекса и сообщает о возможности записи или бронирования.

## Как добавить кнопку действия в профиль своей компании {#add-all}

Подключите онлайн‑запись через партнерский сервис Яндекса или через API Яндекса.


{% list tabs %}

- Через партнерский сервис

  
  1. Подключитесь к партнеру.
      
      {% cut "Список партнеров" %}

      <div class="table-style-none">
      
      #|
      ||      
      {% if tld == "ru" or tld == "kz" or tld == "uz" %}

      - [1C Салон красоты](https://salon1c.ru/);
      
      {% endif %}
      
      {% if tld == "ru" or tld == "kz" or tld == "uz" %}

      - [Клатч](https://evolution-it.ru);
      
      {% endif %}
      
      {% if tld == "ru" or tld == "kz" or tld == "uz" %}

      - [ПрофиГид](https://profi.guide/);
      
      {% endif %}
      
      {% if tld == "ru" or tld == "kz" or tld == "uz" %}

      - [ПрофСалон](https://profsalon.org/);
      
      {% endif %}

      - [Altegio](https://alteg.io/);
      
      - [Amango](https://www.amango.ru/);
      
      - [Arnica](https://arnica.pro/);
      
      - [Beauty Expert](http://beauty-saas.ru/);
      
      - [Core12](https://core12.ru);
      
      - [Dikidi](https://dikidi.net/promo/yandex);
      |
      - [Masters](https://www.masters-app.ru/);
      
      - [Rient](https://rient.ru);
      
      - [RocketWash](https://www.rocketwash.me/);
      
      - [SberCRM](https://sbercrm.com/services);
      
      - [Sonline](https://sonline.su/);
      
      - [Sycret](https://sycret.ru/);
      
      - [Tetradka](https://plus.tetradka.io/);
      
      - [Torrow](https://info.torrow.net/service_booking);
      
      - [Universe Soft](https://www.universe-soft.ru/);
      
      - [YClients](https://www.yclients.com).
      ||
      |#

      </div>
      
      {% endcut %}
      
  1. Включите онлайн‑запись в Личном кабинете партнера.
      
  1. Пройдите модерацию в сервисе партнера.
      
  
  {% if tld == "ru" or tld == "kz" %}
  
  Если у вашей компании подключена [Рекламная подписка](../order.md) или [Приоритетное размещение](../benefits.md), и вы настраивали кнопку действия, убедитесь, что поле **Ссылка** заполнено правильно:
  1. Выберите нужную рекламную кампанию.
  1. Перейдите на вкладку **Рекламные материалы**.
      
      {% note info %}
      
      Если вы рекламируетесь в Картах, то кнопка действия находится на вкладке **Реклама в Картах**.
      
      {% endnote %}
      
  1. Выберите активную кнопку действия.
  1. В поле **Надпись на кнопке** выберите **Записаться онлайн**.
  1. Укажите ссылку на виджет партнера в поле **Ссылка**.
  
  {% endif %}
  

- Через API Яндекса

  
  Этот способ подходит для сервисов бронирования и крупных сетей, к которым подключено больше 300 организаций.
  
  Станьте партнером Яндекса и добавьте кнопку действия самостоятельно:
  
  1. Прочитайте [оферту](https://yandex.ru/legal/maps_booking_partners_api_offer/).
  1. [Отправьте заявку](https://forms.yandex.ru/surveys/11904974.7336a132c614bb1304259a42d96078a24f9a8775/) на подключение. С вами свяжется наш менеджер.
  1. Подключите API по инструкции.

{% endlist %}


Кнопка действия появится в профиле вашей компании в течение 10 дней.

Виджет онлайн‑записи Яндекса будет выглядеть одинаково, независимо от того, к какому из наших партнеров вы подключены. Настроить внешний вид кнопки действия нельзя.

{% if tld == "ru" or tld == "kz" %}

## Как скрыть кнопку действия {#hide-link}

Чтобы удалить кнопку онлайн‑записи, отключите бронирование в Личном кабинете партнера.

Отключить возможность записи или бронирования из профиля компании в Яндексе могут только компании, у которых подключена [Рекламная подписка](../order.md) или [Приоритетное размещение](../benefits.md).

Чтобы скрыть кнопку действия:

1. В интерфейсе [Яндекс Бизнеса](https://yandex.ru/business/priority/in) перейдите на вкладку **Рекламные материалы**.
    
    {% note info %}
    
    Если вы рекламируетесь в Картах, то кнопка действия находится на вкладке **Реклама в Картах**.
    
    {% endnote %}
    
1. Пролистайте страницу до блока **Кнопка действия**.
1. Нажмите ![](../_assets/spn-delete.png).
1. Подтвердите действие.
{% endif %}


{% include [support-buttons](../_includes/support-buttons-table.md) %}

{% include [footer](../_includes/footer.md) %}

{% include [table-style-none](../_includes/table-style-none.md) %}

{% include [button-style](../_includes/yellow-button-styles.md) %}



[*Заказать-доставку]: для ресторанов и кафе через сервис Яндекс Еда

[*Записаться-онлайн]: например, для салонов красоты и барбершопов через {% if tld == "ru" %}[Яндекс Карты](https://yandex.ru/support/maps/concept/booking.html){% endif %}{% if tld == "kz" %}[Яндекс Карты](https://yandex.kz/support/maps/concept/booking.html){% endif %}{% if tld == "uz" %}[Яндекс Карты](https://yandex.uz/support/maps/concept/booking.html){% endif %}{% if tld == "com" %}[Яндекс Карты](https://yandex.com/support/maps/concept/booking.html){% endif %}{% if tld == 'com.tr' %}[Яндекс Карты](https://yandex.com.tr/support/maps/concept/booking.html){% endif %}

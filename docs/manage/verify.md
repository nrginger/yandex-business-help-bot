---
keywords: как найти свою компанию
---

# Подтверждение прав на компанию

Управлять профилем компании в Яндекс Бизнесе может пользователь с  ролью **Владелец**, **Представитель** или **Представитель (Вебмастер)**. Подробнее читайте в разделе [Роли пользователей](accesses.md).

Чтобы подтвердить права на компанию, [получите код](#get-code) и [введите его в форму](#set-code).


{% note info %}

Если у компании указан неправильный номер телефона, [исправьте его](#verify-phone-num).

{% endnote %}



## Получить код {#get-code}

### Код для компании {#find-companies}

<div class="no-list-reset">

1. Найдите вашу компанию в Яндекс Бизнесе или Яндекс Картах.
    
    {% list tabs %}
    
    - Яндекс Бизнес
    
      {% include [get-code-in-business](../_includes/resource/id-get-code/in-business.md) %}
    
    - Яндекс Карты
    
      1. Найдите компанию и перейдите в ее профиль в Картах.
    
      1. Нажмите **![](../_assets/blue-check-outline.svg) Вы владелец этой организации?**      
    
            {% note info %}
          
            Ссылки **![](../_assets/blue-check-outline.svg) Вы владелец этой организации?** не будет, если в профиле компании в Яндекс Картах есть пометка, что **![](../_assets/blue-check.svg) Владелец следит за актуальностью информации** — в этом случае подтвердите права через [Личный кабинет Яндекс Бизнеса](https://business.yandex.ru/).
          
            {% endnote %}
    
    {% endlist %}
   
1. {% include [get-code-confirm-rights](../_includes/resource/id-get-code/confirm-rights.md) %}
    
1. {% include [get-code-numbers](../_includes/resource/id-get-code/numbers.md) %}

</div>    

{% include [get-code-call](../_includes/resource/id-get-code/call.md) %}


Дождитесь СМС или звонка оператора, который сообщит код, и введите код в поле **Код подтверждения**. Если не хотите ждать — закройте окно и введите код позже (см. [Если код уже есть](#set-code)).


{% note info %}

Если в течение 3 дней оператор не позвонил вам по городскому номеру, значит он не смог дозвониться, или городской номер по какой-то причине не проходит верификацию. В этом случае внесите дополнительный номер телефона в Картах через кнопку **Исправить неточность** и [подтвердите права по нему](#get-code).

{% endnote %}


### Код для сети {#network}

1. Перейдите на страницу {% if tld == "ru" %}[Организации](https://yandex.ru/sprav/companies){% endif %}{% if tld == "kz" %}[Организации](https://yandex.kz/sprav/companies){% endif %}{% if tld == "uz" %}[Организации](https://yandex.uz/sprav/companies){% endif %}{% if tld == "com" %}[Организации](https://yandex.com/sprav/companies){% endif %}{% if tld == 'com.tr' %}[Организации](https://yandex.com.tr/sprav/companies){% endif %}.
    
1. В верхней части страницы в поле **Поиск** введите название компании и нажмите ![](../_assets/search.svg). Чтобы уточнить поиск, введите регион.
    
    {% cut "Пример" %}
    
    ![](../_assets/comp-search-1.png){width=700}{.border-yes}
    
    {% endcut %}
    
1. В результатах поиска выберите сеть и нажмите ссылку в ее названии.
    
1. Укажите страну и регион, чтобы привязать филиалы в конкретном регионе.
    
1. Нажмите **Это моя сеть**.
    
1. В окне **Нужно подтвердить, что вы владелец** выберите способ получения кода — **СМС** или **Телефон**.
    
1. Выберите номер телефона, с помощью которого хотите подтвердить права.
    
1. Нажмите **Получить код** и закройте окно.

Вам перезвонит автоматический оператор и сообщит код. Или вам придет сообщение с кодом.


## Если код уже есть {#set-code}

{% include [set-code-set-code](../_includes/resource/id-set-code/set-code.md) %}


{% if tld == "ru" %}

## Права для бизнес‑центра {#business-center}

**Получить роль Владельца**

 
:   Пришлите подтверждающие документы о праве собственности на бизнес‑центр (например, выписку из ЕГРН) через форму:
    
    {% cut "Отправить документы о владении бизнес‑центром" %}
    
    <div style="padding: 15px;
         margin: 10px 0;
         background: #FFFFFF;
         border-radius: 10px;
         border: 1px solid var(--yc-color-line-generic);">
      <iframe style="background: #FFFFFF;"
            height="700"
            width="100%"
            frameborder="0"
            src="https://forms.yandex.ru/surveys/10012013/?&iframe=1">
      </iframe>
    </div>
    
    {% endcut %}

**Получить роль Представителя**

 
:   - Попросите пользователя с ролью **Владелец** [добавить](accesses.md#add-representative) вас как **Представителя**.
    - Запустите [рекламную кампанию](../benefits.md). На время действия рекламы вы получите роль **Представителя**.

{% endif %}

{% if tld == "ru" %}

## Права для агентства {#verify-agency}

Агентства не могут самостоятельно подтверждать права на компанию и получать роль **Владелец** в Яндекс Бизнесе.

Чтобы управлять профилем компании и подключать рекламу, попросите пользователя с ролью **Владелец** добавить логин агентства с ролью **Представитель**. Подробнее читайте в разделах [Подтверждение прав на компании субклиента](../agency/access.md) и [Роли пользователей](accesses.md).

{% endif %}

## Частые вопросы {#faq}


{#verify-phone-num}

{% cut "Номер не привязан к профилю или изменился" %}


Подтвердить права можно только по номеру, к которому у вас есть доступ. Если номер некорректный, исправьте его.

1. В профиле компании в Яндекс Картах нажмите **Исправить неточность**&nbsp;→ **Неправильная информация**.
1. Добавьте или исправьте номер телефона.
1. Внизу страницы нажмите **Отправить**.

Заявку на изменение номера рассмотрят в течение трех дней.


{% note alert %}

Чтобы в профиле добавился новый номер — опубликуйте его на сайте компании или подтвердите изменение оператору, который позвонит на ваш старый номер.

{% endnote %}


Как только номер появится в профиле, вы можете запросить код для подтверждения прав.


{% endcut %}

{% cut "Какой номер можно привязать к профилю" %}


Для подтверждения прав можно привязать как городской, так и мобильный номер телефона.


{% note tip %}

Для подтверждения прав привязывайте прямые номера, на которых нет голосового меню или автоответчика. Так процедура пройдет быстрее.

{% endnote %}



{% endcut %}

{% cut "Мне не пришел код. Что делать?" %}


Проверьте, что номер, который вы привязали к профилю, правильный. Как исправить номер — см. вопрос [Номер не привязан к профилю или изменился](#verify-phone-num).

Если номер верный, [перезапросите код](#get-code). Если код так и не пришел, обратитесь в [службу поддержки](https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53).


{% endcut %}

{% cut "Мне не позвонили. Что делать?" %}


Проверьте, что номер, который вы привязали к профилю, правильный. Как исправить номер — см. вопрос [Номер не привязан к профилю или изменился](#verify-phone-num).

Если номер верный, возможно, автоматический оператор не дозвонился. В этом случае заявка будет переведена в колл‑центр. В течение трех суток оператор колл‑центра вам перезвонит и сообщит код.

Если оператор так и не перезвонил, [перезапросите звонок](#get-code) или обратитесь в [службу поддержки](https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53).


{% endcut %}

{% cut "Как еще можно подтвердить права на компанию или сеть?" %}


- C помощью {% if tld == "ru" %}[Вебмастера](https://yandex.ru/support/webmaster/diagnosis/recommendations.html#diagnostics-recommendations__auto-sprav){% endif %}{% if tld == "kz" %}[Вебмастера](https://yandex.kz/support/webmaster/diagnosis/recommendations.html#diagnostics-recommendations__auto-sprav){% endif %}{% if tld == "uz" %}[Вебмастера](https://yandex.uz/support/webmaster/diagnosis/recommendations.html#diagnostics-recommendations__auto-sprav){% endif %}{% if tld == "com" %}[Вебмастера](https://yandex.com/support/webmaster/diagnosis/recommendations.html#diagnostics-recommendations__auto-sprav){% endif %}{% if tld == 'com.tr' %}[Вебмастера](https://yandex.com.tr/support/webmaster/diagnosis/recommendations.html#diagnostics-recommendations__auto-sprav){% endif %}.
    
    Если подтвердить права таким способом не получилось, обратитесь в [службу поддержки](https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53).
    
- Сетевые компании могут подтвердить права с помощью неперсональной учетной записи на корпоративном домене. Для этого нужно обратиться в [службу поддержки](https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53).


{% endcut %}

{% cut "Какую роль я получу после подтверждения прав на компанию?" %}


После подтверждения прав на компанию вам выдадут роль **Владелец**. Если у компании уже есть такой пользователь, то вам будет присвоена роль **Представитель**.


{% endcut %}

{% cut "Почему мне выдали роль Представитель, хотя я владелец компании?" %}


У компании уже есть пользователь с ролью **Владелец**. Чтобы исправить это, попросите пользователя с ролью **Владелец** переназначить эту роль на вас или обратитесь в [службу поддержки](https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53).


{% endcut %}


{% include [edu-online-business](../_includes/edu-online-business.md) %}


<div class="table-style-none">

#|
||
<a href="https://yandex.ru/chat?context=%7B%22entrypoint%22%3A%22%7B%5C%22page_name%5C%22%3A%5C%22help%5C%22%2C%5C%22a_pageurl%5C%22%3A%5C%22https%3A%2F%2Fyandex.ru%2Fsupport%2Fbusiness-priority%2Fmanage%2Fverify.html%5C%22%7D%22%7D#/user/5cb78286-a944-4c0f-bf33-b5c282eae053">
  <span class="button">Чат с поддержкой</span>
</a>
|
<a href="https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53">
  <span class="button">Письмо в поддержку</span>
</a>
||
|#

</div>

{% include [footer](../_includes/footer.md) %}

{% include [table-style-none](../_includes/table-style-none.md) %}

{% include [button-style](../_includes/yellow-button-styles.md) %}

{% include [border-style](../_includes/border-style.md) %}


<style>
.yfm .no-list-reset ol {
    counter-reset: no-reset-list !important;
}

.yfm .no-list-reset ol>li {
    counter-increment: no-reset-list !important;
}

.yfm .no-list-reset ol>li:before {
    content: counters(no-reset-list, ".") ". " !important;
}
</style>

# Как обновлять данные сети
Вы можете обновлять данные сети вручную или с помощью файлов в форматах XML и CSV.

{% list tabs %}

- Вручную
  
  **Добавить в сеть филиал**
  
  1. На странице {% if tld == "ru" %}[Организации](https://www.yandex.ru/sprav/companies/){% endif %}{% if tld == "kz" %}[Организации](https://www.yandex.kz/sprav/companies/){% endif %}{% if tld == "uz" %}[Организации](https://www.yandex.uz/sprav/companies/){% endif %}{% if tld == "com" %}[Организации](https://www.yandex.com/sprav/companies/){% endif %}{% if tld == 'com.tr' %}[Организации](https://www.yandex.com.tr/sprav/companies/){% endif %} рядом с названием нужной сети нажмите ![](../_assets/menu.png) и выберите **Добавить в сеть филиал**.
  1. Данные XML-файла должны быть на одном языке. Чтобы выбрать язык XML-файла, укажите нужное значение для `lang`.
  1. В открывшемся окне выберите филиал из списка и нажмите **Включить в сеть**.
      
  Также вы можете добавить филиал в карточке сети. Для этого перейдите в раздел **Филиалы** и нажмите **Добавить филиал**.
  
  **Создать филиал**
  
  1. На странице {% if tld == "ru" %}[Организации](https://www.yandex.ru/sprav/companies/){% endif %}{% if tld == "kz" %}[Организации](https://www.yandex.kz/sprav/companies/){% endif %}{% if tld == "uz" %}[Организации](https://www.yandex.uz/sprav/companies/){% endif %}{% if tld == "com" %}[Организации](https://www.yandex.com/sprav/companies/){% endif %}{% if tld == 'com.tr' %}[Организации](https://www.yandex.com.tr/sprav/companies/){% endif %} рядом с названием нужной сети нажмите ![](../_assets/menu.png) и выберите **Создать филиал**.

  1. В открывшемся окне заполните адрес, телефон и время работы филиала.
      
  Также вы можете создать филиал в карточке сети. Для этого перейдите в раздел **Филиалы** и нажмите **Создать филиал**.
  
  **Редактировать данные о филиалах**
  
   
  :   В разделе **Филиалы** можно массово редактировать [информацию](*информацию) о филиалах. Для этого:

      1. На странице сети в разделе **Филиалы** отметьте нужные филиалы или выберите всю сеть.
          
      1. Нажмите **Редактировать** и выберите из списка данные, которые хотите изменить.
          
      1. В открывшемся окне можно добавить или удалить информацию о филиалах. Например, если выбрать **Телефон** и удалить какой‑либо номер из предложенного списка, он будет удален во всех выбранных филиалах.

      Отредактировать фотографии и другие данные можно также в карточке филиала. Для этого:
      
      1. Перейдите в карточку филиала.
      1. Нажмите ![](../_assets/edit-icon.png)**Редактировать данные**.
      1. Внесите нужные изменения.
      1. Нажмите **Сохранить**.
  
  **Удалить филиал**
  
  1. Перейдите в раздел **Филиалы**.
  1. Отметьте нужный(‑е) филиал(‑ы).
  1. Нажмите **Исключить из сети** или **Удалить**.
      
      **Исключить из сети** — филиал выйдет из состава сети, закроется в Яндекс Картах, вы потеряете доступ к его карточке.
      
      **Удалить** — филиал останется в составе сети, закроется в Яндекс Картах, вы потеряете доступ к его карточке.
    
- Через файл XML

  
  Если в вашей сети более 30 филиалов, рекомендуем обновлять данные в Яндекс Бизнесе [с помощью XML‑файла](*с-помощью-XML‑файла).
  
  Данные о ваших филиалах будут обновлены на основе информации из файла XML. Новые филиалы будут добавлены в базу и будут отображаться в сервисах с указанными признаками. Карточки филиалов, сведения о которых не добавлены в XML‑файл, будут закрыты.
  
  **Шаг 1. Подготовьте XML‑файл**
  
   
  :   {% cut "Требования к файлу" %}
      
      
      1. XML‑файл должен быть создан в кодировке UTF‑8.
      1. Стандартный XML‑заголовок должен начинаться с первой строки, с нулевого символа.
          
          Например:
          ```xml
          <?xml version="1.0" encoding="UTF-8"?>
          ```
          
      1. Для описания филиалов используйте [набор обязательных и дополнительных признаков](#parameters-description). Каждое свойство филиала оборачивайте в отдельный признак (см. [Пример файла](#example)). Если для одного свойства есть несколько значений (например телефонов), передавайте несколько признаков с одинаковыми именами.
      1. Данные XML-файла должны быть на одном языке. Исключение составляют мультиязычные признаки (см. [Описание признаков](#parameters-description)).
          
          _Мультиязычный признак_ ― признак в XML-файле со значениями на нескольких языках.
          
          Язык определяется атрибутом `lang`. Для каждого нового языка указывайте признак со своим атрибутом `lang` на отдельной строке.
          
          {% cut "Пример" %}
          
          ```xml
          <address lang="ru">город Екатеринбург, просп. Ленина, 101, а</address>
          <address lang="en">Ekaterinburg, prosp. Lenina, 101, a</address>
          ```
          
          {% endcut %}
          
          Актуальные значения `lang` вы найдете в {% if tld == "ru" or tld == "kz" or tld == "uz" %}[схеме XML](https://yastatic.net/s3/doc-binary/src/support/business-priority/ru/files/partner-public.xsd){% endif %}{% if tld == "com" or tld == 'com.tr' %}[схеме XML](https://yastatic.net/s3/doc-binary/src/support/business-priority/en/files/partner-public-en.xsd){% endif %}. Чтобы добавить другие языки, обратитесь в [службу поддержки](https://yandex.ru/support2/business-feedback/ru/).
          
      1. В данных не должно быть HTML‑признаков. В стандарте XML недопустимы символы с ASCII‑кодами в диапазоне значений от 0 до 31 в текстовых полях. Исключениями являются значения 9 (табуляция), 10 (перевод строки), 13 (возврат каретки). Также по стандарту XML нужно заменять символ `&` на `&amp;`.
      
      
      {% endcut %}

      {% cut "Описание признаков" %} {#parameters-description}
      
      #|
      ||
      **Признак**
      |
      **Описание**
      |
      **Мультиязычный элемент**
      |
      **Обязательное поле**
      ||
      ||
      companies
      |
      {% include [popup-companies](../_includes/popup/id-popup/companies.md) %}
      |
      Н/п
      |
      Да
      ||
      ||
      company
      |
      {% include [popup-company](../_includes/popup/id-popup/company.md) %}
      |
      Н/п
      |
      Да
      ||
      ||
      company-id
      |
      {% include [popup-company-id](../_includes/popup/id-popup/company-id.md) %}
      |
      Нет
      |
      Да
      ||
      ||
      name
      |
      {% include [popup-name](../_includes/popup/id-popup/name.md) %}
      |
      Да
      |
      Да
      ||
      ||
      shortname
      |
      {% include [popup-shortname](../_includes/popup/id-popup/shortname.md) %}
      |
      Да
      |
      Нет
      ||
      ||
      name-other
      |
      {% include [popup-name-other](../_includes/popup/id-popup/name-other.md) %}
      |
      Да
      |
      Нет
      ||
      ||
      address
      |
      {% include [popup-address](../_includes/popup/id-popup/address.md) %}
      |
      Да
      |
      Да
      ||
      ||
      country
      |
      {% include [popup-country](../_includes/popup/id-popup/country.md) %}
      |
      Да
      |
      Нет
      ||
      ||
      address-add
      |
      {% include [popup-address-add](../_includes/popup/id-popup/address-add.md) %}
      |
      Да
      |
      Нет
      ||
      ||
      phone
      |
      {% include [popup-phone](../_includes/popup/id-popup/phone.md) %}
      |
      Нет
      |
      Да
      ||
      ||
      **Элементы, вложенные в phone**
      ||
      ||
      number
      |
      {% include [popup-number](../_includes/popup/id-popup/number.md) %}
      |
      
      |
      
      ||
      ||
      ext
      |
      {% include [popup-ext](../_includes/popup/id-popup/ext.md) %}
      |
      
      |
      
      ||
      ||
      info
      |
      {% include [popup-info](../_includes/popup/id-popup/info.md) %}
      |
      
      |
      
      ||
      ||
      type
      |
      {% include [popup-type](../_includes/popup/id-popup/type.md) %}
      |
      
      |
      
      ||
      ||
      
      ||
      ||
      email
      |
      {% include [popup-email](../_includes/popup/id-popup/email.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      url
      |
      {% include [popup-url](../_includes/popup/id-popup/url.md) %}
      |
      Нет
      |
      Да
      ||
      ||
      add-url
      |
      {% include [popup-add-url](../_includes/popup/id-popup/add-url.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      info-page
      |
      {% include [popup-info-page](../_includes/popup/id-popup/info-page.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      working-time
      |
      {% include [popup-working-time](../_includes/popup/id-popup/working-time.md) %}
      |
      Да
      |
      Да
      ||
      ||
      rubric-id
      |
      {% include [popup-rubric-id](../_includes/popup/id-popup/rubric-id.md) %}
      |
      Нет
      |
      Да
      ||
      ||
      actualization-date
      |
      {% include [popup-actualization-date](../_includes/popup/id-popup/actualization-date.md) %}
      |
      Нет
      |
      Да
      ||
      ||
      coordinates
      |
      {% include [popup-coordinates](../_includes/popup/id-popup/coordinates.md) %}
      |
      Нет
      |
      Да
      ||
      ||
      **Элементы, вложенные в coordinates**
      ||
      ||
      lon
      |
      {% include [popup-lon](../_includes/popup/id-popup/lon.md) %}
      |
      
      |
      
      ||
      ||
      lat
      |
      {% include [popup-lat](../_includes/popup/id-popup/lat.md) %}
      |
      
      |
      
      ||
      ||
      
      ||
      ||
      photos
      |
      {% include [popup-photos](../_includes/popup/id-popup/photos.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      **Элементы, вложенные в photos**
      ||
      ||
      tag
      |
      {% include [popup-tag](../_includes/popup/id-popup/tag.md) %}
      |
      
      |
      
      ||
      ||
      
      ||
      ||
      feature-boolean
      |
      {% include [popup-feature-boolean](../_includes/popup/id-popup/feature-boolean.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-enum-single
      |
      {% include [popup-feature-enum-single](../_includes/popup/id-popup/feature-enum-single.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-enum-multiple
      |
      {% include [popup-feature-enum-multiple](../_includes/popup/id-popup/feature-enum-multiple.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-numeric-single
      |
      {% include [popup-feature-numeric-single](../_includes/popup/id-popup/feature-numeric-single.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-numeric-multiple
      |
      {% include [popup-feature-numeric-multiple](../_includes/popup/id-popup/feature-numeric-multiple.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-in-units-single
      |
      {% include [popup-feature-in-units-single](../_includes/popup/id-popup/feature-in-units-single.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-in-units-multiple
      |
      {% include [popup-feature-in-units-multiple](../_includes/popup/id-popup/feature-in-units-multiple.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-range-single
      |
      {% include [popup-feature-range-single](../_includes/popup/id-popup/feature-range-single.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-range-in-units-single
      |
      {% include [popup-feature-range-in-units-single](../_includes/popup/id-popup/feature-range-in-units-single.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-range-in-units-multiple
      |
      {% include [popup-feature-range-in-units-multiple](../_includes/popup/id-popup/feature-range-in-units-multiple.md) %}
      |
      Нет
      |
      Нет
      ||
      ||
      feature-text-single
      |
      {% include [popup-feature-text-single](../_includes/popup/id-popup/feature-text-single.md) %}
      |
      Нет
      |
      Нет
      ||
      |#
      
      {% endcut %}
      
      {% cut "Дополнительные признаки" %}
      
      
      Через XML‑файл вы можете передавать дополнительные признаки для вашей сети или филиала. Например, указать, есть ли возле вашего торгового центра парковка или в какой валюте можно получить деньги в вашем банкомате.
      
      Чтобы получить XML‑файл со списком возможных признаков для вашего вида деятельности:
      
      1. На странице сети перейдите в раздел **Филиалы**.
      1. В блоке **Управление филиалами** выберите **Файл**.
      1. Нажмите **Выгрузить данные**&nbsp;→ **Выгрузить признаки**.
      
      Если есть вопросы по выгрузке файла с дополнительными признаками, напишите [нам](mailto:partner@sprav.yandex.ru).
      
      
      {% endcut %}

      {% cut "Пример файла" %} {#example}
      
      {% note info %}
      
      Чтобы открыть описание признака из примера файла, нажмите на название любого подсвеченного признака.
      
      {% endnote %}
      
      
      ```xml
      <?xml version="1.0" encoding="UTF-8"?> 
      <companies>
        <company>
          <company-id>770704034</company-id>
          <name lang="ru">Якорь</name>
          <shortname lang="ru">Якорь</shortname>
          <address lang="ru">город Екатеринбург, просп. Ленина, 101, а</address>
          <country lang="ru">Россия</country>
          <address-add lang="ru">ТЦ Ромашка, 2 этаж, офис 203</address-add>
          <phone>
            <number>+7 (343) 375-13-99</number>
            <ext>555</ext>
            <info>секретарь</info>
            <type>phone</type>
          </phone>
          <phone>
            <type>phone</type>
            <number>+7 (800) 200-23-45</number>
            <info/>
          </phone>
          <email>info@yakor-anapa.ru</email>
          <url>http://www.yakor-anapa.ru</url>
          <add-url>http://www.yakoranapa.ru</add-url>
          <info-page>http://www.test.ru/yakor-anapa</info-page>
          <working-time lang="ru">ежедн. 10:00-21:00</working-time>
          <rubric-id>184106414</rubric-id>
          <rubric-id>184106394</rubric-id>
          <actualization-date>1511724300</actualization-date>
          <photos gallery-url="http://test.ru/yakor-anapa/gallery">
            <photo url="http://test.ru/yakor-anapa/11_b.jpg" alt="Ресторан отеля" 
            type="interior"></photo>
            <photo url="http://test.ru/yakor-anapa/19_b.jpg">
              <tag>EXTERIOR</tag>
            </photo>
            <photo url="http://test.ru/yakor-anapa/25_b.jpg"></photo>
            <photo url="http://test.ru/yakor-anapa/26_b.jpg"></photo>
            <photo url="http://test.ru/yakor-anapa/17_b.jpg"></photo>
            <photo url="http://test.ru/yakor-anapa/drink1.jpg" alt="Коктейль в баре отеля">
              <tag>FOOD</tag>
            </photo>
          </photos>
          <feature-boolean name="internet" value="1"/>
          <feature-enum-single name="star" value="five"/>
          <feature-numeric-single name="room_number" value="15"/>
          <feature-enum-multiple name="hotel_type" value="art_hotel"/>
          <feature-numeric-multiple name="license_number" value="004555"/>
          <feature-in-units-single name="minimum_order" unit="money" unit-value="rub" value="300"/>
          <feature-in-units-multiple name="ats_by_type" unit="apartment_type" unit-value="single" value="200"/>
          <feature-range-single name="number_seats_banquet_hall" from="15" to="20"/>
          <feature-range-in-units-single name="tickets" unit="money" unit-value="rub" from="100" to="150"/>
          <feature-range-in-units-single name="price_1_min" unit="money" unit-value="rub" from="7" to="10"/>
          <feature-range-in-units-multiple name="tea" unit="money" unit-value="rub" from="100" to="300"/>
          <feature-text-single value="Yakor_free_wi-fi" name="ssid"/>
        </company>
        <company>
          <company-id>7707040070</company-id>
          <name lang="ru">Якорьбанк</name>
          <shortname lang="ru">Якорьбанк</shortname>
          <name-other lang="ru">Якорьбанк, платёжное устройство</name-other>
          <address lang="ru">Россия, Республика Татарстан, Зеленодольский район, село Нурлаты, улица Гагарина, 46</address>
          <phone>
            <ext/><type>phone</type>
            <number>+7 (800) 999-99-90</number>
            <info/>
          </phone>
          <url>http://www.yakorbank.ru/</url>
          <working-time lang="ru">будни 8:30-18:00, сб 9:00-14:30</working-time>
          <rubric-id>184106974</rubric-id>
          <actualization-date>23.09.2019</actualization-date>
          <coordinates>
            <lon>48.295532</lon>
            <lat>55.616051</lat>
          </coordinates>
        </company>
      </companies>
      ```
      {% if tld == "kz" %}
      ```xml
      <?xml version="1.0" encoding="UTF-8"?> 
      <companies>
        <company>
          <company-id>770704034</company-id>
          <name lang="kk">Якорь</name>
          <shortname lang="kk">Якорь</shortname>
          <address lang="kk">город Алматы, просп. Ленина, 101, а</address>
          <country lang="kk">Казахстан</country>
          <address-add lang="kk">ТЦ Ромашка, 2 этаж, офис 203</address-add>
          <phone>
            <number>+7 (343) 375-13-99</number>
            <ext>555</ext>
            <info>секретарь</info>
            <type>phone</type>
          </phone>
          <phone>
            <type>phone</type>
            <number>+7 (800) 200-23-45</number>
            <info/>
          </phone>
          <email>info@yakor.kz</email>
          <url>http://www.yakor.kz</url>
          <add-url>http://www.yakor.kz</add-url>
          <info-page>http://www.test.kz/yakor</info-page>
          <working-time lang="kk">ежедн. 10:00-21:00</working-time>
          <rubric-id>184106414</rubric-id>
          <rubric-id>184106394</rubric-id>
          <actualization-date>1511724300</actualization-date>
          <photos gallery-url="http://test.kz/yakor/gallery">
            <photo url="http://test.kz/yakor/11_b.jpg" alt="Ресторан отеля" 
            type="interior"></photo>
            <photo url="http://test.kz/yakor/19_b.jpg">
              <tag>EXTERIOR</tag>
            </photo>
            <photo url="http://test.kz/yakor/25_b.jpg"></photo>
            <photo url="http://test.kz/yakor/26_b.jpg"></photo>
            <photo url="http://test.kz/yakor/17_b.jpg"></photo>
            <photo url="http://test.kz/yakor/drink1.jpg" alt="Коктейль в баре отеля">
              <tag>FOOD</tag>
            </photo>
          </photos>
          <feature-boolean name="internet" value="1"/>
          <feature-enum-single name="star" value="five"/>
          <feature-numeric-single name="room_number" value="15"/>
          <feature-enum-multiple name="hotel_type" value="art_hotel"/>
          <feature-numeric-multiple name="license_number" value="004555"/>
          <feature-in-units-single name="minimum_order" unit="money" unit-value="rub" value="300"/>
          <feature-in-units-multiple name="ats_by_type" unit="apartment_type" unit-value="single" value="200"/>
          <feature-range-single name="number_seats_banquet_hall" from="15" to="20"/>
          <feature-range-multiple name="tickets" unit="money" unit-value="rub" from="100" to="150"/>
          <feature-range-in-units-single name="price_1_min" unit="money" unit-value="rub" from="7" to="10"/>
          <feature-range-in-units-multiple name="tea" unit="money" unit-value="rub" from="100" to="300"/>
          <feature-text-single value="Yakor_free_wi-fi" name="ssid"/>
        </company>
        <company>
          <company-id>7707040070</company-id>
          <name lang="kk">Якорьбанк</name>
          <shortname lang="kk">Якорьбанк</shortname>
          <name-other lang="kk">Якорьбанк, платёжное устройство</name-other>
          <address lang="kk">Казахстан, город Алматы, улица Пушкина, 127</address>
          <phone>
            <ext/><type>phone</type>
            <number>+7 (800) 999-99-90</number>
            <info/>
          </phone>
          <url>http://www.yakorbank.kz/</url>
          <working-time lang="kk">будни 8:30-18:00, сб 9:00-14:30</working-time>
          <rubric-id>184106974</rubric-id>
          <actualization-date>23.09.2019</actualization-date>
          <coordinates>
            <lon>48.295532</lon>
            <lat>55.616051</lat>
          </coordinates>
        </company>
      </companies>
      ```
      {% endif %}{% if tld == "uz" %}
      ```xml
      <?xml version="1.0" encoding="UTF-8"?> 
      <companies>
        <company>
          <company-id>770704034</company-id>
          <name lang="uz">Якорь</name>
          <shortname lang="uz">Якорь</shortname>
          <address lang="uz">город Ташкент, просп. Ленина, 101, а</address>
          <country lang="uz">Узбекистан</country>
          <address-add lang="uz">ТЦ Ромашка, 2 этаж, офис 203</address-add>
          <phone>
            <number>+7 (343) 375-13-99</number>
            <ext>555</ext>
            <info>секретарь</info>
            <type>phone</type>
          </phone>
          <phone>
            <type>phone</type>
            <number>+7 (800) 200-23-45</number>
            <info/>
          </phone>
          <email>info@yakor.uz</email>
          <url>http://www.yakor.uz</url>
          <add-url>http://www.yakor.uz</add-url>
          <info-page>http://www.test.uz/yakor</info-page>
          <working-time lang="uz">ежедн. 10:00-21:00</working-time>
          <rubric-id>184106414</rubric-id>
          <rubric-id>184106394</rubric-id>
          <actualization-date>1511724300</actualization-date>
          <photos gallery-url="http://test.uz/yakor/gallery">
            <photo url="http://test.uz/yakor/11_b.jpg" alt="Ресторан отеля" 
            type="interior"></photo>
            <photo url="http://test.uz/yakor/19_b.jpg">
              <tag>EXTERIOR</tag>
            </photo>
            <photo url="http://test.uz/yakor/25_b.jpg"></photo>
            <photo url="http://test.uz/yakor/26_b.jpg"></photo>
            <photo url="http://test.uz/yakor/17_b.jpg"></photo>
            <photo url="http://test.uz/yakor/drink1.jpg" alt="Коктейль в баре отеля">
              <tag>FOOD</tag>
            </photo>
          </photos>
          <feature-boolean name="internet" value="1"/>
          <feature-enum-single name="star" value="five"/>
          <feature-numeric-single name="room_number" value="15"/>
          <feature-enum-multiple name="hotel_type" value="art_hotel"/>
          <feature-numeric-multiple name="license_number" value="004555"/>
          <feature-in-units-single name="minimum_order" unit="money" unit-value="rub" value="300"/>
          <feature-in-units-multiple name="ats_by_type" unit="apartment_type" unit-value="single" value="200"/>
          <feature-range-single name="number_seats_banquet_hall" from="15" to="20"/>
          <feature-range-multiple name="tickets" unit="money" unit-value="rub" from="100" to="150"/>
          <feature-range-in-units-single name="price_1_min" unit="money" unit-value="rub" from="7" to="10"/>
          <feature-range-in-units-multiple name="tea" unit="money" unit-value="rub" from="100" to="300"/>
          <feature-text-single value="Yakor_free_wi-fi" name="ssid"/>
        </company>
        <company>
          <company-id>7707040070</company-id>
          <name lang="uz">Якорьбанк</name>
          <shortname lang="uz">Якорьбанк</shortname>
          <name-other lang="uz">Якорьбанк, платёжное устройство</name-other>
          <address lang="uz">Узбекистан, город Ташкент, улица Паркент, 74</address>
          <phone>
            <ext/><type>phone</type>
            <number>+998 99 999 99 90</number>
            <info/>
          </phone>
          <url>http://www.yakorbank.uz/</url>
          <working-time lang="uz">будни 8:30-18:00, сб 9:00-14:30</working-time>
          <rubric-id>184106974</rubric-id>
          <actualization-date>23.09.2019</actualization-date>
          <coordinates>
            <lon>48.295532</lon>
            <lat>55.616051</lat>
          </coordinates>
        </company>
      </companies>
      ```
      {% endif %}{% if tld == 'com.tr' %}
      ```xml
      <?xml version="1.0" encoding="UTF-8"?> 
      <companies>
        <company>
          <company-id>770704034</company-id>
          <name lang="tr">Якорь</name>
          <shortname lang="tr">Якорь</shortname>
          <address lang="tr">город Стамбул, улица Бююк Постане, 7</address>
          <country lang="tr">Турция</country>
          <address-add lang="tr">ТЦ Роза, 2 этаж, офис 203</address-add>
          <phone>
            <number>020 1234 5678</number>
            <ext>555</ext>
            <info>секретарь</info>
            <type>phone</type>
          </phone>
          <phone>
            <type>phone</type>
            <number>034 2202 3303</number>
            <info/>
          </phone>
          <email>info@anchor.com.tr</email>
          <url>http://www.anchor.com.tr</url>
          <add-url>http://www.anchor.com.tr</add-url>
          <info-page>http://www.test.com.tr/anchor</info-page>
          <working-time lang="tr">ежедн. 10:00-21:00</working-time>
          <rubric-id>184106414</rubric-id>
          <rubric-id>184106394</rubric-id>
          <actualization-date>1511724300</actualization-date>
          <photos gallery-url="http://test.com.tr/anchor/gallery">
            <photo url="http://test.com.tr/anchor/11_b.jpg" alt="Ресторан отеля" 
            type="interior"></photo>
            <photo url="http://test.com.tr/anchor/19_b.jpg">
              <tag>EXTERIOR</tag>
            </photo>
            <photo url="http://test.com.tr/anchor/25_b.jpg"></photo>
            <photo url="http://test.com.tr/anchor/26_b.jpg"></photo>
            <photo url="http://test.com.tr/anchor/17_b.jpg"></photo>
            <photo url="http://test.com.tr/anchor/drink1.jpg" alt="Коктейль в баре отеля">
              <tag>FOOD</tag>
            </photo>
          </photos>
          <feature-boolean name="internet" value="1"/>
          <feature-enum-single name="star" value="five"/>
          <feature-numeric-single name="room_number" value="15"/>
          <feature-enum-multiple name="hotel_type" value="art_hotel"/>
          <feature-numeric-multiple name="license_number" value="004555"/>
          <feature-in-units-single name="minimum_order" unit="money" unit-value="gbp" value="30"/>
          <feature-in-units-multiple name="ats_by_type" unit="apartment_type" unit-value="single" value="200"/>
          <feature-range-single name="number_seats_banquet_hall" from="15" to="20"/>
          <feature-range-multiple name="tickets" unit="money" unit-value="gbp" from="10" to="15"/>
          <feature-range-in-units-single name="price_1_min" unit="money" unit-value="gbp" from="7" to="10"/>
          <feature-range-in-units-multiple name="tea" unit="money" unit-value="gbp" from="100" to="300"/>
          <feature-text-single value="Anchor_free_wi-fi" name="ssid"/>
        </company>
        <company>
          <company-id>7707040070</company-id>
          <name lang="tr">Якорьбанк</name>
          <shortname lang="tr">Якорьбанк</shortname>
          <name-other lang="tr">Якорьбанк, платёжное устройство</name-other>
          <address lang="tr">Турция, Стамбул, Фатих, махалле Хобьяр, улица Бююк Постане, 7</address>
          <phone>
            <ext/><type>phone</type>
            <number>+90 999 999 99 90</number>
            <info/>
          </phone>
          <url>http://www.anchorbank.com.tr/</url>
          <working-time lang="tr">будни 8:30-18:00, сб 9:00-14:30</working-time>
          <rubric-id>184106974</rubric-id>
          <actualization-date>23.09.2019</actualization-date>
          <coordinates>
            <lon>48.295532</lon>
            <lat>55.616051</lat>
          </coordinates>
        </company>
      </companies>
      ```
      {% endif %}{% if tld == "com" %}
      ```xml
      <?xml version="1.0" encoding="UTF-8"?> 
      <companies>
        <company>
          <company-id>770704034</company-id>
          <name lang="en">Якорь</name>
          <shortname lang="en">Якорь</shortname>
          <address lang="en">город Лондон, ул. Бейкер-стрит, 101, а</address>
          <country lang="en">Великобритания</country>
          <address-add lang="en">ТЦ Роза, 2 этаж, офис 203</address-add>
          <phone>
            <number>020 1234 5678</number>
            <ext>555</ext>
            <info>секретарь</info>
            <type>phone</type>
          </phone>
          <phone>
            <type>phone</type>
            <number>034 2202 3303</number>
            <info/>
          </phone>
          <email>info@anchor.com</email>
          <url>http://www.anchor.com</url>
          <add-url>http://www.anchor.com</add-url>
          <info-page>http://www.test.com/anchor</info-page>
          <working-time lang="en">ежедн. 10:00-21:00</working-time>
          <rubric-id>184106414</rubric-id>
          <rubric-id>184106394</rubric-id>
          <actualization-date>1511724300</actualization-date>
          <photos gallery-url="http://test.com/anchor/gallery">
            <photo url="http://test.com/anchor/11_b.jpg" alt="Ресторан отеля" 
            type="interior"></photo>
            <photo url="http://test.com/anchor/19_b.jpg">
              <tag>EXTERIOR</tag>
            </photo>
            <photo url="http://test.com/anchor/25_b.jpg"></photo>
            <photo url="http://test.com/anchor/26_b.jpg"></photo>
            <photo url="http://test.com/anchor/17_b.jpg"></photo>
            <photo url="http://test.com/anchor/drink1.jpg" alt="Коктейль в баре отеля">
              <tag>FOOD</tag>
            </photo>
          </photos>
          <feature-boolean name="internet" value="1"/>
          <feature-enum-single name="star" value="five"/>
          <feature-numeric-single name="room_number" value="15"/>
          <feature-enum-multiple name="hotel_type" value="art_hotel"/>
          <feature-numeric-multiple name="license_number" value="004555"/>
          <feature-in-units-single name="minimum_order" unit="money" unit-value="gbp" value="30"/>
          <feature-in-units-multiple name="ats_by_type" unit="apartment_type" unit-value="single" value="200"/>
          <feature-range-single name="number_seats_banquet_hall" from="15" to="20"/>
          <feature-range-multiple name="tickets" unit="money" unit-value="gbp" from="10" to="15"/>
          <feature-range-in-units-single name="price_1_min" unit="money" unit-value="gbp" from="7" to="10"/>
          <feature-range-in-units-multiple name="tea" unit="money" unit-value="gbp" from="100" to="300"/>
          <feature-text-single value="Anchor_free_wi-fi" name="ssid"/>
        </company>
        <company>
          <company-id>7707040070</company-id>
          <name lang="en">Якорьбанк</name>
          <shortname lang="en">Якорьбанк</shortname>
          <name-other lang="en">Якорьбанк, платёжное устройство</name-other>
          <address lang="en">Великобритания, графство Мерсисайд, Ливерпуль, ул.Мэтью-стрит, 46</address>
          <phone>
            <ext/><type>phone</type>
            <number>040 9988 7444</number>
            <info/>
          </phone>
          <url>http://www.anchorbank.com/</url>
          <working-time lang="en">будни 8:30-18:00, сб 9:00-14:30</working-time>
          <rubric-id>184106974</rubric-id>
          <actualization-date>23.09.2019</actualization-date>
          <coordinates>
            <lon>48.295532</lon>
            <lat>55.616051</lat>
          </coordinates>
        </company>
      </companies>
      ```
      {% endif %}

      {% endcut %}
      
      
      Файл можно проверить:
      
      - С помощью [валидатора Вебмастера](https://webmaster.yandex.ru/tools/xml-validator/). Выберите схему валидации документа — **Бизнес** и источник XML‑данных для валидации — файл, ссылку или текст.
          
      - Самостоятельно на своем компьютере с помощью {% if tld == "ru" or tld == "kz" or tld == "uz" %}[схемы (XML Schema Definition)](https://yastatic.net/s3/doc-binary/src/support/business-priority/ru/files/partner-public.xsd){% endif %}{% if tld == "com" or tld == 'com.tr' %}[схемы (XML Schema Definition)](https://yastatic.net/s3/doc-binary/src/support/business-priority/en/files/partner-public-en.xsd){% endif %}.
  
  **Шаг 2. Загрузите файл на свой сайт**
  
   
  :   Загрузите файл на свой сайт по обновляемой ссылке. Данные должны быть доступны по протоколу HTTP или HTTPS.
  
  **Шаг 3. Укажите ссылку на файл в Яндекс Бизнесе**
  
   
  :   1. На странице сети перейдите в раздел **Филиалы**.
      1. В блоке **Управление филиалами** выберите **Файл**.
      1. Добавьте ссылку на подготовленный файл, выберите тип **XML** и нажмите **Проверить**. Проверка файла может занять несколько часов.
      1. Если проверка файла прошла успешно, нажмите кнопку **Опубликовать**. В открывшемся окне проверьте изменения в филиалах. На карте может быть показано до 50 филиалов с изменениями. Нажмите **Все верно, начать загрузку в базу**. Данные из файла пройдут модерацию и будут загружены в базу Яндекс Бизнеса. При большом объеме данных загрузка может занять несколько суток.
          
          Если в результате проверки файла будут обнаружены ошибки, вы увидите сообщение об этом. Исправьте ошибки и снова отправьте файл на проверку.
          
      
      Чтобы посмотреть изменения в филиалах, загруженные в базу Яндекс Бизнеса из файла, нажмите **История загрузок**. Кнопка будет доступна спустя сутки после первой загрузки.
      
      Новые филиалы и другие изменения будут доступны в Яндекс Картах в течение нескольких дней.
  

- Через файл CSV

  
  Формат CSV ― текстовый формат, предназначенный для представления табличных данных. Первая строка содержит названия столбцов, а следующие строки ― сами данные. Содержимое столбцов отделяется друг от друга запятой.
  
  Данные в файле должны быть в кодировке UTF‑8.
  
  Вы можете скачать {% if tld == "ru" or tld == "kz" or tld == "uz" %}[пример CSV‑файла](https://download.cdn.yandex.net/support/ru/sprav/files/import-branches-example.csv){% endif %}{% if tld == "com" or tld == 'com.tr' %}[пример CSV‑файла](https://yastatic.net/s3/doc-binary/src/support/business-priority/en/files/import-branches-example_eng.csv){% endif %}.
  
  Чтобы просмотреть пример в LibreOffice, импортируйте текст: выберите кодировку UTF‑8, разделитель ― запятая, разделитель текста ― двойные кавычки.
  
  Чтобы просмотреть пример в Excel, откройте через меню **Данные**&nbsp;→ **Получение внешних данных**&nbsp;→ **Из текста**. Выберите кодировку UTF‑8, разделитель —запятая, ограничитель строк — двойные кавычки.
  
  **Шаг 1. Подготовьте CSV‑файл**
  
   
  :   Чтобы настроить автоматическое ежедневное обновление данных о ваших филиалах, подготовьте файл в формате CSV. Данные должны быть в кодировке UTF‑8.
      
      
      #|
      ||
      **Признак**
      |
      **Описание**
      |
      **Обязательное поле**
      ||
      ||
      `name`
      |
      {% include [popup-name](../_includes/popup/id-popup/name.md) %}
      |
      Да
      ||
      ||
      `country`
      |
      {% include [popup-country](../_includes/popup/id-popup/country.md) %}
      |
      Да
      ||
      ||
      `address`
      |
      Полный адрес местонахождения филиала, с точностью до номера дома.
      |
      Да
      ||
      ||
      `address-add`
      |
      {% include [popup-address-add](../_includes/popup/id-popup/address-add.md) %}
      |
      Да
      ||
      ||
      `phone`
      |
      Номер телефона с кодом страны и населенного пункта. Если номеров несколько, отделяйте их друг от друга точкой с запятой ;.
      |
      Да
      ||
      ||
      `rubric-id`
      |
      {% if tld == "ru" or tld == "kz" or tld == "uz" %}[Идентификатор вида деятельности](https://download.cdn.yandex.net/support/ru/sprav/files/rubric.xlsx){% endif %}{% if tld == "com" or tld == 'com.tr' %}[Идентификатор вида деятельности](https://yastatic.net/s3/doc-binary/src/support/business-priority/en/files/rubrics_en.xlsx){% endif %}, к которому относится данный филиал. Если видов деятельности несколько, указывайте их через запятую. У каждого филиала может быть до трех видов деятельности, но хотя бы один из них должен совпадать с видом деятельности сети.
      |
      Да
      ||
      ||
      `url`
      |
      {% include [popup-url](../_includes/popup/id-popup/url.md) %}
      |
      Да
      ||
      ||
      `add-url`
      |
      Дополнительный сайт сети (например ссылки на страницы в социальных сетях).
      |
      Нет
      ||
      ||
      `working-time`
      |
      {% include [popup-working-time](../_includes/popup/id-popup/working-time.md) %}
      |
      Да
      ||
      ||
      `lat`
      |
      Географическая широта местоположения филиала. В качестве разделителя целой и дробной части используйте точку.
      |
      Да (если адрес неточный)
      ||
      ||
      `lon`
      |
      Географическая долгота местоположения филиала. В качестве разделителя целой и дробной части используйте точку.
      |
      Да (если адрес неточный)
      ||
      |#
  
  **Шаг 2. Загрузите файл на сайт**
  
   
  :   Загрузите файл на свой сайт по обновляемой ссылке. Данные должны быть доступны по протоколу HTTP или HTTPS.
  
  **Шаг 3. Укажите ссылку на файл в Яндекс Бизнесе**
  
  1. На странице сети перейдите в раздел **Филиалы**.
  1. В блоке **Управление филиалами** выберите **Файл**.
  1. Добавьте ссылку на подготовленный файл, выберите тип **CSV** и нажмите **Проверить**. Проверка файла может занять несколько часов.
  1. Если проверка файла прошла успешно, нажмите кнопку **Опубликовать**. В открывшемся окне проверьте изменения в филиалах. На карте может быть показано до 50 филиалов с изменениями. Нажмите **Все верно, начать загрузку в базу**. Данные из файла пройдут модерацию и будут загружены в базу Яндекс Бизнеса. При большом объеме данных загрузка может занять несколько суток.
    Если в результате проверки файла будут обнаружены ошибки, вы увидите сообщение об этом. Исправьте ошибки и снова отправьте файл на проверку.
  
  
  Чтобы посмотреть изменения в филиалах, загруженные в базу Яндекс Бизнеса из файла, нажмите **История загрузок**. Кнопка будет доступна через сутки после первой загрузки.
  
  Для однократного обновления данных сохраните файл в формате CSV или XSLX и передайте с помощью [формы](https://yandex.ru/support2/business-feedback/ru/). Укажите в сообщении актуальную электронную почту и телефон вашей компании. Если у нас возникнут вопросы по загруженному файлу, мы свяжемся с вами.
  
  Новые данные появятся в Яндекс Картах в течение нескольких дней после загрузки правильно оформленного файла.

{% endlist %}


<div class="table-style-none">

#|
||
<a href="https://yandex.ru/chat?context=%7B%22entrypoint%22%3A%22%7B%5C%22page_name%5C%22%3A%5C%22help%5C%22%2C%5C%22a_pageurl%5C%22%3A%5C%22https%3A%2F%2Fyandex.ru%2Fsupport%2Fbusiness-priority%2Fbranches%2Fbasic.html%5C%22%7D%22%7D#/user/5cb78286-a944-4c0f-bf33-b5c282eae053?utm-source=chat-in-help" target="_blank">
  <span class="button">Чат с поддержкой</span>
</a>
|
<a href="https://yandex.ru/support2/business-feedback/ru/feedback-branches" target="_blank">
  <span class="button">Письмо в поддержку</span>
</a>
||
|#

</div>

{% include [table-style-none](../_includes/table-style-none.md) %}

{% include [button-style](../_includes/yellow-button-styles.md) %}

{% include [border-style](../_includes/border-style.md) %}

{% include [cut-button-style](../_includes/cut-button-style.md) %}

{% include [footer](../_includes/footer.md) %}

{% include [list-reset](../_includes/list-reset.md) %}


[*информацию]: - статус;
- название;
- телефоны;
- сайты;
- вид деятельности;
- услуги;
- электронная почта;
- график работы;
- режим работы на дату.

[*с-помощью-XML‑файла]: - Данные о ваших филиалах будут всегда актуальны во всех сервисах и мобильных приложениях Яндекса. Ваши потенциальные клиенты смогут легко добраться до ближайшего филиала с помощью {% if tld == "ru" or tld == "uz" %}[Яндекс Карт](https://maps.yandex.ru/){% endif %}{% if tld == "kz" %}[Яндекс Карт](https://maps.yandex.kz/){% endif %}{% if tld == "com" %}[Яндекс Карт](https://maps.yandex.com/){% endif %}{% if tld == 'com.tr' %}[Яндекс Карт](https://maps.yandex.com.tr/){% endif %}{% if tld == "ru" or tld == "kz" or tld == "uz" %}, [Яндекс Навигатора](http://navigator.yandex.ru/), найти филиал в Поиске и других сервисах Яндекса{% endif %}.
- Вы можете полностью автоматизировать передачу данных о филиалах, настроив выгрузку данных из своей базы 1С, ERP (SAP, Axapta) или других систем.
- Через XML‑файл вы можете передавать полную информацию о филиалах, в том числе фотографии и дополнительные параметры.



<style type="text/css">
label:after { content: ""; display: block;}

.radio-group-2,
.radio-group-3,
.radio-group-4,
.radio-group-5,
.radio-group-6,
.radio-group-7,
.radio-group-8,
.radio-group-9 {
  margin-left: 15px;
  display: none;
  pointer-events: none;
  margin-bottom: 30px;
}

input:checked + label + .radio-group-3,
input:checked + label + .radio-group-4,
input:checked + label + .radio-group-2,
input:checked + label + .radio-group-5,
input:checked + label + .radio-group-6,
input:checked + label + .radio-group-7,
input:checked + label + .radio-group-8,
input:checked + label + .radio-group-9 {
  opacity: 1;
  display: block;
  pointer-events: all;
}

.form_radio_btn {
   display: block;
   margin-right: 10px;
}

.form_radio_btn input[type=radio] {
   display: none;
}

.form_radio_btn label {
   display: block;
   cursor: pointer;
   padding: 0px 15px;
   line-height: 34px;
   border: 1px solid #c4c4c4;
   border-radius: 6px;
   user-select: none;
   margin-bottom: 5px;
}

.form_radio_btn input[type=radio]:checked + label {
   background: #6a67f8;
   color: #ffffff
}

.radio-content {
   padding: 5px 0 10px 0;
   width: 100%;
   margin: 5px;
}

.content {
   margin: 10px 0 20px 0;
   width: 100%;
}

ol, ul {
   margin: 0;
   padding: 0;
   margin-left: 18px;
}

li {
   padding-top: 5px;
}

.info {
   background-color: #c4c4c4;
   border-radius: 10px;
   margin-top: 10px;
}

.content-info {
   padding: 20px;
}

details {
   display: inline-block;
}

summary {
   cursor: pointer;
}

desktop-img {
 display: none; /* Скрыть изображение на мобильных устройствах */
}

.container {
 display: flex;
 flex-wrap: wrap; /* Разрешаем перенос элементов на новую строку */
 justify-content: space-between; /* Равномерное распределение элементов по горизонтали */
 width: 100%;
}

.column {
 width: calc(50% - 10px); /* Ширина каждой колонки (минус расстояние между ними) */
 margin: 20px 0 10px; /* Расстояние между элементами */
}
.column ul {
   padding-left: 0;
  list-style-type: none;
}

@media screen and (min-width: 601px) {
   .form_radio_btn {
   width: 55%;
 }

 .desktop-img {
   display: block; /* Показать изображение на десктопах */
 }

 .mobile-img {
   display: none; /* Скрыть изображение на десктопах */
 }
}

@media (max-width: 601px) {
 .desktop-img {
   display: none; /* Скрыть изображение на десктопах */
 }

 .mobile-img {
   display: block; /* Показать изображение на десктопах */
 }

 .column {
   width: 100%; /* Перестраиваем в 1 колонку на мобильных */
 }
}
/*Стили для адаптивного баннера*/
   .banner {
      width: 100%;
      height: 92px;
      display: flex;
      flex-direction: row;
      justify-content: end;
      align-items: center;
      background-image: url(https://lead-assessors.s3.yandex.net/b902086a-4a70-464b-ba18-bf2a72966b15), url(https://lead-assessors.s3.yandex.net/700b8fb2-7e89-4fb3-ada2-238e5d8430ae);
      background-position: 20px center, right center;
      background-size: auto, contain;
      background-color: #F4F7FA;
      background-repeat: no-repeat;
      border-radius: 12px;
      margin-top: 90px;
   }
   .banner-title {
      width: 20px;
   }
   .banner-button {
      background: url(https://lead-assessors.s3.yandex.net/67139abe-983e-42ac-adae-e6737487ea0b) center center #FFF;
      border-radius: 14px;
      width: 197px;
      height: 44px;
      display: block;
      text-decoration: none;
      background-repeat: no-repeat;
   }
   @media (max-width: 601px) {
      .banner {
         flex-direction: column;
         height: 194px;
         background-image: url(https://lead-assessors.s3.yandex.net/b902086a-4a70-464b-ba18-bf2a72966b15), url(https://lead-assessors.s3.yandex.net/e2573994-bcce-4d13-af5c-b3a0668523e5);
         background-position: 20px 20px, bottom center;
         background-color: #F4F7FA;
         background-repeat: no-repeat;
         background-size: auto, 100% auto;
      }
      .banner-button {
         width: calc(100% - 40px);
         height: 44px;
      }
      .banner-title {
         margin-top: 20px;
   }
</style>

<h1>Служба поддержки компаний</h1>

<div class="content">
   <!--Если вы не нашли нужную информацию <a href="https://yandex.ru/support/business-priority/index.html" target="_blank">в&nbsp;разделах Справки</a>, напишите нам. Это&nbsp;эффективно: вы&nbsp;можете передать нам&nbsp;скриншоты, ссылки или&nbsp;видео. Так&nbsp;мы&nbsp;быстрее разберемся с&nbsp;проблемой и&nbsp;поможем вам.</div> 
   Воспользуйтесь нашим онлайн-помощником:
   <br>
   <a href="https://yandex.ru/chat?context=%7B%22entrypoint%22%3A%22%7B%5C%22page_name%5C%22%3A%5C%22help_form%5C%22%2C%5C%22a_pageurl%5C%22%3A%5C%22https%3A%2F%2Fyandex.ru%2Fsupport%2Fbusiness-priority%2F%5C%22%7D%22%7D#/user/5cb78286-a944-4c0f-bf33-b5c282eae053?utm-source=chat-in-help" target="_blank">
   <span style="line-height: 34px;display: inline-block;ext-align: center;font-size: 15px;font-family: var(--yc-text-body-font-family);padding: 0 15px;border-radius: 6px;color: #fff;background-color: #6a67f8; margin: 20px 0;">Онлайн-помощник</span>
   </a>
   <div class="content"> Или уточните, с&nbsp;чем связан ваш вопрос. Для этого выберите одну из категорий ниже, и мы ответим вам на почту:
   </div>-->

   <p>Напишите&nbsp;нам в&nbsp;чат, если не&nbsp;нашли ответ в&nbsp;<a href="https://yandex.ru/support/business-priority/index.html" target="_blank">Справке</a>. Вы&nbsp;можете приложить скриншоты или&nbsp;видео, чтобы ускорить помощь:
   <br>
   <a href="https://yandex.ru/chat?context=%7B%22entrypoint%22%3A%22%7B%5C%22page_name%5C%22%3A%5C%22help_form%5C%22%2C%5C%22a_pageurl%5C%22%3A%5C%22https%3A%2F%2Fyandex.ru%2Fsupport2%2Fbusiness-feedback%2Fru%2Ffeedback-company%5C%22%7D%22%7D#/user/5cb78286-a944-4c0f-bf33-b5c282eae053?utm-source=chat-in-help" target="_blank">
   <span style="line-height: 34px;display: inline-block;ext-align: center;font-size: 15px;font-family: var(--yc-text-body-font-family);padding: 0 15px;border-radius: 6px;color: #fff;background-color: #6a67f8; margin: 20px 0;">Чат с поддержкой</span></a>
   </p>
   <div class="content"> Или уточните ваш вопрос:
   </div>
</div>


<!---- Добавить в Карты ---->

<div class="form_radio_btn">
   <input type="radio" id="r-1" name="radio-group-3">
   <label for="r-1">Добавить компанию в&nbsp;Карты</label>
      <div class="radio-group-4">
         <div class="radio-content">
            Добавьте компанию в Карты через <a href="https://yandex.ru/sprav/add" target="_blank">форму</a>. Модерация занимает до двух дней.
         </div>
         <div class="radio-content">
            Отслеживайте статус на странице <a href="https://yandex.ru/sprav/requests/" target="_blank">Заявки</a>.
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-11" name="radio-group-4">
         <label for="m-11">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-12" name="radio-group-4">
         <label for="m-12">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <script src="https://forms.yandex.ru/_static/embed.js"></script><iframe src="https://forms.yandex.ru/surveys/13485450.308d0627b9787959fb16f18893a4fa631501e159/?iframe=1" frameborder="0" name="ya-form-13485450.308d0627b9787959fb16f18893a4fa631501e159" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Изменить статус ---->
      <input type="radio" id="b-2" name="radio-group-3">
      <label for="b-2">Изменить статус компании</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <b>Выберите тему:</b>
         </div>
         <!---- Компания закрылась/открылась ---->
         <input type="radio" id="m-21" name="radio-group-4">
         <label for="m-21">Закрылась/открылась</label>
         <div class="radio-group-5">
            <div class="radio-content">
               В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте <b>О компании</b> → <b>Данные и укажите статус</b>.
            </div>
            <div class="radio-content">
               Или найдите компанию в Картах и нажмите <b>Исправить неточность</b>. В открывшейся форме укажите верный статус. После проверки информация будет изменена.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-211" name="radio-group-5">
            <label for="m-211">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-212" name="radio-group-5">
            <label for="m-212">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe src="https://forms.yandex.ru/surveys/13485713.100b0162bd90561e96449c37be3bd2485451f82b/?iframe=1" frameborder="0" name="ya-form-13485713.100b0162bd90561e96449c37be3bd2485451f82b" width="650"></iframe>
               </div>
            </div>
         </div>
         <!---- Компания временно закрылась ---->
         <input type="radio" id="m-22" name="radio-group-4">
         <label for="m-22">Временно закрылась</label>
         <div class="radio-group-5">
            <div class="radio-content">
               В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте <b>О компании</b> → <b>Данные</b> и укажите статус.
            </div>
            <div class="radio-content">
               Или найдите компанию в Картах и нажмите Исправить неточность. В открывшейся форме укажите верный статус. После проверки информация будет изменена.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-221" name="radio-group-5">
            <label for="m-221">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-222" name="radio-group-5">
            <label for="m-222">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe src="https://forms.yandex.ru/surveys/13485713.100b0162bd90561e96449c37be3bd2485451f82b/?iframe=1" frameborder="0" name="ya-form-13485713.100b0162bd90561e96449c37be3bd2485451f82b" width="650"></iframe>
               </div>
            </div>
         </div>
         <!---- Компания давно закрыта ---->
         <input type="radio" id="m-23" name="radio-group-4">
         <label for="m-23">Давно закрыта, а в Картах есть</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Полностью удалить информацию о компании из Яндекс Карт нельзя. Если компания больше не работает, статус изменится на <b>Закрыта</b>.
            </div>
            <div class="radio-content">
               Мы считаем, что пользователям должна быть доступна и архивная информация. Поэтому карточки компаний, которые уже не работают, временно закрыты или переехали, продолжат отображаться в Картах.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-231" name="radio-group-5">
            <label for="m-231">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-232" name="radio-group-5">
            <label for="m-232">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe src="https://forms.yandex.ru/surveys/13485713.100b0162bd90561e96449c37be3bd2485451f82b/?iframe=1" frameborder="0" name="ya-form-13485713.100b0162bd90561e96449c37be3bd2485451f82b" width="650"></iframe>
               </div>
            </div>
         </div>
         <!---- Такой компании нет ---->
         <input type="radio" id="m-24" name="radio-group-4">
         <label for="m-24">Такой компании нет</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <ol>
                  <li>Найдите компанию в Картах и нажмите <b>Исправить неточность</b> → <b>Закрыто или не существует</b>.</li>
                  <li>В открывшейся форме укажите, что компания закрыта или отсутствует по этому адресу.</li>
               </ol>
            </div>
            <div class="radio-content">
               После проверки в карточке компании появится актуальный статус. Проверка занимает до двух недель.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-241" name="radio-group-5">
            <label for="m-241">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-242" name="radio-group-5">
            <label for="m-242">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe src="https://forms.yandex.ru/surveys/13485713.100b0162bd90561e96449c37be3bd2485451f82b/?iframe=1" frameborder="0" name="ya-form-13485713.100b0162bd90561e96449c37be3bd2485451f82b" width="650"></iframe>
               </div>
            </div>
         </div>
      </div>
      <!---- Изменить телефон ---->
      <input type="radio" id="b-3" name="radio-group-3">
      <label for="b-3">Изменить телефон</label>
      <div class="radio-group-4">
         <div class="radio-content">
            В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> → <b>Номера телефонов</b> укажите актуальные контакты.
         </div>
         <div class="radio-content">
            Или найдите компанию в Картах и нажмите Исправить неточность. В открывшейся форме укажите верный телефон. Этот телефон должен быть указан на сайте или в социальных сетях компании.
         </div>
         <div class="radio-content">
            Информация обновится после проверки.
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-31" name="radio-group-4">
         <label for="m-31">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-32" name="radio-group-4">
         <label for="m-32">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13485716.d3c81ebfc8810d62997fe94ae9afb58ec7565990/?iframe=1" frameborder="0" name="ya-form-13485716.d3c81ebfc8810d62997fe94ae9afb58ec7565990" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Изменить сайт/соц.сеть ---->
      <input type="radio" id="b-4" name="radio-group-3">
      <label for="b-4">Изменить сайт или социальную сеть</label>
      <div class="radio-group-4">
         <div class="radio-content">
            В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> → <b>Контакты</b> укажите ссылку на сайт, социальную сеть.
         </div>
         <div class="radio-content">
            Или найдите компанию в Картах и нажмите ссылку <b>Исправить неточность</b>. В открывшейся форме укажите верные данные.
         </div>
         <div class="radio-content">
            Информация обновится после проверки.
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-41" name="radio-group-4">
         <label for="m-41">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-42" name="radio-group-4">
         <label for="m-42">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13486366.26917a66ef6dc86feb6534a9a4e9d6196eb9d763/?iframe=1" frameborder="0" name="ya-form-13486366.26917a66ef6dc86feb6534a9a4e9d6196eb9d763" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Изменить название ---->
      <input type="radio" id="b-5" name="radio-group-3">
      <label for="b-5">Изменить название компании</label>
      <div class="radio-group-4">
         <div class="radio-content">
            В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> → <b>Подробная информация</b> укажите название компании.
         </div>
         <div class="radio-content">
            Или найдите компанию в Картах и нажмите ссылку <b>Исправить неточность</b>. В открывшейся форме укажите верные данные. Название компании в Картах должно соответствовать <a href="https://yandex.ru/support/business-priority/add-company/info-terms.html#rules-of-desing__name" target="_blank">правилам Яндекс Бизнеса</a>.
         </div>
         <div class="radio-content">
            Информация обновится после проверки в течение трех дней.
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-51" name="radio-group-4">
         <label for="m-51">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-52" name="radio-group-4">
         <label for="m-52">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13485715.a12010876b86df545385c2841c11197b0d070f42/?iframe=1" frameborder="0" name="ya-form-13485715.a12010876b86df545385c2841c11197b0d070f42" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Изменить адрес/вход ---->
      <input type="radio" id="b-6" name="radio-group-3">
      <label for="b-6">Изменить адрес, вход</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <b>Компания переезжает</b>
            <ol>
               <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите компанию и нажмите <b>О компании</b> → <b>Данные</b>.</li>
               <li>Выберите <b>Основные</b> → <b>Адрес</b>.</li>
               <li>Измените адрес компании или передвиньте метку на карте в нужное место.</li>
               <li>Проверьте новый адрес, а затем нажмите <b>Переезжаю</b>. Если фото и отзывы нужно оставить по прежнему адресу, уберите отметки.</li>
               <li>Нажмите <b>Сохранить данные</b>.</li>
            </ol>
         </div>
         <div class="content-info">
            Информация из раздела <b>Статистика</b> не переносится при переезде.
         </div>
         <div class="radio-content">
            Карточка компании с новым адресом будет создана автоматически в течение трех дней. В Картах компания по старому адресу опубликуется со статусом <b>Переехала</b>. Изменить информацию в старом профиле будет уже нельзя.
         </div>
         <div class="radio-content">
            <b>Добавить или удалить вход</b>
            <ol>
               <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите компанию и нажмите <b>О компании</b> → <b>Данные</b>.</li>
               <li>Выберите <b>Основные</b> → <b>Адрес</b>.</li>
               <li>Нажмите <b>Редактировать входы</b>.</li>
               <li>Нажмите <b>Добавить вход</b> или <b>Удалить вход</b>, чтобы расставить метки в нужных местах на здании.</li>
               <li>Нажмите <b>Сохранить данные</b>.</li>
            </ol>
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-61" name="radio-group-4">
         <label for="m-61">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-62" name="radio-group-4">
         <label for="m-62">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13485717.0c53dd6a28ef50cae68c7e59573b8f985c589440/?iframe=1" frameborder="0" name="ya-form-13485717.0c53dd6a28ef50cae68c7e59573b8f985c589440" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Компания уже есть ---->
      <input type="radio" id="b-7" name="radio-group-3">
      <label for="b-7">Такая компания уже есть</label>
      <div class="radio-group-4">
         <div class="radio-content">
	      <iframe src=" https://forms.yandex.ru/surveys/13485713.100b0162bd90561e96449c37be3bd2485451f82b/?iframe=1 " frameborder="0" name="ya-form-13485713.100b0162bd90561e96449c37be3bd2485451f82b" width="650"></iframe>
         </div>
      </div>
      <!---- Получить доступ к профилю ---->
      <input type="radio" id="b-8" name="radio-group-3">
      <label for="b-8">Подтвердить права и получить доступ к профилю</label>
      <div class="radio-group-4">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53/?iframe=1" frameborder="0" name="ya-form-13486251.f4acbe82566619cef990d6d4f7914aaa0739fd53" width="650"></iframe>
            </div>
       </div>
      <!---- Вопрос по онлайн-компании ---->
      <input type="radio" id="b-9" name="radio-group-3">
      <label for="b-9">Вопрос по онлайн-компании</label>
      <div class="radio-group-4">
         <div class="radio-content">
            Онлайн-компания — компания без фактического адреса.
         </div>
         <div class="radio-content">
            <b>Выберите тему:</b>
         </div>
         <!---- Появился офис ---->
         <input type="radio" id="m-91" name="radio-group-4">
         <label for="m-91">Появился офис. Как добавиться в Карты?</label>
         <div class="radio-group-5">
            <div class="radio-content">
               В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите нужную компанию и нажмите <b>Вы появитесь в Картах</b>. Заполните заявку. После проверки тип компании будет изменен.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-911" name="radio-group-5">
            <label for="m-911">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-912" name="radio-group-5">
            <label for="m-912">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10012012/?lang=ru&iframe=1&answer_short_text_66246=[Профиль+-+Онлайн-компания]+Появился+офис,+добавиться+в+Карты" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Отображается неверный адрес ---->
         <input type="radio" id="m-92" name="radio-group-4">
         <label for="m-92">Отображается неверный адрес</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Мы показываем только те регионы, которые вы указали в профиле компании. Список можно посмотреть в поле <b>Оказывает услуги в</b>. Адрес вычисляется автоматически. Это центр области, которая указана в профиле.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-921" name="radio-group-5">
            <label for="m-921">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-922" name="radio-group-5">
            <label for="m-922">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10012012/?lang=ru&iframe=1&answer_short_text_66246=[Профиль+-+Онлайн-компания]+Неверный+адрес" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
      </div>
      <!---- Отзывы ---->
      <input type="radio" id="b-10" name="radio-group-3">
      <label for="b-10">Отзывы</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <b>Выберите тему:</b>
         </div>
         <!---- Жалоба на отзыв ---->
         <input type="radio" id="m-101" name="radio-group-4">
         <label for="m-101">Жалоба на отзыв</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Мы не удаляем отзывы, которые отражают субъективное мнение пользователя и соответствуют <a href="https://yandex.ru/support/reviews/rules.html" target="_blank">правилам публикации</a>. Вы можете <a href="https://yandex.ru/support/business-priority/manage/reviews.html#reviews__reply" target="_blank">ответить</a> на отзыв пользователя и выяснить причину.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-1011" name="radio-group-5">
            <label for="m-1011">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-1012" name="radio-group-5">
            <label for="m-1012">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10031622.abe3961e45af496269f9c47c99f1a095187c3452/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Отзыв отклонен/не опубликован ---->
         <input type="radio" id="m-102" name="radio-group-4">
         <label for="m-102">Отзыв отклонен или не опубликован</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отзыва нет в профиле компании, если:
               <ul>
                  <li>Он на модерации. Отзыв появится в течение двух дней.</li>
                  <li>Отзыв не соответствует <a href="https://yandex.ru/support/reviews/rules.html" target="_blank">правилам публикации</a>.</li>
                  <li>Отзыв удален, потому что он был похож на накрученный. Подробнее о накрутке — в статье <a href="https://yandex.ru/support/reviews/rules.html#rule" target="_blank">Правила публикации</a>.</li>
               </ul>
            </div>
            <div class="radio-content">
               Полезные ссылки:
               <ul>
                  <li><a href="https://business.yandex/klienty/kak-yandeks-proveryaet-otzyvy-v-kartah-i-poiske/?utm_source=support&utm_medium=organic&utm_campaign=supportresponse" target="_blank">Как Яндекс проверяет отзывы в Картах и Поиске</a>.</li>
                  <li><a href="https://business.yandex.ru/reviewspage?utm_source=support&utm_medium=organic&utm_campaign=supportresponse" target="_blank">Как работать с отзывами и влиять на рейтинг</a>.</li>
               </ul>
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-1021" name="radio-group-5">
            <label for="m-1021">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-1022" name="radio-group-5">
            <label for="m-1022">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015059/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Сортировка отзывов ---->
         <input type="radio" id="m-103" name="radio-group-4">
         <label for="m-103">Как сортируются отзывы</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отзывы показываются справа от результатов поиска и сортируются по полезности и популярности среди пользователей. В этом помогают алгоритмы ранжирования и результаты опросов о пользе отзывов.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-1031" name="radio-group-5">
            <label for="m-1031">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-1032" name="radio-group-5">
            <label for="m-1032">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10031624.90787d9cadae29bcf9d3c0b7c4ded8bfbe351a23/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
      </div>
      <!---- Рейтинг ---->
      <input type="radio" id="b-11" name="radio-group-3">
      <label for="b-11">Рейтинг</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <b>Выберите тему:</b>
         </div>
         <!---- Рейтинг пропал ---->
         <input type="radio" id="m-111" name="radio-group-4">
         <label for="m-111">Рейтинг пропал</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Мы скрываем рейтинг для компаний и объектов, если для пользователей он не имеет значение. Узнать подробности о таких местах или поделиться информацией о них вы можете в разделе <b>Отзывы</b>.
            </div>
            <div class="radio-content">
               <details>
                  <summary>Категории компаний без рейтинга</summary>
                            <ul>
                              <li>
                                Аварийная служба
                              </li>
                              <li>
                                Автомат для приёма монет
                              </li>
                              <li>
                                Автомобильная парковка
                              </li>
                              <li>
                                Аграрная инфраструктура
                              </li>
                              <li>
                                Администрация
                              </li>
                              <li>
                                Аквариум
                              </li>
                              <li>
                                Анимация
                              </li>
                              <li>
                                Арбитражный суд
                              </li>
                              <li>
                                Арт-объект
                              </li>
                              <li>
                                Ассоциации и промышленные союзы
                              </li>
                              <li>
                                Аудитория
                              </li>
                              <li>
                                АЭС, ГЭС, ТЭС
                              </li>
                              <li>
                                Багажный сервис
                              </li>
                              <li>
                                База гидросамолётов
                              </li>
                              <li>
                                Банкомат
                              </li>
                              <li>
                                Бельевая площадка
                              </li>
                              <li>
                                Беседка
                              </li>
                              <li>
                                Благотворительный фонд
                              </li>
                              <li>
                                Блок стадиона
                              </li>
                              <li>
                                БТИ
                              </li>
                              <li>
                                Бюро пропусков, пост охраны
                              </li>
                              <li>
                                Велопарковка
                              </li>
                              <li>
                                Вертолётная площадка
                              </li>
                              <li>
                                Водоканал, водное хозяйство
                              </li>
                              <li>
                                Водоразборная колонка
                              </li>
                              <li>
                                Военкомат
                              </li>
                              <li>
                                Военный комендант
                              </li>
                              <li>
                                Вольер животных
                              </li>
                              <li>
                                Вольер птиц
                              </li>
                              <li>
                                Воскресная школа
                              </li>
                              <li>
                                Въездной знак
                              </li>
                              <li>
                                Выдача негабаритного багажа
                              </li>
                              <li>
                                Выход из железнодорожного вокзала или станции
                              </li>
                              <li>
                                Выход со станции скоростного транспорта
                              </li>
                              <li>
                                Гардероб
                              </li>
                              <li>
                                Городская телефонная сеть
                              </li>
                              <li>
                                Госавтоинспекция
                              </li>
                              <li>
                                Государственная служба безопасности
                              </li>
                              <li>
                                Гражданская оборона
                              </li>
                              <li>
                                Дежурный по вокзалу
                              </li>
                              <li>
                                Декоративный объект, доска почёта
                              </li>
                              <li>
                                Детская площадка
                              </li>
                              <li>
                                Детская скорая помощь
                              </li>
                              <li>
                                Душ
                              </li>
                              <li>
                                Железнодорожная станция
                              </li>
                              <li>
                                Железнодорожный вокзал
                              </li>
                              <li>
                                Жилищный отдел
                              </li>
                              <li>
                                Защита прав потребителя
                              </li>
                              <li>
                                Зона таможенного контроля
                              </li>
                              <li>
                                Избирательные участки
                              </li>
                              <li>
                                Иммиграционный офис
                              </li>
                              <li>
                                Инженерная инфраструктура
                              </li>
                              <li>
                                Инспекция
                              </li>
                              <li>
                                Инфостойка
                              </li>
                              <li>
                                Инфраструктура отдыха
                              </li>
                              <li>
                                Исправительное учреждение
                              </li>
                              <li>
                                Казначейство
                              </li>
                              <li>
                                Камера хранения
                              </li>
                              <li>
                                Касса
                              </li>
                              <li>
                                Кладбище
                              </li>
                              <li>
                                Ключ, ручей
                              </li>
                              <li>
                                Коллекторское агентство
                              </li>
                              <li>
                                Колодец
                              </li>
                              <li>
                                Коммунальная служба
                              </li>
                              <li>
                                Комната матери и ребенка
                              </li>
                              <li>
                                Конструкторское бюро
                              </li>
                              <li>
                                Космодром
                              </li>
                              <li>
                                КПП
                              </li>
                              <li>
                                Крематорий
                              </li>
                              <li>
                                Лаборатория ветеринарно-санитарной экспертизы
                              </li>
                              <li>
                                Ледовая переправа
                              </li>
                              <li>
                                Лента выдача багажа
                              </li>
                              <li>
                                Лесничество, лесхоз
                              </li>
                              <li>
                                Лесной массив
                              </li>
                              <li>
                                Лесопарк
                              </li>
                              <li>
                                Лицензирование
                              </li>
                              <li>
                                Медико-социальная экспертиза
                              </li>
                              <li>
                                Международная организация
                              </li>
                              <li>
                                Место для курения
                              </li>
                              <li>
                                Министерства, ведомства, государственные службы
                              </li>
                              <li>
                                Мировой судья
                              </li>
                              <li>
                                Могилы известных людей
                              </li>
                              <li>
                                Молочная кухня
                              </li>
                              <li>
                                Морг
                              </li>
                              <li>
                                Морские и речные вокзалы
                              </li>
                              <li>
                                МРЭО
                              </li>
                              <li>
                                Мусорная площадка
                              </li>
                              <li>
                                Мухтарлык
                              </li>
                              <li>
                                МФЦ
                              </li>
                              <li>
                                Налоговая инспекция
                              </li>
                              <li>
                                Научно-производственная организация
                              </li>
                              <li>
                                Непассажирская станция
                              </li>
                              <li>
                                НИИ
                              </li>
                              <li>
                                Ночлежный дом
                              </li>
                              <li>
                                Общежитие
                              </li>
                              <li>
                                Общественная группа
                              </li>
                              <li>
                                Общественная организация
                              </li>
                              <li>
                                Общественный пункт охраны порядка
                              </li>
                              <li>
                                Общественный фонд
                              </li>
                              <li>
                                Озеро
                              </li>
                              <li>
                                Оператор спутниковой связи
                              </li>
                              <li>
                                Органы государственного надзора
                              </li>
                              <li>
                                Остановка беспилотника
                              </li>
                              <li>
                                Остановка маршрутного такси
                              </li>
                              <li>
                                Остановка общественного транспорта
                              </li>
                              <li>
                                Остановка трамвая
                              </li>
                              <li>
                                Отделение милиции
                              </li>
                              <li>
                                Отделение полиции
                              </li>
                              <li>
                                Офис интернет-магазина
                              </li>
                              <li>
                                Офис компании
                              </li>
                              <li>
                                Офис управления
                              </li>
                              <li>
                                Парковка тележек
                              </li>
                              <li>
                                Парковочная зона
                              </li>
                              <li>
                                Паспортные и миграционные службы
                              </li>
                              <li>
                                Паспортный контроль
                              </li>
                              <li>
                                Патентные услуги
                              </li>
                              <li>
                                Пенсионный фонд
                              </li>
                              <li>
                                Питьевые галереи и источники
                              </li>
                              <li>
                                Платёжный терминал
                              </li>
                              <li>
                                Пляж
                              </li>
                              <li>
                                Пограничный переход
                              </li>
                              <li>
                                Пожарные части и службы
                              </li>
                              <li>
                                Полигон ТБО
                              </li>
                              <li>
                                Политическая партия
                              </li>
                              <li>
                                Посольство, консульство
                              </li>
                              <li>
                                Пост ДПС
                              </li>
                              <li>
                                Потребительская кооперация
                              </li>
                              <li>
                                Почтовое отделение
                              </li>
                              <li>
                                Предприятие связи
                              </li>
                              <li>
                                Приём негабаритного багажа
                              </li>
                              <li>
                                Примерочная
                              </li>
                              <li>
                                Пристань
                              </li>
                              <li>
                                Прокат инвалидных колясок
                              </li>
                              <li>
                                Прокуратура
                              </li>
                              <li>
                                Промышленная инфраструктура
                              </li>
                              <li>
                                Профсоюз
                              </li>
                              <li>
                                Прочие кассы
                              </li>
                              <li>
                                Прощальный зал
                              </li>
                              <li>
                                Публичный центр правовой информации
                              </li>
                              <li>
                                Пункт взимания платы
                              </li>
                              <li>
                                Пункт выдачи страховых полисов
                              </li>
                              <li>
                                Пункт декларирования валюты
                              </li>
                              <li>
                                Пункт приёма ёлок
                              </li>
                              <li>
                                Пункт сбора населения во время чрезвычайных ситуаций
                              </li>
                              <li>
                                Пункт сбора помощи
                              </li>
                              <li>
                                Пункт экстренной связи
                              </li>
                              <li>
                                Радиационный контроль
                              </li>
                              <li>
                                Раздельный сбор отходов
                              </li>
                              <li>
                                Регистрационная палата
                              </li>
                              <li>
                                Религиозное объединение
                              </li>
                              <li>
                                Розетки для зарядки
                              </li>
                              <li>
                                Садоводческие товарищества и общества
                              </li>
                              <li>
                                Саморегулируемая организация
                              </li>
                              <li>
                                Санитарно-эпидемиологическая служба
                              </li>
                              <li>
                                Сервисный центр МВД Украины
                              </li>
                              <li>
                                Сертификация продукции и услуг
                              </li>
                              <li>
                                Скамейка
                              </li>
                              <li>
                                Скорая медицинская помощь
                              </li>
                              <li>
                                Следственный комитет
                              </li>
                              <li>
                                Служба газового хозяйства
                              </li>
                              <li>
                                Служба спасения
                              </li>
                              <li>
                                Собачья площадка
                              </li>
                              <li>
                                Совет депутатов
                              </li>
                              <li>
                                Социальная реабилитация
                              </li>
                              <li>
                                Социальная служба
                              </li>
                              <li>
                                Социологические исследования
                              </li>
                              <li>
                                Спортивная касса
                              </li>
                              <li>
                                Спортивное объединение
                              </li>
                              <li>
                                Спортплощадка, воркаут
                              </li>
                              <li>
                                Стандартизация и метрология
                              </li>
                              <li>
                                Станция метро
                              </li>
                              <li>
                                Станция скоростного городского транспорта
                              </li>
                              <li>
                                Статистическая организация
                              </li>
                              <li>
                                Стойка вызова экстренных служб
                              </li>
                              <li>
                                Стойка регистрации
                              </li>
                              <li>
                                Стойка такси
                              </li>
                              <li>
                                Стоянка такси
                              </li>
                              <li>
                                Стрит-арт
                              </li>
                              <li>
                                Строительная экспертиза и технадзор
                              </li>
                              <li>
                                Строительство и ремонт дорог
                              </li>
                              <li>
                                Суд
                              </li>
                              <li>
                                Судебно-медицинская экспертиза
                              </li>
                              <li>
                                Судебные приставы
                              </li>
                              <li>
                                Сцена
                              </li>
                              <li>
                                Таксофон
                              </li>
                              <li>
                                Таможенный склад
                              </li>
                              <li>
                                Таможня
                              </li>
                              <li>
                                Танцплощадка
                              </li>
                              <li>
                                Телекоммуникационная компания
                              </li>
                              <li>
                                Теплоснабжение
                              </li>
                              <li>
                                Терминал аэропорта
                              </li>
                              <li>
                                Торговая точка
                              </li>
                              <li>
                                Торгово-промышленная палата
                              </li>
                              <li>
                                Трамвайная станция
                              </li>
                              <li>
                                Транспортная инфраструктура
                              </li>
                              <li>
                                Транспортная касса
                              </li>
                              <li>
                                Трибуна
                              </li>
                              <li>
                                Троллейбусная станция
                              </li>
                              <li>
                                ТСЖ, правление СНТ
                              </li>
                              <li>
                                Туалет
                              </li>
                              <li>
                                Туалет для инвалидов
                              </li>
                              <li>
                                Умные устройства Яндекса
                              </li>
                              <li>
                                Управление водными путями и их обслуживание
                              </li>
                              <li>
                                Управление воздушным транспортом и его обслуживание
                              </li>
                              <li>
                                Управление городским транспортом и его обслуживание
                              </li>
                              <li>
                                Управление железными дорогами и их обслуживание
                              </li>
                              <li>
                                Управление исполнения наказаний
                              </li>
                              <li>
                                Управление образованием
                              </li>
                              <li>
                                Фестиваль
                              </li>
                              <li>
                                Фитосанитарный, ветеринарный контроль
                              </li>
                              <li>
                                Фонд социального страхования
                              </li>
                              <li>
                                Центр занятости
                              </li>
                              <li>
                                Центр Яндекс Такси
                              </li>
                              <li>
                                Шлюз
                              </li>
                              <li>
                                Шоу-рум
                              </li>
                              <li>
                                Штрафстоянка
                              </li>
                              <li>
                                Экологическая организация
                              </li>
                              <li>
                                Экспертиза
                              </li>
                              <li>
                                Экстренная социальная психологическая помощь
                              </li>
                              <li>
                                Элеватор
                              </li>
                              <li>
                                Энергоснабжение
                              </li>
                            </ul>
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-1111" name="radio-group-5">
            <label for="m-1111">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-1112" name="radio-group-5">
            <label for="m-1112">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10031624.90787d9cadae29bcf9d3c0b7c4ded8bfbe351a23/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Рейтинг занижен ---->
         <input type="radio" id="m-112" name="radio-group-4">
         <label for="m-112">Рейтинг занижен</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Рейтинг компании — это агрегированная оценка качества работы и популярности компании по мнению пользователей Яндекса. Он не равен среднему арифметическому значению всех оценок. Алгоритм учитывает влияние многих факторов: от количества оценок до степени доверия к отзыву.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-1121" name="radio-group-5">
            <label for="m-1121">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-1122" name="radio-group-5">
            <label for="m-1122">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10031624.90787d9cadae29bcf9d3c0b7c4ded8bfbe351a23/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Нет рейтинга ---->
         <input type="radio" id="m-113" name="radio-group-4">
         <label for="m-113">У компании нет рейтинга</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Рейтинг начинает отображаться, когда компания получает достаточное количество оценок. Чтобы он появился, оценок должно быть не меньше пяти.
            </div>
            <div class="radio-content">
               Полезные ссылки:
               <ul>
                  <li><a href="https://business.yandex/klienty/kak-rejting-kompanii-v-poiske-i-kartah-vliyaet-na-vash-biznes/" target="_blank">Как рейтинг компании в Поиске и Картах влияет на ваш бизнес</a>.</li>
                  <li><a href="https://business.yandex.ru/reviewspage?utm_source=support&utm_medium=organic&utm_campaign=supportresponse" target="_blank">Как работать с отзывами и влиять на рейтинг</a>.</li>
               </ul>
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="m-1131" name="radio-group-5">
            <label for="m-1131">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="m-1132" name="radio-group-5">
            <label for="m-1132">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10031624.90787d9cadae29bcf9d3c0b7c4ded8bfbe351a23/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
      </div>
      <!---- Не получил знак "Хорошее место" ---->
      <input type="radio" id="b-12" name="radio-group-3">
      <label for="b-12">Не получил знак «Хорошее место»</label>
      <div class="radio-group-4">
         <div class="radio-content">
            Чтобы получить значок «Хорошее место», нужно:
            <ul>
               <li>относиться к <a href="https://yandex.ru/support/business-priority/manage/stiker.html#stiker__categories2021" target="_blank">категории, которая участвует в проекте</a>;</li>
               <li>иметь рейтинг в Яндексе 4,5 и выше;</li>
               <li>иметь знак <a href="https://yandex.ru/support/business-priority/manage/verified-owner.html" target="_blank">«Информация подтверждена владельцем»</a>.</li>
            </ul>
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-121" name="radio-group-4">
         <label for="m-121">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-122" name="radio-group-4">
         <label for="m-122">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/13485709.01e67750c4c748c375da0829bd931e5d7eb16383/?lang=ru&iframe=1" id="registration" loading="lazy" ></iframe>
            </div>
         </div>
      </div>
      <!---- Добавить фотографии ---->
      <input type="radio" id="b-13" name="radio-group-3">
      <label for="b-13">Изменить фото, видео или логотип</label>
      <div class="radio-group-4">
         <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13485720.2d1693cf829e33f1f1b5ff03afbf6bee08f305c9/?iframe=1" frameborder="0" name="ya-form-13485720.2d1693cf829e33f1f1b5ff03afbf6bee08f305c9" width="650"></iframe>
            </div>
      </div>
      <!---- "Информация подтверждена владельцем" ---->
      <input type="radio" id="b-14" name="radio-group-3">
      <label for="b-14">Знак «Информация подтверждена владельцем»</label>
      <div class="radio-group-4">
         <div class="radio-content">
            В левом верхнем углу Личного кабинета найдите блок‑индикатор заполнения и нажмите. Появится окно с информацией о заполненности профиля.
         </div>
         <div class="radio-content">
            Заполните или обновите все обязательные блоки:
            <ul>
               <li>Время работы.</li>
               <li>Ссылка на сайт. Если сайта нет, достаточно указать ссылку на социальную сеть.</li>
               <li>Телефон.</li>
               <li>Фото, видео.</li>
               <li>Прайс‑лист. Укажите как минимум три позиции с ценой.</li>
            </ul>
         </div>
         <div class="radio-content">
         Знак появится в течение 1‑2 дней после заполнения или обновления профиля.
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-141" name="radio-group-4">
         <label for="m-141">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-142" name="radio-group-4">
         <label for="m-142">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/13486200.5d39b4609e5e31e79e606d8740ed8cd420245b3d/?iframe=1" frameborder="0" name="ya-form-13486200.5d39b4609e5e31e79e606d8740ed8cd420245b3d" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Не найти компанию через поиск ---->
      <input type="radio" id="b-15" name="radio-group-3">
      <label for="b-15">Не могу найти компанию через поиск в Картах</label>
      <div class="radio-group-4">
            <div class="radio-content">
               <iframe src="https://forms.yandex.ru/surveys/10015062/?iframe=1" frameborder="0" name="ya-form-10015062" width="650"></iframe>
            </div>
      </div>
      <!---- Добавить "Товары" ---->
      <input type="radio" id="b-16" name="radio-group-3">
      <label for="b-16">Как добавить товары</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <ol>
               <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> нажмите <b>О компании</b> → <b>Товары и услуги</b>.</li>
               <li>Нажмите <b>Новый товар</b>.</li>
               <li>
                  Заполните информацию о товаре или услуге (далее обязательные поля отмечены звездочкой):
                  <ul>
                     <li><b>Фотография</b></li>
                     <li><b>Название</b></li>
                     <li><b>Категория</b></li>
                     <li><b>Цена</b></li>
                     <li><b>Описание</b></li>
                     <li><b>Популярный товар</b></li>
                     <li><b>Нет в наличии</b></li>
                  </ul>
               </li>
               <li>Нажмите <b>Сохранить</b>.</li>
            </ol>
         </div>
         <div class="radio-content">
            В любой момент вы можете отредактировать информацию в прайс-листе. После размещения информации данные появятся в карточке компании на Яндексе и в Картах в течение суток.
         </div>
         <div class="radio-content">
            Также товары можно добавить через XLS/XLSX-файл и YML-файл. Подробнее см. в статье <a href="https://yandex.ru/support/business-priority/manage/price-list.html" target="_blank">Прайс-лист компании</a>.
         </div>
         <div class="radio-content">
            Удалось найти ответ?
         </div>
         <input type="radio" id="m-161" name="radio-group-4">
         <label for="m-161">Да. Всё получилось</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Отлично!
            </div>
         </div>
         <input type="radio" id="m-162" name="radio-group-4">
         <label for="m-162">Мне нужна помощь</label>
         <div class="radio-group-5">
            <div class="radio-content">
              <iframe src="https://forms.yandex.ru/surveys/13485724.a1310d38f50da2df17deb93bfdb4b514c5679847/?iframe=1" frameborder="0" name="ya-form-13485724.a1310d38f50da2df17deb93bfdb4b514c5679847" width="650"></iframe>
            </div>
         </div>
      </div>
      <!---- Другое ---->
      <input type="radio" id="b-17" name="radio-group-3">
      <label for="b-17">Другое</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <iframe src="https://forms.yandex.ru/surveys/13485723.5a3c3e8b1a45226ec566f3ff6ae85e6f4082f770/?iframe=1" frameborder="0" name="ya-form-13485723.5a3c3e8b1a45226ec566f3ff6ae85e6f4082f770" width="650"></iframe>
         </div>
      </div>
   </div>
</div>


<!-------------------------->

<div style="clear: both;"></div>

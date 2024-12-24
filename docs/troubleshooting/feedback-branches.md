
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

<h1>Служба поддержки сетей</h1>

<div class="content">
   Напишите&nbsp;нам, если не&nbsp;нашли ответ в&nbsp;<a href="https://yandex.ru/support/business-priority/index.html" target="_blank">Справке</a>. Вы&nbsp;можете приложить скриншоты или&nbsp;видео, чтобы ускорить помощь. Уточните ваш&nbsp;вопрос:
</div>

<!---- СЕТИ ---->

<div class="form_radio_btn">
   <input type="radio" id="r-3" name="radio-group-2" checked="checked">
   <label for="r-3">У меня уже есть сеть в Яндекс Бизнесе, а данные обновляются через файл.</label>
    <div class="radio-group-3">
         <div class="radio-content">
         </div>
      <!---- Да ---->
      <input type="radio" id="c-1" name="radio-group-3">
      <label for="c-1">Да</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <b>Выберите тему:</b>
         </div>
         <!---- Изменить информацию ---->
         <input type="radio" id="n-11" name="radio-group-4">
         <label for="n-11">Изменить информацию</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Внесите правки вручную в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>, либо через <a href="https://yandex.ru/support/business-priority/branches/xml-feed-sprav.html" target="_blank">XML-файл</a> или <a href="https://yandex.ru/support/business-priority/branches/csv-feed-sprav.html" target="_blank">CSV-файл</a>. Используйте только один метод внесения изменений.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-111" name="radio-group-5">
            <label for="n-111">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-112" name="radio-group-5">
            <label for="n-112">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Через+файл]+Изменить+информацию" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Добавить филиал ---->
         <input type="radio" id="n-12" name="radio-group-4">
         <label for="n-12">Добавить филиал в сеть</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Добавьте информацию о филиале в <a href="https://yandex.ru/support/business-priority/branches/xml-feed-sprav.html" target="_blank">XML-файл</a> или <a href="https://yandex.ru/support/business-priority/branches/csv-feed-sprav.html" target="_blank">CSV-файл</a>, а затем обновите информацию на странице сети. Филиал добавится при ближайшей синхронизации.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-121" name="radio-group-5">
            <label for="n-121">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-122" name="radio-group-5">
            <label for="n-122">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл]+Добавить+филиал" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Удалить/закрыть филиал ---->
         <input type="radio" id="n-13" name="radio-group-4">
         <label for="n-13">Удалить или закрыть филиал</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Добавьте или удалите информацию о нужном филиале в <a href="https://yandex.ru/support/business-priority/branches/xml-feed-sprav.html" target="_blank">XML-файле</a> или <a href="https://yandex.ru/support/business-priority/branches/csv-feed-sprav.html" target="_blank">CSV-файле</a>.
            </div>
            <div class="radio-content">
               Чтобы оперативно обновить данные, внесите правки в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>. После этого не забудьте добавить их в XML/CSV-файл. Если этого не сделать, при ближайшей синхронизации в профиль попадут неверные данные из файла, а правки, которые вы внесли вручную в Личном кабинете, пропадут. Данные в файле имеют больший приоритет, чем данные в Личном кабинете.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-131" name="radio-group-5">
            <label for="n-131">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-132" name="radio-group-5">
            <label for="n-132">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Через+файл]+Удалить,+закрыть+филиал" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Компания уже есть ---->
         <input type="radio" id="n-14" name="radio-group-4">
         <label for="n-14">Такая компания уже есть</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл]+Удалить+дубль" id="registration" loading="lazy" ></iframe>
            </div>
         </div>
         <!---- Подтверждение/передача прав доступа ---->
         <input type="radio" id="n-15" name="radio-group-4">
         <label for="n-15">Подтверждение и передача прав доступа</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <b>Уточните ваш вопрос:</b>
            </div>
            <!---- Подтвердить права на сеть ---->
            <input type="radio" id="c-151" name="radio-group-5">
            <label for="c-151">Как подтвердить права на сеть</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <ol>
                     <li>На <a href="https://yandex.ru/sprav/search" target="_blank">странице поиска</a> ведите название и нажмите <b>Найти</b>.</li>
                     <li>Выберите сеть и нажмите <b>Это моя сеть</b>.</li>
                     <li>В появившемся окне выберите номер телефона, с помощью которого хотите подтвердить права.</li>
                  </ol>
               </div>
               <div class="radio-content">
                  Получите код и введите его. Код можно ввести позже на странице <a href="https://yandex.ru/sprav/requests/confirmation" target="_blank">Мои заявки</a>.
               </div>
               <div class="radio-content">
                  Компания появится в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>.
               </div>
               <div class="radio-content">
                  <b>Что-то пошло не так:</b>
               </div>
               <!---- Не пришёл код ---->
               <input type="radio" id="c-1511" name="radio-group-6">
               <label for="c-1511">Не пришло SMS с кодом</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Вы можете запросить код для подтверждения еще раз через сутки. Откройте <b>Мои заявки</b> → <b>На подтверждение</b> и нажмите <b>Получить код</b>.
                  </div>
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="m-15111" name="radio-group-7">
                  <label for="m-15111">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="m-15112" name="radio-group-7">
                  <label for="m-15112">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл+-+Подтвердить+права+на+сеть]+Не+пришло+SMS" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Не перезвонили ---->
               <input type="radio" id="c-1512" name="radio-group-6">
               <label for="c-1512">Мне не перезвонили</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="m-15121" name="radio-group-7">
                  <label for="m-15121">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="m-15122" name="radio-group-7">
                  <label for="m-15122">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл+-+Подтвердить+права+на+сеть]+Не+позвонили" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- "Введен неверный код" ---->
               <input type="radio" id="c-1513" name="radio-group-6">
               <label for="c-1513">Ошибка "Введен неверный код"</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл+-+Подтвердить+права+на+сеть]+Неверный+код" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
            <!---- Подтвердить права на филиал ---->
            <input type="radio" id="c-152" name="radio-group-5">
            <label for="c-152">Как подтвердить права на филиал</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <ol>
                     <li>Найдите филиал в <a href="https://yandex.ru/maps" target="_blank">Картах</a> или на <a href="https://yandex.ru/sprav/search" target="_blank">странице поиска</a>.</li>
                     <li>Нажмите <b>Вы владелец этой организации?</b> (или <b>Получить доступ</b>). Система предложит запросить код подтверждения.</li>
                     <li>В появившемся окне выберите номер телефона, с помощью которого хотите подтвердить права.</li>
                  </ol>
               </div>
               <div class="radio-content">
                  Получите код и введите его. Код можно ввести позже на странице <a href="https://yandex.ru/sprav/requests/confirmation" target="_blank">Мои заявки</a>.
               </div>
               <div class="radio-content">
                  Компания появится в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>.
               </div>
               <div class="radio-content">
                  <b>Что-то пошло не так:</b>
               </div>
               <!---- Не пришёл код ---->
               <input type="radio" id="c-1521" name="radio-group-6">
               <label for="c-1521">Не пришло SMS с кодом</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Вы можете запросить код для подтверждения еще раз через сутки. Откройте <b>Мои заявки</b> → <b>На подтверждение</b> и нажмите <b>Получить код</b>.
                  </div>
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="m-15211" name="radio-group-7">
                  <label for="m-15211">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="m-15212" name="radio-group-7">
                  <label for="m-15212">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл+-+Подтвердить+права+на+филиал]+Не+пришло+SMS" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Не перезвонили ---->
               <input type="radio" id="c-1522" name="radio-group-6">
               <label for="c-1522">Мне не перезвонили</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="m-15221" name="radio-group-7">
                  <label for="m-15221">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="m-15222" name="radio-group-7">
                  <label for="m-15222">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл+-+Подтвердить+права+на+филиал]+Не+позвонили" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- "Введен неверный код" ---->
               <input type="radio" id="c-1523" name="radio-group-6">
               <label for="c-1523">Ошибка "Введен неверный код"</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл+-+Подтвердить+права+на+филиал]+Неверный+код" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
            <!---- Передать права другому ---->
            <input type="radio" id="c-153" name="radio-group-5">
            <label for="c-153">Как передать права другому человеку</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Если вы владелец компании, выдайте доступ другому пользователю (представителю):
                  <ol>
                     <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте нужную компанию и выберите <b>Доступы</b>.</li>
                     <li>Нажмите <b>Добавить</b> и укажите логин представителя.</li>
                  </ol>
               </div>
               <div class="radio-content">
                  Если вы не видите раздел <b>Доступы</b>, значит вы не владелец организации и выдать права не получится. Пользователь может сам получить доступ к Личному кабинету. Достаточно запросить код подтверждения.
               </div>
               <div class="radio-content">
                  Удалось найти ответ?
               </div>
               <input type="radio" id="m-1531" name="radio-group-6">
               <label for="m-1531">Да. Всё получилось</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Отлично!
                  </div>
               </div>
               <input type="radio" id="m-1532" name="radio-group-6">
               <label for="m-1532">Мне нужна помощь</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл]+Передать+права" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
         </div>
         <!---- В ЛК несколько одинаковых сетей ---->
         <input type="radio" id="n-16" name="radio-group-4">
         <label for="n-16">В Личном кабинете несколько одинаковых сетей</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Дублирование может быть, если одну и ту же сеть добавили для разных регионов. Вы можете удалить одну из них. Для этого:
               <ol>
                  <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте <b>Организации</b>.</li>
                  <li>Напротив нужной компании нажмите <img src="https://lead-assessors.s3.yandex.net/a399146c-005f-4f58-85d9-75a1e8832552" loading="lazy"> → <b>Скрыть из Личного кабинета</b>.</li>
               </ol>
            </div>
            <div class="radio-content">
               На публикацию филиалов это никак не повлияет.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-161" name="radio-group-5">
            <label for="n-161">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-162" name="radio-group-5">
            <label for="n-162">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через+файл]+Удалить+дубль" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Другое ---->
         <input type="radio" id="n-17" name="radio-group-4">
         <label for="n-17">Другое</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Через файл]+Другой+вопрос" id="registration" loading="lazy" ></iframe>
            </div>
         </div>
      </div>
      <!---- Нет ---->
      <input type="radio" id="c-2" name="radio-group-3">
      <label for="c-2">Нет</label>
      <div class="radio-group-4">
         <div class="radio-content">
            <b>Ваш вопрос:</b>
         </div>
         <!---- Создать сеть ---->
         <input type="radio" id="n-21" name="radio-group-4">
         <label for="n-21">Создать сеть</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Компании можно объединить в сеть, если:
               <ul>
                  <li>Как минимум две компании уже есть в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>.</li>
                  <li>Филиалы объединяет общее название или часть названия.</li>
                  <li>Есть общий основной <a href="https://yandex.ru/support/business-priority/add-company/info-terms.html#rules-of-desing__rubrics" target="_blank">вид деятельности</a>.</li>
               </ul>
            </div>
            <div class="radio-content">
               Чтобы объединить филиалы в сеть, заполните форму ниже. Уточните:
            </div>
            <!---- Филиалы привязаны к ЛК ---->
            <input type="radio" id="n-211" name="radio-group-5">
            <label for="n-211">Все филиалы привязаны к моему Личному кабинету</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/1631/?lang=ru&iframe=1&answer_short_text_10192394=[Сети+-+Вручную+-+Создать]+Все+филиалы+уже+привязаны+в+ЛКБ" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
            <!---- Филиалов нет в Я.Бизнесе ---->
            <input type="radio" id="n-212" name="radio-group-5">
            <label for="n-212">Филиалов еще нет в Яндекс Бизнесе</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Филиалы уже открылись?
               </div>
               <!---- Филиалы открылись ---->
               <input type="radio" id="n-2121" name="radio-group-6">
               <label for="n-2121">Да</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>
                           Добавьте филиалы в Карты через <a href="https://yandex.ru/sprav/add" target="_blank">форму</a>. Модерация занимает до двух дней.
                           <div class="info">
                              <div class="content-info">
                                 Статус можно посмотреть на странице Заявки.
                              </div>
                           </div>
                        </li>
                        <li>Когда филиалы появятся в Картах, отправьте заявку на создание сети.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-21211" name="radio-group-7">
                  <label for="n-21211">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-21212" name="radio-group-7">
                  <label for="n-21212">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/1631/?lang=ru&iframe=1&answer_short_text_10192394=[Сети+-+Вручную+-+Создать]+Филиалы+открылись,+но+в+ЛКБ+их+нет" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Филиалы ещё не открылись ---->
               <input type="radio" id="n-2122" name="radio-group-6">
               <label for="n-2122">Нет</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/1631/?lang=ru&iframe=1&answer_short_text_10192394=[Сети+-+Вручную+-+Создать]+Филиалы+не+открылись,+в+ЛКБ+их+нет" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
         </div>
         <!---- Изменить информацию ---->
         <input type="radio" id="n-22" name="radio-group-4">
         <label for="n-22">Изменить информацию</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <b>Что нужно изменить?</b>
            </div>
            <!---- Изменить данные 1 филиала ---->
            <input type="radio" id="n-221" name="radio-group-5">
            <label for="n-221">Данные одного филиала</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Какие правки хотите внести?
               </div>
               <!---- Открыть филиал ---->
               <input type="radio" id="n-2211" name="radio-group-6">
               <label for="n-2211">Открыть филиал</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>Откройте профиль компании в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>.</li>
                        <li>Нажмите <b>О компании</b> → <b>Данные</b>.</li>
                        <li>Укажите, что филиал открыт.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     Проверьте данные на странице компании.
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22111" name="radio-group-7">
                  <label for="n-22111">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22112" name="radio-group-7">
                  <label for="n-22112">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал]+Открыть+филиал" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Закрыть/удалить филиал ---->
               <input type="radio" id="n-2212" name="radio-group-6">
               <label for="n-2212">Закрыть или удалить филиал</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <b>Выберите причину:</b>
                  </div>
                  <!---- Филиал закрылся ---->
                  <input type="radio" id="n-22121" name="radio-group-7">
                  <label for="n-22121">Удалить, филиал закрылся насовсем</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Если компания закрылась, она останется в Картах в статусе <b>Больше не работает</b>. Удалить филиал нельзя.
                     </div>
                     <div class="radio-content">
                        Удалось найти ответ?
                     </div>
                     <input type="radio" id="n-221211" name="radio-group-8">
                     <label for="n-221211">Да. Всё получилось</label>
                     <div class="radio-group-9">
                        <div class="radio-content">
                           Отлично!
                        </div>
                     </div>
                     <input type="radio" id="n-221212" name="radio-group-8">
                     <label for="n-221212">Мне нужна помощь</label>
                     <div class="radio-group-9">
                        <div class="radio-content">
                           <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал+-+Закрыть]+Он+закрыт+насовсем" id="registration" loading="lazy" ></iframe>
                        </div>
                     </div>
                  </div>
                  <!---- Компания вышла из состава сети ---->
                  <input type="radio" id="n-22122" name="radio-group-7">
                  <label for="n-22122">Компания вышла из состава сети</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Удалить филиал нельзя, но можно указать статус <b>Больше не работает</b>. Если компания продолжит работать по этому адресу, <a href="https://yandex.ru/sprav/add" target="_blank">создайте новую карточку</a>.
                     </div>
                     <div class="radio-content">
                        Удалось найти ответ?
                     </div>
                     <input type="radio" id="n-221221" name="radio-group-8">
                     <label for="n-221221">Да. Всё получилось</label>
                     <div class="radio-group-9">
                        <div class="radio-content">
                           Отлично!
                        </div>
                     </div>
                     <input type="radio" id="n-221222" name="radio-group-8">
                     <label for="n-221222">Мне нужна помощь</label>
                     <div class="radio-group-9">
                        <div class="radio-content">
                           <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал+-+Закрыть]+Он+вышел+из+сети" id="registration" loading="lazy" ></iframe>
                        </div>
                     </div>
                  </div>
                  <!---- Филиал пока не работает ---->
                  <input type="radio" id="n-22123" name="radio-group-7">
                  <label for="n-22123">Филиал пока не работает</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> укажите, что филиал закрыт.
                     </div>
                     <div class="radio-content">
                        Удалось найти ответ?
                     </div>
                     <input type="radio" id="n-221231" name="radio-group-8">
                     <label for="n-221231">Да. Всё получилось</label>
                     <div class="radio-group-9">
                        <div class="radio-content">
                           Отлично!
                        </div>
                     </div>
                     <input type="radio" id="n-221232" name="radio-group-8">
                     <label for="n-221232">Мне нужна помощь</label>
                     <div class="radio-group-9">
                        <div class="radio-content">
                           <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал+-+Закрыть]+Временно+не+работает" id="registration" loading="lazy" ></iframe>
                        </div>
                     </div>
                  </div>
               </div>
               <!---- Изменить название филиала ---->
               <input type="radio" id="n-2213" name="radio-group-6">
               <label for="n-2213">Изменить название филиала</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     У всех филиалов сети должно быть одинаковое название. Если компания вышла из сети и теперь у нее новое название, <a href="https://yandex.ru/sprav/add" target="_blank">создайте новую карточку</a>. А этот филиал закройте. Для этого в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> укажите, что он закрыт.
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22131" name="radio-group-7">
                  <label for="n-22131">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22132" name="radio-group-7">
                  <label for="n-22132">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал]+Изменить+название+филиала" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Изменить телефон ---->
               <input type="radio" id="n-2214" name="radio-group-6">
               <label for="n-2214">Изменить телефон</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> → <b>Номера телефонов</b> укажите актуальные контакты.
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22141" name="radio-group-7">
                  <label for="n-22141">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22142" name="radio-group-7">
                  <label for="n-22142">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал]+Изменить+телефон+филиала" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Изменить график работы ---->
               <input type="radio" id="n-2215" name="radio-group-6">
               <label for="n-2215">Изменить график работы</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> → <b>График работы</b> укажите время работы филиала.
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22151" name="radio-group-7">
                  <label for="n-22151">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22152" name="radio-group-7">
                  <label for="n-22152">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал]+Изменить+график+работы+филиала" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Добавить/удалить вход ---->
               <input type="radio" id="n-2216" name="radio-group-6">
               <label for="n-2216">Добавить или удалить вход</label>
               <div class="radio-group-7">
                  <div class="radio-content">
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
                  <input type="radio" id="n-22161" name="radio-group-7">
                  <label for="n-22161">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22162" name="radio-group-7">
                  <label for="n-22162">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал]+Добавить,+удалить+вход+филиала" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Добавить фотографии ---->
               <input type="radio" id="n-2217" name="radio-group-6">
               <label for="n-2217">Добавить фотографии</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Фотографии</b> нажмите <b>Загрузить фотографию</b>.
                  </div>
                  <div class="radio-content">
                     Требования к фотографиям:
                     <ul>
                        <li>формат JPG или PNG;</li>
                        <li>разрешение от 320 × 240 до 5000 × 5000 пикселей;</li>
                        <li>размер до 10 Мб.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Фотографии появятся в течение часа.
                  </div>
                  <div class="radio-content">
                     Если вы загрузили фотографию в Картах, проверка займет до двух недель.
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22171" name="radio-group-7">
                  <label for="n-22171">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22172" name="radio-group-7">
                  <label for="n-22172">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Один+филиал]+Добавить+фотографии+филиала" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
            </div>
            <!---- Изменить данные всех филиалов ---->
            <input type="radio" id="n-222" name="radio-group-5">
            <label for="n-222">Данные для всех филиалов</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Выберите тему:
               </div>
               <!---- Изменить телефон ---->
               <input type="radio" id="n-2221" name="radio-group-6">
               <label for="n-2221">Изменить телефон</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите сеть.</li>
                        <li>Откройте <b>Филиалы</b>, отметьте те, для которых нужно внести правки. Воспользуйтесь фильтром, чтобы выбрать сразу все или филиалы в нужном регионе.</li>
                        <li>Нажмите <b>Редактировать</b> → <b>Телефоны</b>.</li>
                        <li>Внесите правки и нажмите <b>Сохранить</b>.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22211" name="radio-group-7">
                  <label for="n-22211">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22212" name="radio-group-7">
                  <label for="n-22212">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Все+филиалы]+Изменить+телефон" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Изменить сайт ---->
               <input type="radio" id="n-2222" name="radio-group-6">
               <label for="n-2222">Изменить сайт</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите сеть.</li>
                        <li>Откройте <b>Филиалы</b>, отметьте те, для которых нужно внести правки. Воспользуйтесь фильтром, чтобы выбрать сразу все или филиалы в нужном регионе.</li>
                        <li>Нажмите <b>Редактировать</b> → <b>Сайты</b>.</li>
                        <li>Внесите правки и нажмите <b>Сохранить</b>.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22221" name="radio-group-7">
                  <label for="n-22221">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22222" name="radio-group-7">
                  <label for="n-22222">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Все+филиалы]+Изменить+сайт" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Изменить вид деятельности ---->
               <input type="radio" id="n-2223" name="radio-group-6">
               <label for="n-2223">Изменить вид деятельности</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите сеть.</li>
                        <li>Откройте <b>Филиалы</b>, отметьте те, для которых нужно внести правки. Воспользуйтесь фильтром, чтобы выбрать сразу все или филиалы в нужном регионе.</li>
                        <li>Нажмите <b>Редактировать</b> → <b>Вид деятельности</b>.</li>
                        <li>Внесите правки и нажмите <b>Сохранить</b>.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22231" name="radio-group-7">
                  <label for="n-22231">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22232" name="radio-group-7">
                  <label for="n-22232">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Все+филиалы]+Изменить+вид+деятельности" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Изменить название ---->
               <input type="radio" id="n-2224" name="radio-group-6">
               <label for="n-2224">Изменить название</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> выберите сеть.</li>
                        <li>Откройте <b>Филиалы</b>, отметьте те, для которых нужно внести правки. Воспользуйтесь фильтром, чтобы выбрать сразу все или филиалы в нужном регионе.</li>
                        <li>Нажмите <b>Редактировать</b> → <b>Название</b>.</li>
                        <li>Внесите правки и нажмите <b>Сохранить</b>.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     У всех филиалов сети должно быть одинаковое название. Если компания вышла из сети и теперь у нее новое название, <a href="https://yandex.ru/sprav/add" target="_blank">создайте новую карточку</a>. А этот филиал закройте. Для этого в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> в разделе <b>О компании</b> → <b>Данные</b> укажите, что он закрыт.
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22241" name="radio-group-7">
                  <label for="n-22241">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22242" name="radio-group-7">
                  <label for="n-22242">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Все+филиалы]+Изменить+название" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Добавить логотип ---->
               <input type="radio" id="n-2225" name="radio-group-6">
               <label for="n-2225">Добавить логотип для сети</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <ol>
                        <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте нужную сеть.</li>
                        <li>Откройте <b>Филиалы</b>, отметьте те, для которых нужно внести правки. Воспользуйтесь фильтром, чтобы выбрать сразу все или филиалы в нужном регионе.</li>
                        <li>Нажмите <b>Информация</b> → <b>Добавить логотип</b>.</li>
                     </ol>
                  </div>
                  <div class="radio-content">
                     В течение нескольких дней логотип появится во всех профилях филиалов.
                  </div>
                  <div class="radio-content">
                     Требования к логотипу:
                     <ul>
                        <li>логотип должен совпадать с логотипом на сайте сети;</li>
                        <li>формат JPG или PNG;</li>
                        <li>разрешение от 200 × 200 до 5000 × 5000 пикселей, соотношение сторон 1:1;</li>
                        <li>размер до 10 Мб.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-22251" name="radio-group-7">
                  <label for="n-22251">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-22252" name="radio-group-7">
                  <label for="n-22252">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/10015915/?lang=ru&iframe=1&answer_short_text_10192394765=[Сети+-+Вручную+-+Все+филиалы]+Добавить+лого+сети" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
            </div>
         </div>
         <!---- Добавить филиал ---->
         <input type="radio" id="n-223" name="radio-group-4">
         <label for="n-223">Добавить филиал в сеть</label>
         <div class="radio-group-5">
            <div class="info">
               <div class="content-info">
                  Карточка филиала должна соответствовать условиям объединения.
               </div>
            </div>
            <div class="radio-content">
               Чтобы включить в сеть компанию, которая есть в Яндекс Бизнесе:
               <ol>
                  <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте <b>Организации</b>.</li>
                  <li>Около названия сети нажмите <img src="https://lead-assessors.s3.yandex.net/a399146c-005f-4f58-85d9-75a1e8832552"  loading="lazy">.</li>
                  <li>Выберите <b>Добавить в сеть филиал</b>.</li>
                  <li>После выбора нужной компании из списка и нажмите <b>Включить в эту сеть</b>.</li>
               </ol>
            </div>
            <div class="radio-content">
               Чтобы создать новый филиал и сразу добавить его в сеть:
               <ol>
                  <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте <b>Организации</b>.</li>
                  <li>Около названия сети нажмите <img src="https://lead-assessors.s3.yandex.net/a399146c-005f-4f58-85d9-75a1e8832552"  loading="lazy">.</li>
                  <li>Выберите <b>Создать филиал</b>.</li>
                  <li>В всплывающем окне <b>Добавление филиала</b> в сеть укажите актуальные данные.</li>
                  <li>Нажмите <b>Добавить</b>. Новый филиал будет включен в сеть после проверки данных в течение 5 дней.</li>
               </ol>
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-2231" name="radio-group-5">
            <label for="n-2231">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-2232" name="radio-group-5">
            <label for="n-2232">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную]+Добавить+филиал" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Компания уже есть ---->
         <input type="radio" id="n-24" name="radio-group-4">
         <label for="n-24">Такая компания уже есть</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную]+Удалить+дубль" id="registration" loading="lazy" ></iframe>
            </div>
         </div>
         <!---- Подтверждение/передача прав доступа ---->
         <input type="radio" id="n-25" name="radio-group-4">
         <label for="n-25">Подтверждение и передача прав доступа</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <b>Уточните ваш вопрос:</b>
            </div>
            <!---- Подтвердить права на сеть ---->
            <input type="radio" id="n-251" name="radio-group-5">
            <label for="n-251">Как подтвердить права на сеть</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <ol>
                     <li>На <a href="https://yandex.ru/sprav/search" target="_blank">странице поиска</a> ведите название и нажмите <b>Найти</b>.</li>
                     <li>Выберите сеть и нажмите <b>Это моя сеть</b>.</li>
                     <li>В появившемся окне выберите номер телефона, с помощью которого хотите подтвердить права.</li>
                  </ol>
               </div>
               <div class="radio-content">
                  Получите код и введите его. Код можно ввести позже на странице <a href="https://yandex.ru/sprav/requests/confirmation" target="_blank">Мои заявки</a>.
               </div>
               <div class="radio-content">
                  Компания появится в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>.
               </div>
               <div class="radio-content">
                  <b>Что-то пошло не так:</b>
               </div>
               <!---- Не пришёл код ---->
               <input type="radio" id="n-2511" name="radio-group-6">
               <label for="n-2511">Не пришло SMS с кодом</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Вы можете запросить код для подтверждения еще раз через сутки. Откройте <b>Мои заявки</b> → <b>На подтверждение</b> и нажмите <b>Получить код</b>.
                  </div>
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-25111" name="radio-group-7">
                  <label for="n-25111">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-25112" name="radio-group-7">
                  <label for="n-25112">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную+-+Подтвердить+права+-+Сеть]+Не+пришло+SMS" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Не перезвонили ---->
               <input type="radio" id="n-2512" name="radio-group-6">
               <label for="n-2512">Мне не перезвонили</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-25121" name="radio-group-7">
                  <label for="n-25121">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-25122" name="radio-group-7">
                  <label for="n-25122">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную+-+Подтвердить+права+-+Сеть]+Не+позвонили" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- "Введен неверный код" ---->
               <input type="radio" id="n-2513" name="radio-group-6">
               <label for="n-2513">Ошибка "Введен неверный код"</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную+-+Подтвердить+права+-+Сеть]+Неверный+код" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
            <!---- Подтвердить права на филиал ---->
            <input type="radio" id="n-252" name="radio-group-5">
            <label for="n-252">Как подтвердить права на филиал</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <ol>
                     <li>Найдите филиал в <a href="https://yandex.ru/maps" target="_blank">Картах</a> или на <a href="https://yandex.ru/sprav/search" target="_blank">странице поиска</a>.</li>
                     <li>Нажмите <b>Вы владелец этой организации?</b> (или <b>Получить доступ</b>). Система предложит запросить код подтверждения.</li>
                     <li>В появившемся окне выберите номер телефона, с помощью которого хотите подтвердить права.</li>
                  </ol>
               </div>
               <div class="radio-content">
                  Получите код и введите его. Код можно ввести позже на странице <a href="https://yandex.ru/sprav/requests/confirmation" target="_blank">Мои заявки</a>.
               </div>
               <div class="radio-content">
                  Компания появится в <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a>.
               </div>
               <div class="radio-content">
                  <b>Что-то пошло не так:</b>
               </div>
               <!---- Не пришёл код ---->
               <input type="radio" id="n-2521" name="radio-group-6">
               <label for="n-2521">Не пришло SMS с кодом</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Вы можете запросить код для подтверждения еще раз через сутки. Откройте <b>Мои заявки</b> → <b>На подтверждение</b> и нажмите <b>Получить код</b>.
                  </div>
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-25211" name="radio-group-7">
                  <label for="n-25211">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-25212" name="radio-group-7">
                  <label for="n-25212">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную+-+Подтвердить+права+-+Филиал]+Не+пришло+SMS" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- Не перезвонили ---->
               <input type="radio" id="n-2522" name="radio-group-6">
               <label for="n-2522">Мне не перезвонили</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Если вы выбрали получение кода через звонок, возможны два варианта:
                     <ul>
                        <li>Вам поступит звонок от автомодератора в течение 10 минут.</li>
                        <li>Оператор позвонит в течение дня в рабочие часы.</li>
                     </ul>
                  </div>
                  <div class="radio-content">
                     Удалось найти ответ?
                  </div>
                  <input type="radio" id="n-25221" name="radio-group-7">
                  <label for="n-25221">Да. Всё получилось</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        Отлично!
                     </div>
                  </div>
                  <input type="radio" id="n-25222" name="radio-group-7">
                  <label for="n-25222">Мне нужна помощь</label>
                  <div class="radio-group-8">
                     <div class="radio-content">
                        <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную+-+Подтвердить+права+-+Филиал]+Не+позвонили" id="registration" loading="lazy" ></iframe>
                     </div>
                  </div>
               </div>
               <!---- "Введен неверный код" ---->
               <input type="radio" id="n-2523" name="radio-group-6">
               <label for="n-2523">Ошибка "Введен неверный код"</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную+-+Подтвердить+права+-+Филиал]+Неверный+код" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
            <!---- Передать права другому ---->
            <input type="radio" id="n-253" name="radio-group-5">
            <label for="n-253">Как передать права другому человеку</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Если вы владелец компании, выдайте доступ другому пользователю (представителю):
                  <ol>
                     <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте нужную компанию и выберите <b>Доступы</b>.</li>
                     <li>Нажмите <b>Добавить</b> и укажите логин представителя.</li>
                  </ol>
               </div>
               <div class="radio-content">
                  Если вы не видите раздел <b>Доступы</b>, значит вы не владелец организации и выдать права не получится. Пользователь может сам получить доступ к Личному кабинету. Достаточно запросить код подтверждения.
               </div>
               <div class="radio-content">
                  Удалось найти ответ?
               </div>
               <input type="radio" id="n-2531" name="radio-group-6">
               <label for="n-2531">Да. Всё получилось</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     Отлично!
                  </div>
               </div>
               <input type="radio" id="n-2532" name="radio-group-6">
               <label for="n-2532">Мне нужна помощь</label>
               <div class="radio-group-7">
                  <div class="radio-content">
                     <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную]+Передать+права" id="registration" loading="lazy" ></iframe>
                  </div>
               </div>
            </div>
         </div>
         <!---- В ЛК несколько одинаковых сетей ---->
         <input type="radio" id="n-26" name="radio-group-4">
         <label for="n-26">В Личном кабинете несколько одинаковых сетей</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Дублирование может быть, если одну и ту же сеть добавили для разных регионов. Вы можете удалить одну из них. Для этого:
               <ol>
                  <li>В <a href="https://yandex.ru/sprav/companies" target="_blank">Личном кабинете</a> откройте <b>Организации</b>.</li>
                  <li>Напротив нужной компании нажмите <img src="https://s3.mds.yandex.net/doc-binary/src/support/business-priority/ru/menu.png"  loading="lazy"> → Скрыть из Личного кабинета.</li>
               </ol>
            </div>
            <div class="radio-content">
               На публикацию филиалов это никак не повлияет.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-261" name="radio-group-5">
            <label for="n-261">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-262" name="radio-group-5">
            <label for="n-262">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную]+Дубли+сети+в+ЛКБ" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Обновить сеть через файл ---->
         <input type="radio" id="n-27" name="radio-group-4">
         <label for="n-27">Хочу обновлять сеть через файл</label>
         <div class="radio-group-5">
            <div class="radio-content">
               Настройте регулярное обновление данных с помощью XML-файла:
               <ol>
                  <li>Подготовьте файл в формате XML (подробнее см. в <a href="https://yandex.ru/support/business-priority/branches/xml-feed-sprav.html" target="_blank">Справке</a>.</li>
                  <li>Выложите файл на свой сайт по обновляемой ссылке.</li>
                  <li>Укажите ссылку в Личном кабинете сети и дождитесь проверки.</li>
               </ol>
            </div>
            <div class="radio-content">
               Когда вы обновите XML-файл, произойдет автоматическая синхронизация (обычно в течение нескольких суток). Обновленные данные появятся на сервисах Яндекса. Через файл можно обновлять адрес, телефон, часы работы и другую информацию.
            </div>
            <div class="radio-content">
               Удалось найти ответ?
            </div>
            <input type="radio" id="n-271" name="radio-group-5">
            <label for="n-271">Да. Всё получилось</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  Отлично!
               </div>
            </div>
            <input type="radio" id="n-272" name="radio-group-5">
            <label for="n-272">Мне нужна помощь</label>
            <div class="radio-group-6">
               <div class="radio-content">
                  <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/1631/?lang=ru&iframe=1&answer_short_text_10192394=[Сети+-+Вручную]+Хочу+обновлять+через+файл" id="registration" loading="lazy" ></iframe>
               </div>
            </div>
         </div>
         <!---- Другое ---->
         <input type="radio" id="n-28" name="radio-group-4">
         <label for="n-28">Другое</label>
         <div class="radio-group-5">
            <div class="radio-content">
               <iframe width="100%" frameborder="0" src="https://forms.yandex.ru/surveys/3063/?lang=ru&iframe=1&answer_short_text_10146751=[Сети+-+Вручную]+Другой+вопрос" id="registration" loading="lazy" ></iframe>
            </div>
         </div>
      </div>
   </div>
</div>
<div><br></div>

<div class="banner">
   <div class="banner-title"></div>
   <a href="https://yandex.ru/adv/edu/online/business?utm_source=support&utm_medium=business&utm_content=banner" target="_blank" class="banner-button"></a>
   <div class="banner-title"></div>
</div>

{% include [footer](../_includes/footer.md) %}

<div><br><br><br></div>
<div class="container">
  <div class="column">
      <p style="font-size: large;">Полезные ссылки</p>
      <ul>
         <li><a href="https://yandex.ru/sprav/add/" target="_blank">Добавить компанию</a></li>
         <li><a href="https://yandex.ru/project/sprav-partner" target="_blank">Стать партнером Яндекс&nbsp;Бизнеса</a></li>
         <li><a href="https://yandex.ru/support/maps/" target="_blank">Справка Яндекс&nbsp;Карт</a></li>
         <li><a href="https://yandex.ru/legal/rules/" target="_blank">Пользовательское соглашение сервисов Яндекса</a></li>
         <li><a href="https://yandex.ru/support/business-priority/troubleshooting/favplacement.html" target="_blank">Служба поддержки рекламодателей</a></li>
      </ul>
  </div>
   <div class="column">
      <p style="font-size: large;">Правовые документы</p>
      <ul>
         <li><a href="https://yandex.ru/legal/oferta_geo/" target="_blank">Оферта</a></li>
         <li><a href="https://yandex.ru/legal/advertising_subscription/" target="_blank">Условия оказания услуги «Рекламная подписка на&nbsp;Яндекс»</a></li>
         <li><a href="https://yandex.ru/legal/directory_conditions/" target="_blank">Условия приоритетного размещения для&nbsp;России</a></li>
         <li><a href="https://yandex.by/legal/directory_conditions/" target="_blank">Условия приоритетного размещения для&nbsp;Беларуси</a></li>
      </ul>
  </div>
</div>

<!-------------------------->

<div style="clear: both;"></div>

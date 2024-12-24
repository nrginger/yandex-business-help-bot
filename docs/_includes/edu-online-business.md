{% if tld == "ru" %}

<div class="container-galery">
  <div class="doc-c-imagemaps">
      <div class="doc-c-imagemaps__image">
          <a class="doc-c-imagemaps__shape" title="Перейти в обучение" href="https://yandex.ru/adv/edu/online/business?utm_source=support&utm_medium=business&utm_content=banner" style="top: 67.5258%; left: 6.09756%; height: 21.6495%; width: 87.5%;"></a><img src="https://yastatic.net/s3/doc-binary/src/support/business-priority/ru/files/mobile-banner.svg">          
      </div>
  </div> 
</div>

{% endif %}

<style>
.container-galery {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
    gap: 15px;
    margin: 0 auto 20px;
    max-width: 830px;
}
.doc-c-imagemaps__image {
    display: inline-block;
    position: relative;
}
.doc-c-imagemaps__shape {
    box-sizing: border-box;
    position: absolute;
}
@media screen and (max-width: 767px) {
  .container-galery {
    grid-template-columns: 1fr;
    justify-items: center;
  }
}
</style>

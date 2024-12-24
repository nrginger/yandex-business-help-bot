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

// Javascript script that fetches and prints how to
// say “Hello” depending of the language
$(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    const urlFull = 'https://www.fourtonfish.com/hellosalut/?lang=' + lang
    $.getJSON(urlFull, function (body) {
      $('div#hello').text(body.hello)
    });
  });
});

// Javascript script that fetches from
// https://fourtonfish.com/hellosalut/?lang=fr and displays
// the value of hello from that fetch in the HTML’s tag DIV#hello.
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});

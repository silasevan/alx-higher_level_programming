// Write a Javascript script that adds a LI element to
// a list when the user clicks on the tag add_item
const item = "<li>Item</li>"
$('#add_item').click(function () {
  $('.my_list').append(item);
});

$(document).ready(function() {
  var list = $('ul.my_list');
  $('#add_item').click(function() {
    list.append('<li>Item</li>');
  });
  $('#remove_item').click(function() {
    list.find('li:last').remove();
  });
  $('#clear_list').click(function() {
    list.empty();
  });
});


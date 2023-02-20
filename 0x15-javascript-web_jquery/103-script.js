$(document).ready(function() {
  // Add event listener for button click
  $('#btn_translate').click(function() {
    translateHello();
  });

  // Add event listener for enter key press in input field
  $('#language_code').keypress(function(event) {
    if (event.which == 13) {
      translateHello();
    }
  });

  // Function to fetch translation and update output
  function translateHello() {
    var langCode = $('#language_code').val();
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/?lang=' + langCode;
    
    $.get(apiUrl, function(data) {
      var translation = data.hello;
      $('#hello').text(translation);
    });
  }
});


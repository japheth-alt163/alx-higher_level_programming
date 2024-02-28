$(document).ready(function(){
    $('#btn_translate').click(translateHello);
    $('#language_code').keypress(function(e){
        if (e.which == 13) {
            translateHello();
        }
    });

    function translateHello() {
        const languageCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
        
        $.get(apiUrl, function(data){
            $('#hello').text(data.hello);
        });
    }
});

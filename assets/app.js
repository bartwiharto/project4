//here I would use ajax to call the api, grab the quote as the response and use innerHTML to append it to #quote-box in base html file
$(document).ready(function(){
    console.log('nest ninjas smell like burritos')
    $.ajax({
        method:'GET',
        url: 'https://talaikis.com/api/quotes/random/',
        success: function(result){
            console.log(result.author)
            $('#quote-box').html(result.quote + ' - ' + result.author)
        }
    })
})
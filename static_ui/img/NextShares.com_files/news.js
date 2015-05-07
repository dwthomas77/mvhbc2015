// News Global Object
var news = news || {

    // array of news articles
    articles : [],

    // assume news Singleton initiated as news
    launchVideoPlayer : function(e) {
        // find current video content string
        var name = $(e.target).attr("data-name");
        // find matching video url tag
        var videoTag = _.result(_.findWhere(news.articles, {'name': name}), 'videoTag');

        // if matching video URL found
        if(videoTag){
            //load video content
            $('.js-modalContent').html(videoTag);
        }

    }
};

// load the news.json file
$.getJSON( "./data/news.json", function(data) {
    news.articles = data.articles;
});

// Event Handlers
$( document ).ready(function() {
    $('.js-openVideo').on('click', news.launchVideoPlayer);
});
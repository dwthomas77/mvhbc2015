 var filter = {
    fromDate: function(date,arr){
    },
    toDate: function(date,arr){
    },
    type: function(news,filterTypes){
        var results = [];
        _.forEach(filterTypes,function(type){
            _.filter(news, function(newsItem) {
                if( _.includes(newsItem.metaTags,type) && !(_.includes(results,newsItem)) ){
                    results.push(newsItem);
                }
            });
        });
        return results;
    }
};

$(function () {
    $(".datepicker").datepicker();
    
    $.getJSON( "./data/news.json", function( data ) { 
        var news = data.articles;
        
        $(".filter-apply-btn").click(function(){
            var filterTypes = [];
            $('input[name="filter"]:checked').each(function() {
                console.log(this.value);
                filterTypes.push(this.value);
            });
            console.log(filter.type(news,filterTypes));
        });
        
        $(".filter-clear-btn").click(function(){
            $('input[name="filter"]').removeAttr('checked');
        });
        
    });
});
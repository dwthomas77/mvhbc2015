// Navigation Functionality
var navigation = {
    activePage: function() {
        var path = $(location).attr('pathname');
        $('a[href="'+path+'"]').parent().addClass('active');
    },
    toggleMobileNav: function() {
        $('.navigation').toggleClass('slideRight');
        $('.navigation-menu-btn').toggleClass('slide');
        $('.nsPage').toggleClass('slide');
    }
};


(function ($) {
    $(document).ready(function () {
        //check current path and set active nav-link
        navigation.activePage();
        
        // Trigger mobile Navigation functionality
        $('.menu-btn').click(navigation.toggleMobileNav);
    });
})(jQuery);
(function($) {
  $(document).on('click', '.item-action > .fa, .item-action .action > .closer' function(e) {
    e.preventDefault();
    $(this).parents('.item-action').toggleClass('active');
  });
})(jQuery);
// $(document).ready(function() {
//     var items = $("h2, h3");
//     var all = [];
    
//     items.each(function() {
//       $(this).data("top", parseInt($(this).offset()["top"]));
//     });
    
//     $(window).on("scroll", function() {
//       var scrollTop = $(window).scrollTop() - 1;
      
//       //if (scrollTop % 2 == 0) {
//         all = [];
        
//         $.each(items, function() {
//           var $this = $(this),
//               top = $this.data("top");
          
//           var onScreen = (top >= scrollTop && top <= $(window).innerHeight() + scrollTop);
          
//           if (onScreen)
//             all.push($this.attr("id"));
//         });
        
//         if (all.length > 0) {
//           var links = $(".index > ol li a");
          
//           $.each(links, function() {
//             var $this = $(this);
//             var $li = $this.parent("li");
//             $li.prop("class", "");
            
//             if ($.inArray($this.attr("href").substring(1), all) > -1)
//                 $li.addClass("active");
//           });
//         }
//       //}
//     });
//   });


$(document).ready(function(){
  $(window).scroll(function () {   
     
   if($(window).scrollTop() > 200) {
      $('.category-bar').css('position','fixed');
      $('.category-bar').css('top','0'); 
   }
  
   else if ($(window).scrollTop() <= 200) {
      $('.category-bar').css('position','');
      $('.category-bar').css('top','');
   }  
      if ($('.category-bar').offset().top + $(".category-bar").height() > $("#footer").offset().top) {
          $('.category-bar').css('top',-($(".category-bar").offset().top + $(".category-bar").height() - $("#footer").offset().top));
      }
  });
  });

$(".student").hide();
$(".startup_li").addClass("active");

$(".student_li").click(function () {
  $(this).addClass("active");
  $(".startup_li").removeClass("active");
  $(".student").show();
  $(".startup").hide();
});

$(".startup_li").click(function () {
  $(this).addClass("active");
  $(".student_li").removeClass("active");
  $(".startup").show();
  $(".student").hide();
});

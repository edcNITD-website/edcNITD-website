$('#avatars input:radio').addClass('input_hidden');
$('#avatars label').click(function() {
    $(this).addClass('border-4 border-blue-400 rounded-full').siblings().removeClass('border-4 border-blue-400 rounded-full');
});
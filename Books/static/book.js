$(function () {
  $(".js-create-book").click(function () {
    $.ajax({
      url: '/books/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  });

});


$('#modal-book').on('submit','.js-book-create-form',function () {
    var form=$(this)
    $.ajax({
        url: form.attr('action'),
        data: form.serialize(),
        dataType:'json',
        type:form.attr('method'),
        success: function (data) {
            if(data.form_is_valid){
                console.log(data)
                    $('#book-table tbody').html(data.html_book_list)
                $("#modal-book").modal("hide");

            }
            else {
                $('#modal-book .modal-content').html(data.html_form)
            }
        }
    })
    return false;
});
$(function () {
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    );

    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }

});
$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget)
  var recipient = button.data('whatever')
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})

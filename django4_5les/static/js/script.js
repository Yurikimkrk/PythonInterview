$(function () {
    $('#add-button').on('click', function (e) {
        let modal = $(this).parents('.modal').first();
        let form = modal.find('form');
        $.post(form.attr('action'), form.serialize(), data => {
            $('table').html(data.catalog_html);
            modal.modal('toggle');
        });
    });
    $('#modal').on('show.bs.modal', function (e) {
        let modal = $(this);
        let form = modal.find('form');
        $.get(form.attr('action'), data => {
            initForm(form, data)
        });
    });
});

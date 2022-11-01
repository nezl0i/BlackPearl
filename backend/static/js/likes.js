function addRemovePostLike() {
    $('.add-remove-like').each((index, el) => {
        console.log(el)
        $(el).on('submit', (e) => {

            const post_id = $(el).find('input[name="post_id"]').val();
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            if ($(e.currentTarget).hasClass('post-like')) {
                e.preventDefault(e);
                $.ajax({
                    headers: {'X-CSRFToken': csrftoken},
                    url: "/likes/ajax/",
                    type: "POST",
                    dataType: "json",
                    data: {
                        post_id: post_id,
                    },

                    success: function (datas) {
                        $('.add-remove-like').html(datas.result);
                    }

                    // success: (data) => {
                    //     location.reload();
                    // }
                });
            }
        });
    });
}

$(document).ready(() => {
    addRemovePostLike();
});
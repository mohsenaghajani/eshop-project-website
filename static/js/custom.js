function sendArticleComment(articleId){
    var comment = $('#commentText').val();
    var parent = $('#parent_id').val()
    // console.log(comment);
    $.get('/get-comment/', {
        comment : comment,
        article_id : articleId,
        parent_id : parent,

    }).then(res =>{
        console.log(res);
        location.reload()
    })

}

function fillParentId(parentId){
    $('#parent_id').val(parentId)
    document.getElementById('comment-form').scrollIntoView({behavior: 'smooth'})
}
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
        $('#comments-area').html(res);
        $('#parent_id').val('');
        $('#commentText').val('');
        if(parent !== null && parent !== '') {
            document.getElementById('comment-box-' + parent).scrollIntoView({behavior: 'smooth'})
        }else{
            document.getElementById('comments-area').scrollIntoView({behavior: 'smooth'})
            }




    });

}

function fillParentId(parentId){
    $('#parent_id').val(parentId)
    document.getElementById('comment-form').scrollIntoView({behavior: 'smooth'})
}

function filterProduct(){
    const filterPrice = $('#sl2').val();
    const startPrice = filterPrice.split(',')[0];
    const endPrice = filterPrice.split(',')[1];
    $('#start-price').val(startPrice);
    $('#end-price').val(endPrice);
    $('#filter-form').submit();
}

function fillPage(page){
    $('#page').val(page);
    $('#filter-form').submit()
}

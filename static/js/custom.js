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

function showLargeImage(imageSrc){
    $('#light-box-image').attr('href', imageSrc)
    $('#mainImage').attr('src', imageSrc)
}


function addToOrder(productId){
    const productCount = $('#product_count').val()
    $.get('/order/add_to_basket?product_id=' + productId + '&count=' + productCount).then(res =>
    Swal.fire({
  title: "نتیجه",
  text: res.text,
  icon: res.icon,
  showCancelButton: true,
  confirmButtonColor: "#3085d6",
  cancelButtonColor: "#d33",
  confirmButtonText: res.confirm_button_text
}).then((result) => {
    if (res.status === 'not_auth'){
  if (result.isConfirmed) {
    window.location.href = '/login';
  }}
}))
}

function removeDetail(detailId){
    $.get('/order/remove_basket_detail?detail_id=' + detailId).then(res =>{
        if(res.status === 'success'){
            $('#order_detail_content').html(res.data)
        }
    })
}

function changeOrderDetailCount(detailId, state){

        $.get('/order/change_basket_detail?detail_id=' + detailId + '&state=' +state).then(res =>{
        if(res.status === 'success'){
            $('#order_detail_content').html(res.data)
        }
    })
}
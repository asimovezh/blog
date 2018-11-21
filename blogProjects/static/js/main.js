$(function() {
    //当滚动条的位置处于距顶部100像素以下时,跳转链接出现,否则消失
    $(function() {
        $(window).scroll(function() {
            if ($(window).scrollTop() > 120 ){
                $("#back-to-top").fadeIn(150);
                }
                else {
                    $("#back-to-top").fadeOut(150);
                }
            });
            //当点击跳转链接后,回到页面顶部位置
            $("#back-to-top").click(function(){
                $('body,html').animate({scrollTop:0},500);
                return false;
            });
        });
    });


function initEditor() {
  $(function() {
    var editor,toolbar;
    Simditor.locale = 'zh-CN';
    toolbar = ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link', 'image', 'hr', '|', 'indent', 'outdent', 'alignment'];

    editor = new Simditor({
      textarea: $('#id_comment'),
      placeholder: '请输入你的留言...',
      toolbar: toolbar,
      pasteImage: true,
      defaultImage: 'http://127.0.0.1:8000/media/category/2018/08/django.jpg',
      upload: true,
    });
  });

};
initEditor();




SyntaxHighlighter.all();


  function toggleChapter(icon) {
    var
        $i = $(icon);
        expand = $i.attr('expand');
        id=$i.attr("id");
    if (expand === 'true') {
       $i.find('span').removeClass('glyphicon glyphicon-minus-sign');
	   $i.find('span').addClass('glyphicon glyphicon-plus-sign');
	   $i.attr('expand', 'false');
	   $("[id="+id+"]").filter(".chapter-s").each(function(){    $(this).css("display","none")  });
    } else {

	$i.find("span").removeClass('glyphicon glyphicon-plus-sign');


	$i.find("span").addClass('glyphicon glyphicon-minus-sign');
	$i.attr('expand', 'true');
	$("[id="+id+"]").filter(".chapter-s").each(function(){$(this).css("display","block")  });
    }
};


       function toggleAll(icon) {
    var
        $i = $(icon);

        id=$i.attr("id");
    if (id === 'minus') {
       $(".chapSpand").find("span").removeClass('glyphicon glyphicon-minus-sign');
       $(".chapSpand").find("span").addClass('glyphicon glyphicon-plus-sign');
	   $(".chapter-s").each(function(){    $(this).css("display","none")  });
    } else {

       $(".chapSpand").find("span").removeClass('glyphicon glyphicon-plus-sign');
       $(".chapSpand").find("span").addClass('glyphicon glyphicon-minus-sign');


       $(".chapter-s").each(function(){    $(this).css("display","block")  });
    }
};



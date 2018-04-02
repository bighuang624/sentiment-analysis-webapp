$(document).ready(function() {

    function predict() {
        if ($("input").val() !== "") {
            $.post("http://localhost:5000/predict", {
                "sentence": $("input").val()
            }, function(data, status) {
                $("span#score").text(data);
            })
        }
    }

    $("button#start").click(function() {
        predict()
    })

    let randomWords = [
        '在所有人事已非的景色里，我最喜欢你',
        '经历了人生百态世间的冷暖，这笑容温暖纯真',
        '爱是一道光如此美妙，指引我们想要的未来',
        '上菜巨慢不说，服务态度还超级差，东西咸的要死，而且普遍的贵，这辈子不会再来了。',
        '饥饿营销的噱头。。味道比北京差远了，服务也很差',
        '挺好的，菜品比较全，种类多，添加也快',
        '已经多次消费了，超棒的，人好多。',
        '非常不愉快的用餐体验，以后不来了',
        '喜欢的一家店，菜不错，环境也喜欢',
        '什么破地方，说能刷卡，到那又不能刷，简直太懒了',
        '很难吃啊，又超级贵，菜量特别少，没什么亮点，真的不推荐来这家店'
    ]

    $("button#random").click(function() {
        $("input").val(randomWords[Math.floor(Math.random() * randomWords.length)])
        predict()
    })
})
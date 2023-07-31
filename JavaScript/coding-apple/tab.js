/*버튼 0(Products)을 누르면  
0. 버튼0, 1 붙은 주황색 제거
0. 내용0,1,2 안보이게 하기
1. 버튼 0이 주황색으로 하이라이트가 되어야함
2. 내용 0이 보여야함*/

for (let i = 0; i < 3; i++) {
	$(".tab-button")
		.eq(i)
		.on("click", function () {
			$(".tab-button").removeClass("orange");
			$(".tab-button").eq(i).addClass("orange");
			$(".tab-content").removeClass("show");
			$(".tab-content").eq(i).addClass("show");
		});
}

// for (let i = 0; i < $(".tab-button").length; i++) {
// 	$(".tab-button")
// 		.eq(i)
// 		.on("click", function () {
// 			$(".tab-button").removeClass("orange");
// 			$(".tab-button").eq(i).addClass("orange");
// 			$(".tab-content").removeClass("show");
// 			$(".tab-content").eq(i).addClass("show");
// 		});
// }

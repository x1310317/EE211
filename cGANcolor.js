var select = document.getElementById("inputGroupSelect");
var edgeimg = document.getElementById("edgeimg");
var resimg = document.getElementById("resimg");
var progress = document.getElementById("progressbtn");

document.getElementById("dataset").onclick = function(){
	document.getElementById("dataset-box").style.visibility = "visible";
}
document.getElementById("preproccess").onclick = function(){
	document.getElementById("facial-box").style.visibility = "visible";
	document.getElementById("edge-box").style.visibility = "visible";
	document.getElementById("median-box").style.visibility = "visible";
}
document.getElementById("train").onclick = function(){
	document.getElementById("train1-box").style.visibility = "visible";
	document.getElementById("train2-box").style.visibility = "visible";
	document.getElementById("train3-box").style.visibility = "visible";
	document.getElementById("train4-box").style.visibility = "visible";
}

document.getElementById("stop").onclick = function(){
	document.getElementById("resimg-box").style.visibility = "hidden";
	progress.style.width = "0%";
}

document.getElementById("run").onclick = function(){
	setTimeout(function(){
		progress.style.width = "20%";
		setTimeout(function(){
			progress.style.width = "50%";
			setTimeout(function(){
				progress.style.width = "80%";
				setTimeout(function(){
					progress.style.width = "100%";
					setTimeout(function(){
						document.getElementById("resimg-box").style.visibility = "visible";
					}, Math.floor(Math.random() * Math.floor(500) + 800));
				}, Math.floor(Math.random() * Math.floor(500) + 800));
			}, Math.floor(Math.random() * Math.floor(500) + 800));
		}, Math.floor(Math.random() * Math.floor(500) + 800));
	}, Math.floor(Math.random() * Math.floor(500) + 800));

}
select.onchange = function(){
	if (select.options[select.selectedIndex].value == 1){
		edgeimg.src = "test.png";
		resimg.src = "test.png";
		document.getElementById("resimg-box").style.visibility = "hidden";
		progress.style.width = "0%";
	}
	if (select.options[select.selectedIndex].value == 2){
		edgeimg.src = "2.jpg";
		resimg.src = "2.jpg";
		document.getElementById("resimg-box").style.visibility = "hidden";
		progress.style.width = "0%";
	}
}

/* アイコン（SVGスプライト）と、画像スロットの自動差し込み */
(function(){
  var S='<svg xmlns="http://www.w3.org/2000/svg" style="display:none">'
  +'<symbol id="i-camera" viewBox="0 0 24 24"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></symbol>'
  +'<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s7-6.2 7-11a7 7 0 10-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></symbol>'
  +'<symbol id="i-leaf" viewBox="0 0 24 24"><path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14z"/><path d="M5 19c3-5 6-8 10-10"/></symbol>'
  +'<symbol id="i-factory" viewBox="0 0 24 24"><path d="M3 20V10l5 3v-3l5 3V6h4v14z"/><path d="M7 20v-3M12 20v-3"/></symbol>'
  +'<symbol id="i-bike" viewBox="0 0 24 24"><circle cx="6" cy="16" r="3.5"/><circle cx="18" cy="16" r="3.5"/><path d="M6 16l4-8h5l3 8M10 8H8M12 16l3-8"/></symbol>'
  +'<symbol id="i-school" viewBox="0 0 24 24"><path d="M3 10l9-5 9 5-9 5z"/><path d="M7 12.5V17c3 2 7 2 10 0v-4.5"/></symbol>'
  +'<symbol id="i-book" viewBox="0 0 24 24"><path d="M4 5h6a2 2 0 012 2v12a2 2 0 00-2-2H4zM20 5h-6a2 2 0 00-2 2v12a2 2 0 012-2h6z"/></symbol>'
  +'<symbol id="i-pencil" viewBox="0 0 24 24"><path d="M4 20l1-4L16 5l3 3L8 19z"/></symbol>'
  +'<symbol id="i-trophy" viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 01-8 0zM8 6H5v1a3 3 0 003 3M16 6h3v1a3 3 0 01-3 3M12 13v4M8 20h8"/></symbol>'
  +'<symbol id="i-home" viewBox="0 0 24 24"><path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-5h4v5"/></symbol>'
  +'<symbol id="i-chart" viewBox="0 0 24 24"><path d="M5 20V10M12 20V4M19 20v-7"/></symbol>'
  +'<symbol id="i-spark" viewBox="0 0 24 24"><path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/></symbol>'
  +'<symbol id="i-people" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6M15 14.5c3 0 6 1.6 6 5.5"/></symbol>'
  +'<symbol id="i-target" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".8"/></symbol>'
  +'</svg>';
  var d=document.createElement('div');d.innerHTML=S;document.body.insertBefore(d.firstChild,document.body.firstChild);
  [].forEach.call(document.querySelectorAll('[data-i]'),function(el){
    el.insertAdjacentHTML('afterbegin','<svg class="i"><use href="#i-'+el.dataset.i+'"/></svg>');
  });
  /* 画像スロット：data-img のファイルがあれば自動で表示 */
  [].forEach.call(document.querySelectorAll('[data-img]'),function(el){
    var im=new Image();
    im.onload=function(){el.style.backgroundImage='url("'+im.src+'")';el.classList.add('loaded')};
    im.src=el.dataset.img;
  });
})();

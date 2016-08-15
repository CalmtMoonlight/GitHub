# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from baidu.items import BaiduItem


class BaiduSpider(CrawlSpider):

    name = "BaiDuSpider"

    start_urls = [
        'http://www.baidu.com/'

    ]

    abc = """

    <!DOCTYPE html><!--STATUS OK--><html><head><meta http-equiv="content-type" content="text/html;charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta content="always" name="referrer"><meta name="theme-color" content="#2932e1"><link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" /><link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu.svg"><link rel="dns-prefetch" href="//s1.bdstatic.com"/><link rel="dns-prefetch" href="//t1.baidu.com"/><link rel="dns-prefetch" href="//t2.baidu.com"/><link rel="dns-prefetch" href="//t3.baidu.com"/><link rel="dns-prefetch" href="//t10.baidu.com"/><link rel="dns-prefetch" href="//t11.baidu.com"/><link rel="dns-prefetch" href="//t12.baidu.com"/><link rel="dns-prefetch" href="//b1.bdstatic.com"/><title>百度一下，你就知道</title>
    <style index="index"  id="css_index">html,body{height:100%}html{overflow-y:auto}body{font:12px arial;text-align:;background:#fff}body,p,form,ul,li{margin:0;padding:0;list-style:none}body,form,#fm{position:relative}td{text-align:left}img{border:0}a{color:#00c}a:active{color:#f60}input{border:0;padding:0}#wrapper{position:relative;_position:;min-height:100%}#head{padding-bottom:100px;text-align:center;*z-index:1}#ftCon{height:100px;position:absolute;bottom:23px;text-align:left;width:100%;margin:0 auto;z-index:0;overflow:hidden}.ftCon-Wrapper{overflow:hidden;margin:0 auto;text-align:center;*width:640px}#qrcode{display:inline-block;*float:left;*margin-top:4px}#qrcode .qrcode-item{float:left}#qrcode .qrcode-item-2{margin-left:33px}#qrcode .qrcode-img{float:left;width:60px;height:60px}#qrcode .qrcode-item-1 .qrcode-img{background:url(http://s1.bdstatic.com/r/www/cache/static/home/img/qrcode/zbios_a4b2d86f.png) 0 0 no-repeat}#qrcode .qrcode-item-2 .qrcode-img{background:url(http://s1.bdstatic.com/r/www/cache/static/home/img/qrcode/nuomi_510f7472.png) 0 0 no-repeat}
    @media only screen and (-webkit-min-device-pixel-ratio:2){#qrcode .qrcode-item-1 .qrcode-img{background-image:url(http://s1.bdstatic.com/r/www/cache/static/home/img/qrcode/zbios_x2_bb1cd2e7.png);background-size:60px 60px}#qrcode .qrcode-item-2 .qrcode-img{background-image:url(http://s1.bdstatic.com/r/www/cache/static/home/img/qrcode/nuomi_x2_de75d5db.png);background-size:60px 60px}}#qrcode .qrcode-text{float:left;color:#999;line-height:23px;margin:8px 0 0 10px}#qrcode .qrcode-text a{color:#999;text-decoration:none}#qrcode .qrcode-text p{text-align:left}#qrcode .qrcode-text b{color:#666;font-weight:bold}#qrcode .qrcode-text span{letter-spacing:1px}#ftConw{display:inline-block;text-align:left;margin-left:33px;line-height:22px;position:relative;top:-2px;*float:right;*margin-left:0;*position:static}#ftConw,#ftConw a{color:#999}.bg{background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_0e814c16.png);background-repeat:no-repeat;_background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_5c448026.gif)}
    .c-icon{display:inline-block;width:14px;height:14px;vertical-align:text-bottom;font-style normal;overflow:hidden;background:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_0e814c16.png) no-repeat 0 0;_background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_5c448026.gif)}.c-icon-triangle-down-blue{background-position:-480px -168px}.c-icon-chevron-unfold2{background-position:-504px -168px}#m{width:720px;margin:0 auto}#nv a,#nv b,.btn,#lk{font-size:14px}#nv{height:19px;font-size:16px;margin:0 0 4px;text-align:left;text-indent:137px}.s_btn{width:95px;height:32px;padding-top:2px\9;font-size:14px;background-color:#ddd;background-position:0 -48px;cursor:pointer}.s_btn_h{background-position:-240px -48px}.s_btn_wr{width:97px;height:34px;display:inline-block;background-position:-120px -48px;*position:relative;z-index:0;vertical-align:top}#cp .c-icon-icrlogo,#jgwab .c-icon-jgwablogo{width:14px;height:17px;display:inline-block;overflow:hidden;background:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_0e814c16.png) no-repeat;_background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_5c448026.gif)}
    #cp .c-icon-icrlogo{background-position:-600px -96px;position:relative;top:3px}#jgwab .c-icon-jgwablogo{background-position:-623px -96px;position:relative;top:3px;margin-right:6px}#shouji{margin-right:14px}#u{display:none}#c-tips-container{display:none}#wrapper{min-width:810px;height:100%;min-height:600px}#head{position:relative;padding-bottom:0;height:100%;min-height:600px}#head .head_wrapper{height:100%}#m{position:relative}#fm{padding-left:40px;top:-37px}#lh a{margin-left:62px}#lh #seth,#lh #setf{margin-left:0}#lk{position:absolute;display:none;top:0;right:0;margin:33px 0}#lk span{font:14px "宋体"}#nv{position:absolute;display:none;top:0;right:0}#lm{color:#666;width:100%;height:60px;margin-top:60px;line-height:15px;font-size:13px;position:absolute;top:0;left:0}#lm a{color:#666}#pad-version{line-height:40px}.s_ipt_wr.bg,.s_btn_wr.bg,#su.bg{background-image:none}.s_btn_wr{width:auto;height:auto;border-bottom:1px solid transparent;*border-bottom:0}.s_btn{width:100px;height:36px;color:white;font-size:15px;letter-spacing:1px;background:#3385ff;border-bottom:1px solid #2d78f4;outline:medium;*border-bottom:0;-webkit-appearance:none;-webkit-border-radius:0}
    .s_btn.btnhover{background:#317ef3;border-bottom:1px solid #2868c8;*border-bottom:0;box-shadow:1px 1px 1px #ccc}.s_btn_h{background:#3075dc;box-shadow:inset 1px 1px 5px #2964bb;-webkit-box-shadow:inset 1px 1px 5px #2964bb;-moz-box-shadow:inset 1px 1px 5px #2964bb;-o-box-shadow:inset 1px 1px 5px #2964bb}#result_logo{display:none}#index_logo img{display:inline-block;width:270px;height:129px}#s_tab{display:none}.s_form{position:relative;top:38.2%}.s_form_wrapper{position:relative;top:-191px}.s_ipt_wr{height:34px}#head .c-icon-bear-round{display:none}#form{margin:22px auto 0;width:641px;text-align:left;z-index:100}#form .bdsug,#fm .bdsug{top:35px}.bdsug{display:none;position:absolute;width:538px;background:#fff;border:1px solid #ccc;_overflow:hidden;box-shadow:1px 1px 3px #ededed;-webkit-box-shadow:1px 1px 3px #ededed;-moz-box-shadow:1px 1px 3px #ededed;-o-box-shadow:1px 1px 3px #ededed}.bdsug.bdsugbg ul{background:url(http://s1.bdstatic.com/r/www/cache/static/home/img/sugbg_6a9201c2.png) 100% 100% no-repeat;background-size:100px 110px;background-image:url(http://s1.bdstatic.com/r/www/cache/static/home/img/sugbg_d24a0811.gif)\9}
    .bdsug li{width:522px;color:#000;font:14px arial;line-height:25px;padding:0 8px;position:relative;cursor:default}.bdsug li.bdsug-s{background:#f0f0f0}.bdsug-store span,.bdsug-store b{color:#7a77c8}.bdsug-store-del{font-size:12px;color:#666;text-decoration:underline;position:absolute;right:8px;top:0;cursor:pointer;display:none}.bdsug-s .bdsug-store-del{display:inline-block}.bdsug-ala{display:inline-block;border-bottom:1px solid #e6e6e6}.bdsug-ala h3{line-height:14px;background:url(//www.baidu.com/img/sug_bd.png) no-repeat left center;margin:8px 0 5px 0;font-size:12px;font-weight:normal;color:#7b7b7b;padding-left:20px}.bdsug-ala p{font-size:14px;font-weight:bold;padding-left:20px}.bdsug .bdsug-direct{width:auto;padding:0;border-bottom:1px solid #f1f1f1}.bdsug .bdsug-direct p{color:#00c;font-weight:bold;line-height:34px;padding:0 8px;cursor:pointer;white-space:nowrap;overflow:hidden}.bdsug .bdsug-direct p img{width:16px;height:16px;margin:7px 6px 9px 0;vertical-align:middle}.bdsug .bdsug-direct p span{margin-left:8px}
    .bdsug .bdsug-direct p i{font-size:12px;line-height:100%;font-style:normal;font-weight:normal;color:#fff;background-color:#2b99ff;display:inline;text-align:center;padding:1px 5px;*padding:2px 5px 0 5px;margin-left:8px;overflow:hidden}.bdsug .bdsug-pcDirect{color:#000;font-size:14px;line-height:30px;height:30px;background-color:#f8f8f8}.bdsug .bdsug-pc-direct-tip{position:absolute;right:15px;top:8px;width:55px;height:15px;display:block;background:url(http://s1.bdstatic.com/r/www/cache/static/global/img/pc_direct_ffda303e.png) no-repeat 0 0}.bdsug li.bdsug-pcDirect-s{background-color:#f0f0f0}.bdsug .bdsug-pcDirect-is{color:#000;font-size:14px;line-height:22px;background-color:#f8f8f8}.bdsug .bdsug-pc-direct-tip-is{position:absolute;right:15px;top:3px;width:55px;height:15px;display:block;background:url(http://s1.bdstatic.com/r/www/cache/static/global/img/pc_direct_ffda303e.png) no-repeat 0 0}.bdsug li.bdsug-pcDirect-is-s{background-color:#f0f0f0}.bdsug .bdsug-pcDirect-s .bdsug-pc-direct-tip,.bdsug .bdsug-pcDirect-is-s .bdsug-pc-direct-tip-is{background-position:0 -15px}
    .bdsug .bdsug-newicon{"""

    def parse(self, response):

        item = BaiduItem()
        item['url'] = response.url
        print response.body
        item['html'] = response.body



        return item
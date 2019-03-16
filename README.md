# zhihu_liker_list
this is a spider of liker list of a Zhihu article
这个项目是为了分析知乎从0赞到20000赞的传播分析。来源参考
（Kumakuma的文章《一夜之间从知乎小透明到万赞。。。需要多少个大V扶持呢？》https://zhuanlan.zhihu.com/p/25821728?utm_source=com.doc360.client&utm_medium=social）
大概几步：1、爬取这篇文章的两万多人点赞的点赞名单及信息
         2、从两万人的名单中找出大V（粉丝较多的人），再爬取他们的粉丝名单
         3、数据分析，筛选出1中的名单中与2中的名单中重叠的名单，以此来判断哪些赞是大V拉过来的（有些许不够严谨，但已足够）
         4、用graph展示可视化效果。

本项目为Github和Gitee双同步，地址分别是：

https://github.com/fangvv/Homepage.git

https://gitee.com/fangvv/Homepage.git

主要用来存放北京交通大学系统与网络实验室的主页。

20230913说明：遇到github无法更新代码，解决方案 git config --global https.proxy 'socks5://127.0.0.1:10808' 写错无效，不开10808代理无效。

20230424说明：无奈删除了某个目录下的fontawesome.css，因Gitee部署时反馈其可能包含WeiJinWeiGui内容，实在无法理解，特此记录。

20211025说明：请拷贝使用本网站网页代码的用户注意，请在使用前务必去除HTML页面包含的statcounter计数器代码（不会影响您的正常使用），否则在您调试时该计数器会影响本网站的正常计数。另外，也不欢迎直接拷贝本站的文字或图片等内容，这些内容都是本人或者实验室相关的，一字不改地拷贝抄袭不觉得丢人吗？

20200317更新：使用Sigal - Simple Static Gallery Generator生成了实验室的静态相片图库，不再依赖于外部云存储。

20191210更新：目前可以实现两者界面的同步，主要需要修改_layout目录下的网页设计，改掉对github项目的判断以显示button，另外添加对新的assets/css/style.css的样式表引用。原因是github默认不自带cayman的显示样式，要从原始包里获取再来修改。

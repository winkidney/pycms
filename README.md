## 说明：
一个为了满足wp不能显示文章封面的问题自己做的简单博客系统，目的是发布带有封面和简介的文章。
如果你也想要运行这个程序，必须安装django1.5.1及其以上，py27及其以上（不能是3）  

另外，django的静态目录'/home/www/' ,请仔细查看pycms/settings/内的设置，将static文件夹做一个軟链接到/home/www/static。  
无需其他配置，访问bolg主页请使用'127.0.0.1:8000/blog/'，目前的页面非常有限。仅仅就绪了makepost,articles,home页面。访问admin以管理django。  

数据库请调用createdb.py进行初始化，里面包含了创建数据库的部分，请先修改数据在再运行。  
settings内的数据库请自行配置。  
如果有任何需求或者bug，也请提交给我^_^  

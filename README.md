# iCourse_so_easy
Get iCourse answer!

## 运行环境：
+ python3.x Chrome浏览器,chromedriver.exe<br>
## 说明：<br>
+ URL为测试与作业页面的URL     
 例如:https://www.icourse163.org/learn/XJTU-1003679002?tid=1207117201#/learn/testlist<br>
+ 答案存在运行生成的HTML中，与py文件同一目录下

# 版本更新：
+ V2.0 修复了一下错误，支持在使用过程中浏览器最小化，程序运行结束后可自动关闭窗口。
+ V3.0 修改获取测试列表的方式同时取消最小化窗口功能，以带来更快速的体验。
+ V3.1 可选择具体所需章节，如1,3,5;修复了由于没有p标签而无法显示判断题答案的bug;将所需环境打包进了requirement.txt,下载后请通过pip install -r requirements.txt安装依赖
# 备注：
+ 暂不支持多选及其他网课平台
+ 由于浏览器的编码原因，请使用Chrome浏览器以获得更好的体验


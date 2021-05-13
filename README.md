# IOTDesign
IOTDesign
- 智能家居系统，使用python模拟客户端设备，产生数据。使用python建立服务端，使用python的`socketserver`框架,支持多客户端连接，可以在web端控制指定家庭的指定设备（https://docs.python.org/3/library/socketserver.html） web后台使用nodejs。nodejs和python使用`.json`文件进行数据交互
- 建议使用Pycharm打开
- 所有有效文件都在`src/`目录下
- `src/include/`包含了Encode和Decode类，负责报文的编码和解码
- `src/json/`包含了实时数据json文件`j_data.json`和实时指令文件`j_instruction.json`
- `src/ss_client/`客户端，暂时有3个，可以直接运行
- `src/ss_server/`服务端，可以直接运行`ss_server.py`
- `src/web/` 该目录下的文件都是无用的，请直接进入`nodejs_io/`
-  `src/web/nodejs_io/` 在该目录下，你可以直接在终端输入`nodejs app.js`，web服务便在3000端口（如果我没记错的话）开启，浏览器访问`localhost:3000`，就可以看到正在运行的客户端。![final effect](http://p.houyz.cn/uploads/big/36a1bdd4450a25a687c97ddf8dde89fb.png)

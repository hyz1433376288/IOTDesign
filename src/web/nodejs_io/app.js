const http = require('http');
var fs = require('fs');
const app = http.createServer();//nodejs 服务器

app.on('request', (req, res) =>{
    fs.readFile(__dirname + '/index.html', function (err, data) {
        if(err){
            res.writeHead(500);
            return res.end('Error loading index.html');
        }
        res.writeHead(200);
        res.end(data);
    })
});
app.listen(3000, () =>{
    console.log("server start 3000 successfully");
});

//app初始化完成之后，传入io
const io = require('socket.io')(app);//socketio 的对象

io.on('connection', socket =>{
    console.log("new custom connect");
    //socket.emit 给浏览器发数据，需要触发浏览器注册的某个事件
    // socket.emit('send', {name: 'zs'});
    //socket.on注册事件，如果需要获取浏览器数据，就要注册一个时间，等待浏览器触发
    socket.on('j_data', data=>{
        console.log(data);
        socket.emit('send_j_data', read_j_data());
    });
    /*
    * socket(string ,data)
    * string : 事件名(任意)
    * data : data got from browser
    * */
    socket.on('hehe', data =>{
        console.log(data);
        socket.emit('send', data);
    })
});

function read_j_data() {
    const fs = require('fs');
    let rawdata = fs.readFileSync('../../json/j_data.json');
    console.log(rawdata);
    return JSON.parse(rawdata);
}



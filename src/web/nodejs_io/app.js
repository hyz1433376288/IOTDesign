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
    socket.on('j_data', data=>{
        console.log(data);
        socket.emit('send_j_data', read_j_data());
    });

    socket.on('instruction', data =>{
        try {
            fs.writeFileSync('../../json/j_instruction.json', JSON.stringify(data));
            console.log("JSON data is saved.");
        } catch (error) {
            console.error(error);
        }

    })

});
var test = 0;
function read_j_data() {
    const fs = require('fs');
    var rawdata;
    //block if read empty
    do{
        rawdata = fs.readFileSync('../../json/j_data.json');
    }while (rawdata.length === 0)

    console.log(rawdata);
    return JSON.parse(rawdata);
}



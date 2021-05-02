const http = require('http');
const server = http.createServer((req, res) =>{

    res.end('Hello world!');
});

server.listen(5000, () =>{
    console.log('server running at port 5000');
});
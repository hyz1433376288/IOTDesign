const http = require('http');
const querystring = require('querystring');

const  serverHandler =  (req, res) => {
    //业务代码
    res.setHeader('Content-Type', 'application/json');
    if(req.method === 'POST'){
        let postData = '';
        //流 stream
        req.on('data', chunk =>{
            postData += chunk.toString();
        });

        req.on('end', () => {
            console.log('postData', postData);
            res.end('I am server,I have rec');
        });
        console.log('post data content type :', req.headers['content-type']);
        // res.end(
        //     JSON.stringify({"res":"I am server,I have rec"})
        // )
    }
    // res.setHeader('Content-Type', 'application/json');
    // console.log(req);
    // const responseData = {
    //     name:'hyz',
    //     age:20
    // };
    //
    // res.end(
    //     JSON.stringify(responseData)
    // )
};
const PORT = 5000;
const server = http.createServer(serverHandler);
server.listen(PORT, () =>{
    console.log('server running at 5000');
});


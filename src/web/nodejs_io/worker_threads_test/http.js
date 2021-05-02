// http.js 修改
const http = require('http')
const { join } = require('path')
const { Worker } = require('worker_threads')

const server = http.createServer((request, response) => {
    if(request.url === '/') {
        response.setHeader('content-Type', 'text/html; charset=utf-8')
        response.statusCode = 200

        const wk1 = new Worker(join(__dirname, './worker.js'))
        const wk2 = new Worker(join(__dirname, './worker.js'))

        let result = ''
        const success = res => {
            if (result) // 判断是否已经接收到一次结果,!!!!!!此处显示到web
                response.end(`${result} <br /> ${res}`, 'utf-8')
            else
                result = res
        }

        wk1.on('message', success)
        wk2.on('message', success)
    }
})

server.listen(8080, () => {
    console.log('启动成功')
    console.log(__filename)
})

// worker.js
const { parentPort } = require('worker_threads')

const startTime = new Date().getTime()
for(let i = 0; i < 1000000000; i ++) {}
const endTime = new Date().getTime()

parentPort.postMessage(`运算1000000000次，开始运算时间：${startTime},结束运算时间${endTime}`)

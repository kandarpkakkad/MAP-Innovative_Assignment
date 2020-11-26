const { request } = require('express');
const gateway = require('fast-gateway');

const server = gateway({
  routes: [
    {
        prefix: '/take',
        target: 'http://127.0.0.1:3000'
    },
    {
        prefix: '/view',
        target: 'http://127.0.0.1:4000'
    },
    {
        prefix: '/modify',
        target: 'http://127.0.0.1:5000'
    }
]
});

server.start(2000).then(gate => {
    console.log("API Gateway running on PORT=2000");
});
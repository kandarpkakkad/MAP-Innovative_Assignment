const { request } = require('express');
const gateway = require('fast-gateway');

const server = gateway({
  routes: [
    {
        prefix: '/dashboard',
        target: 'http://127.0.0.1:7000'
    },
]
});

server.start(2222).then(gate => {
    console.log("API Gateway running on PORT=2222");
});

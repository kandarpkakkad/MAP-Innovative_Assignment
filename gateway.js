const gateway = require('fast-gateway')
const server = gateway({
  routes: [
    {
        prefix: '/take/:lecture/:class_name',
        target: 'http://127.0.0.1:2000'
    },
    {
        prefix: '/view',
        target: 'http://127.0.0.1:3000'
    },
    {
        prefix: '/modify',
        target: 'http://127.0.0.1:4000'
    }
]
});

server.start(1000).then(gate => {
    console.log("API Gateway running on PORT=1000");
});
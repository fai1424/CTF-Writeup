const vm = require("node:vm");
const http = require('http');
const querystring = require('querystring');

const getFlag = () => {
    if (process.env.FLAG === undefined) {
        return "PUCTF24{this_is_a_fake_flag}";
    } else return process.env.FLAG;
}

const server = http.createServer((req, res) => {
    if (req.method === 'POST') {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
        req.on('end', () => {
            const postBody = querystring.parse(body);
            const name = postBody.name;
            res.writeHead(200, {'Content-Type': 'text/html'});

            const userInput = "nickname = \"" + name + "\"";
            const context = {nickname: "Placeholder"};
            vm.createContext(context);
            vm.runInContext(userInput, context);

            res.end(`Hello, ${context.nickname}!`);
        });
    } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(`
            <form method="POST" action="/">
                <label for="name">Enter your name:</label><br>
                <input type="text" id="name" name="name"><br>
                <input type="submit" value="Submit">
            </form>
        `);
    }
});

server.listen(5000, () => {
    console.log('Server is running at http://localhost:5000');
});
